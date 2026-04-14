# LIBRARIES AND MODULES
# ---------------------

import os # Route confiration
import sys # Startup arguments
import json # JSON handling
import importlib # Dynamic imports for platform-specific RFID modules
import time # Timing for locker operations
import ast # AST parsing for MQTT payloads

import paho.mqtt.client as mqtt # MQTT client
from PySide6 import QtWidgets # QtWidgets
from PySide6.QtWidgets import QCalendarWidget, QMessageBox, QLabel, QPushButton, QVBoxLayout, QGroupBox, QScrollArea, QWidget, QTabWidget # UI widgets
from PySide6.QtCore import QThreadPool, Slot, Qt, QByteArray, QTimer # Threading, slot-decorators and Qt
from PySide6.QtGui import QPixmap, QCursor # Picture handling and cursor changes

from app_ui import Ui_MainWindow # Translated GUI class


if sys.platform.startswith("linux"):
    try:
        gpiozero = importlib.import_module("gpiozero")
        SimpleMFRC522 = importlib.import_module("mfrc522").SimpleMFRC522
        #joyit_module = importlib.import_module("/home/adm/RFID-Testi/MFRC522-python/src/JoyIT_RC522/JoyIT_RC522")
        RFID_IMPORT_ERROR = None
    except Exception as exc:
        gpiozero = None
        SimpleMFRC522 = None
        RFID_IMPORT_ERROR = str(exc)
else:
    gpiozero = None
    SimpleMFRC522 = None
    RFID_IMPORT_ERROR = "RFID reading is available only on Linux/Raspberry Pi (requires spidev)."

# MQTT settings
BROKER = "192.168.251.200"
PORT = 1883
TOPIC_CONTROL = "locker/control"
TOPIC_ACTION = "locker/action"

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    LOCKER_TIMEOUT_SECONDS = 10
    STALE_CHECK_INTERVAL_MS = 10000
    COMMAND_RESPONSE_TIMEOUT_MS = 2000

    def __init__(self):
        super().__init__()

        self.threadPool = QThreadPool.globalInstance()
        self.setupUi(self)
        
        # Locker state management variables
        self.lockers = {}  # {locker_id: QLabel}
        self.locker_widgets = {}  # {locker_id: QGroupBox}
        self.locker_buttons = {}  # {locker_id: {"open": QPushButton, "close": QPushButton}}
        self.locker_leds = {}  # {locker_id: QLabel}
        self.locker_mac_map = {}  # {locker_alias: mac}
        self.mac_locker_map = {}  # {mac: locker_alias}
        self.connected_lockers = set()  # currently connected locker aliases
        self.locker_last_seen = {}  # {locker_alias: monotonic_seconds}
        self.pending_operations = {}  # {locker_alias: operation}
        self.pending_operation_timers = {}  # {locker_alias: QTimer}
        self.blink_animation_timers = {}  # {locker_alias: QTimer}
        self.blink_animation_steps = {}  # {locker_alias: int}
        self.door_blink_timers = {}  # {locker_alias: QTimer}
        self.door_blink_steps = {}  # {locker_alias: int}
        self.door_open_states = {}  # {locker_alias: bool}
        self.next_locker_number = 1

        # Connections for the menuPage buttons
        self.takePushButton.clicked.connect(self.go_to_takePage)
        self.returnPushButton.clicked.connect(self.go_to_returnPage)
        self.historyPushButton.clicked.connect(self.go_to_historyPage)
        self.scanPageMenuPushButton.clicked.connect(self.go_to_menuPage)

        # Connections for the back buttons on each page
        self.takeBackPushButton.clicked.connect(self.go_to_menuPage)
        self.returnBackPushButton.clicked.connect(self.go_to_menuPage)
        self.historyBackPushButton.clicked.connect(self.go_to_menuPage)

        # Set a default size for all columns in the history tableWidget
        self.historyTableWidget.setColumnWidth(0,208)
        self.historyTableWidget.setColumnWidth(1,208)
        self.historyTableWidget.setColumnWidth(2,208)
        self.historyTableWidget.setColumnWidth(3,208)
        self.historyTableWidget.setColumnWidth(4,208)

        # Variables to be used in resizing DateEdit widget's size
        calendarStart = QCalendarWidget()
        calendarStart.setMinimumSize(500,400)

        calendarEnd = QCalendarWidget()
        calendarEnd.setMinimumSize(500,400)

        # Variables to be used in resizing DateEdit widget's font
        calendarStartFont = calendarStart.font()
        calendarStartFont.setPointSize(18)

        calendarEndFont = calendarStart.font()
        calendarEndFont.setPointSize(18)

        # Resizeing the calendar in QDateEdit widget
        self.historyStartDateEdit.setCalendarWidget(calendarStart)
        self.historyEndDateEdit.setCalendarWidget(calendarEnd)

        # Resizeing the calendar font size in QDateEdit widget
        calendarStart.setFont(calendarStartFont)
        calendarEnd.setFont(calendarEndFont)
        
        # MQTT client setup
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.username_pw_set("adm", "Q2werty7")
        self.client.connect(BROKER, PORT)
        self.client.loop_start()  # Background connection

        # Stale locker pruning timer
        self.stale_timer = QTimer(self)
        self.stale_timer.timeout.connect(self.prune_stale_lockers)
        self.stale_timer.start(self.STALE_CHECK_INTERVAL_MS)
        
        

    # Functions that takes the user to the connenected page
    def go_to_menuPage(self):
     self.stackedWidget.setCurrentWidget(self.menuPage)
    
    def go_to_takePage(self):
     self.stackedWidget.setCurrentWidget(self.takePage)
    
    def go_to_returnPage(self):
     self.stackedWidget.setCurrentWidget(self.returnPage)
    
    def go_to_historyPage(self):
     self.stackedWidget.setCurrentWidget(self.historyPage)

    def go_to_scanPage(self):
     self.stackedWidget.setCurrentWidget(self.scanPage)

    # ==================== RFID Reading ====================
    def read_rfid_tag(self):
        """Read RFID tag from SimpleMFRC522 reader."""
        if SimpleMFRC522 is None:
            QMessageBox.warning(self, "RFID Error", f"RFID import failed: {RFID_IMPORT_ERROR}")
            return None, None
        
        try:
            reader = SimpleMFRC522()
            tag_id, tag_text = reader.read()
            print(f"RFID Tag Read - ID: {tag_id}, Text: {tag_text}")
            return tag_id, tag_text
        except Exception as exc:
            QMessageBox.warning(self, "RFID Error", f"RFID read failed: {exc}")
            return None, None

    # ==================== Locker Control ====================
    def send_command(self, locker_id, operation):
        """Send control command to locker via MQTT."""
        if locker_id in self.locker_mac_map and locker_id not in self.connected_lockers:
            QMessageBox.warning(self, "Locker Error", f"Error: {locker_id} disconnected.")
            return

        target_locker_id = self.locker_mac_map.get(locker_id, locker_id)
        msg = {
            "locker_id": target_locker_id,
            "operation": operation
        }
        self.client.publish(TOPIC_CONTROL, json.dumps(msg))
        response_timeout_ms = 9000 if operation == "blink" else self.COMMAND_RESPONSE_TIMEOUT_MS
        self.start_pending_operation(locker_id, operation, response_timeout_ms)
        print(f"Sent command: {msg}")

    def start_pending_operation(self, locker_id, operation, timeout_ms):
        """Start tracking pending locker operation with timeout."""
        self.clear_pending_operation(locker_id)
        self.pending_operations[locker_id] = operation

        timer = QTimer(self)
        timer.setSingleShot(True)
        timer.timeout.connect(lambda lid=locker_id, op=operation: self.on_operation_timeout(lid, op))
        timer.start(timeout_ms)
        self.pending_operation_timers[locker_id] = timer

    def clear_pending_operation(self, locker_id):
        """Clear pending operation and stop its timer."""
        timer = self.pending_operation_timers.pop(locker_id, None)
        if timer is not None:
            timer.stop()
            timer.deleteLater()
        self.pending_operations.pop(locker_id, None)

    def on_operation_timeout(self, locker_id, operation):
        """Handle pending operation timeout."""
        pending_operation = self.pending_operations.get(locker_id)
        if pending_operation != operation:
            return

        self.clear_pending_operation(locker_id)
        error_msg = f"Error: no response from {locker_id}. Locker may be unreachable."
        QMessageBox.warning(self, "Locker Error", error_msg)
        print(error_msg)

    # ==================== MQTT Handlers ====================
    def on_connect(self, client, userdata, flags, rc):
        """MQTT connect callback."""
        print("Connected to MQTT broker")
        client.subscribe(TOPIC_ACTION)
        client.subscribe("locker/info")

    def on_message(self, client, userdata, msg):
        """MQTT message callback - route to main thread."""
        payload = msg.payload.decode("utf-8")
        QTimer.singleShot(0, lambda: self.handle_message(msg.topic, payload))

    def handle_message(self, topic, payload):
        """Handle incoming MQTT messages."""
        try:
            if topic not in {TOPIC_ACTION, "locker/info"}:
                return

            data = self.parse_message_payload(payload)
            locker_id = data.get("locker_id")
            event = data.get("event", "")

            if not locker_id:
                return

            if self.is_disconnect_event(event):
                disconnected_alias = self.mac_locker_map.get(locker_id, locker_id)
                self.remove_locker_by_identifier(locker_id)
                print(f"Locker disconnected: {locker_id}")
                return

            ui_locker_id = locker_id
            if self.is_mac_address(locker_id):
                ui_locker_id = self.register_locker_mac(locker_id)
            elif locker_id in self.mac_locker_map:
                ui_locker_id = self.mac_locker_map[locker_id]
                self.connected_lockers.add(ui_locker_id)

            if ui_locker_id not in self.lockers:
                print(f"New locker discovered: {ui_locker_id}")

            self.mark_locker_seen(ui_locker_id)

            trigger = data.get("trigger") or data.get("lock", "unknown")
            
            # Handle pending operations
            if topic == TOPIC_ACTION and ui_locker_id in self.pending_operations:
                pending_operation = self.pending_operations.get(ui_locker_id)
                if pending_operation == "blink":
                    if trigger == "blink" and event == "done":
                        self.clear_pending_operation(ui_locker_id)
                else:
                    if trigger == "lock" and event in {"open", "closed"}:
                        self.clear_pending_operation(ui_locker_id)

            print(f"Locker {ui_locker_id}: {trigger} / {event}")

        except Exception as e:
            print(f"Message parse failed: {e}")

    def parse_message_payload(self, payload):
        """Parse JSON or AST literal from MQTT payload."""
        try:
            return json.loads(payload)
        except json.JSONDecodeError:
            return ast.literal_eval(payload)

    def is_mac_address(self, value):
        """Check if value is valid MAC address."""
        if not isinstance(value, str):
            return False
        parts = value.split(":")
        if len(parts) != 6:
            return False
        return all(len(part) == 2 and all(char in "0123456789abcdefABCDEF" for char in part) for part in parts)

    def is_disconnect_event(self, event):
        """Check if event indicates disconnection."""
        if not isinstance(event, str):
            return False
        normalized = event.strip().lower()
        return normalized in {"disconnected", "offline", "lost", "dropped"}

    def register_locker_mac(self, mac):
        """Register locker MAC address and create mapping."""
        if mac in self.mac_locker_map:
            alias = self.mac_locker_map[mac]
            self.connected_lockers.add(alias)
            self.mark_locker_seen(alias)
            print(f"Reconnected: {alias}")
            return alias

        alias = f"locker{self.next_locker_number}"
        self.next_locker_number += 1
        self.locker_mac_map[alias] = mac
        self.mac_locker_map[mac] = alias
        self.connected_lockers.add(alias)
        self.mark_locker_seen(alias)
        print(f"Mapped {alias} -> {mac}")
        return alias

    def mark_locker_seen(self, locker_alias):
        """Update last seen timestamp for locker."""
        self.locker_last_seen[locker_alias] = time.monotonic()

    def remove_locker_by_identifier(self, locker_identifier):
        """Remove locker from UI and disconnect tracking."""
        locker_alias = locker_identifier
        if locker_identifier in self.mac_locker_map:
            locker_alias = self.mac_locker_map[locker_identifier]

        self.clear_pending_operation(locker_alias)
        self.connected_lockers.discard(locker_alias)
        self.locker_last_seen.pop(locker_alias, None)
        print(f"Locker removed: {locker_alias}")

    def prune_stale_lockers(self):
        """Remove lockers that haven't been seen recently."""
        now = time.monotonic()
        stale_aliases = [
            alias
            for alias, last_seen in self.locker_last_seen.items()
            if now - last_seen > self.LOCKER_TIMEOUT_SECONDS
        ]

        for alias in stale_aliases:
            self.remove_locker_by_identifier(alias)
            print(f"Locker timed out: {alias}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())