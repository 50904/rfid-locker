# LIBRARIES AND MODULES
# ---------------------

import os # Route confiration
import sys # Startup arguments
import json # JSON handling
import importlib # Dynamic imports for platform-specific RFID modules
import time # Timing for locker operations
import ast # AST parsing for MQTT payloads
from datetime import datetime

import paho.mqtt.client as mqtt # MQTT client
import psycopg2 # PostgreSQL driver
from PySide6 import QtWidgets # QtWidgets
from PySide6.QtWidgets import QCalendarWidget, QMessageBox, QLabel, QPushButton, QVBoxLayout, QGroupBox, QScrollArea, QWidget, QTabWidget, QTableWidgetItem # UI widgets
from PySide6.QtCore import QThreadPool, Slot, Qt, QByteArray, QTimer, QDate # Threading, slot-decorators and Qt
from PySide6.QtGui import QPixmap, QCursor # Picture handling and cursor changes

from app_ui import Ui_MainWindow # Translated GUI class
DEBUG = True


if sys.platform.startswith("linux"):
    try:
        gpiozero = importlib.import_module("gpiozero")
        try:
            # Prefer local driver modules bundled with this project.
            SimpleMFRC522 = importlib.import_module("SimpleMFRC522").SimpleMFRC522
        except Exception:
            # Fallback for environments using pip-installed mfrc522 package.
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
BROKER = os.getenv("MQTT_BROKER", "192.168.251.200")
PORT = int(os.getenv("MQTT_PORT", "1883"))
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
        self.db_conn = None
        self.db_available = False
        self.local_history_rows = []
        self.take_items = []
        self.return_items = []
        self.current_rfid = None
        self.mqtt_available = False
        self.rfid_reader = None
        self.last_rfid_read_at = 0.0
        self.rfid_error_reported = False

        # Connections for the menuPage buttons
        self.takePushButton.clicked.connect(self.go_to_takePage)
        self.returnPushButton.clicked.connect(self.go_to_returnPage)
        self.historyPushButton.clicked.connect(self.go_to_historyPage)
        self.scanPageMenuPushButton.clicked.connect(self.go_to_menuPage)
        self.menuPageScanPushButton.clicked.connect(self.go_to_scanPage)

        # Locker_gui style RFID reader control on scan page.
        self.setup_scanpage_rfid_reader_controls()

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
        self.historyTableWidget.setRowCount(0)

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
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        self.client.username_pw_set("adm", "Q2werty7")
        self.init_mqtt_connection()

        # Stale locker pruning timer
        self.stale_timer = QTimer(self)
        self.stale_timer.timeout.connect(self.prune_stale_lockers)
        self.stale_timer.start(self.STALE_CHECK_INTERVAL_MS)

        # Continuous RFID scan loop for scan page.
        self.rfid_scan_timer = QTimer(self)
        self.rfid_scan_timer.timeout.connect(self.poll_rfid_scan)
        self.rfid_scan_timer.start(200)

        # PostgreSQL setup for RFID and locker event logging
        self.init_database()

        # Page-specific actions and default data for combo boxes/history table
        self.configure_page_functionality()
        self.set_info_status("Status: waiting for events...")
        
        

    # Functions that takes the user to the connenected page
    def go_to_menuPage(self):
        self.refresh_locker_combo_boxes()
        self.refresh_history_filter_options()
        self.stackedWidget.setCurrentWidget(self.menuPage)
    
    def go_to_takePage(self):
        self.refresh_locker_combo_boxes()
        self.stackedWidget.setCurrentWidget(self.takePage)
    
    def go_to_returnPage(self):
        self.refresh_locker_combo_boxes()
        self.stackedWidget.setCurrentWidget(self.returnPage)
    
    def go_to_historyPage(self):
        self.refresh_history_filter_options()
        self.load_history_table()
        self.stackedWidget.setCurrentWidget(self.historyPage)

    def go_to_scanPage(self):
        self.stackedWidget.setCurrentWidget(self.scanPage)
        if RFID_IMPORT_ERROR is None:
            self.set_info_status("Status: waiting for RFID tag...")
        else:
            self.show_error(f"RFID import failed: {RFID_IMPORT_ERROR}", show_popup=False)

    def setup_scanpage_rfid_reader_controls(self):
        """Add RFID reader controls to scanPage (locker_gui style)."""
        self.scanReadRfidPushButton = QPushButton("Lue RFID-tagi")
        self.scanReadRfidPushButton.setMinimumSize(220, 56)
        self.scanReadRfidPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.scanReadRfidPushButton.clicked.connect(self.handle_scanpage_read_button)
        self.scanReadRfidPushButton.setEnabled(RFID_IMPORT_ERROR is None)

        self.horizontalLayout_11.insertWidget(0, self.scanReadRfidPushButton)

        if RFID_IMPORT_ERROR is None:
            self.scanPageLabel.setText("RFID Reader")
            self.waitingForTagLabel.setText("RFID imports loaded. Bring tag near the reader.")
            self.scanFailedLabel.hide()
        else:
            self.scanPageLabel.setText("RFID Reader")
            self.scanFailedLabel.setText(f"RFID import failed: {RFID_IMPORT_ERROR}")
            self.scanFailedLabel.show()

    def handle_scanpage_read_button(self):
        """Manual scanPage RFID read via button."""
        self.set_info_status("Status: waiting for RFID tag...")
        self.read_rfid_tag(non_blocking=False, show_popup_on_error=True)

    def poll_rfid_scan(self):
        """Poll RFID reader continuously while scan page is visible."""
        if self.stackedWidget.currentWidget() is not self.scanPage:
            return

        self.read_rfid_tag(non_blocking=True, show_popup_on_error=False)

    def init_mqtt_connection(self):
        """Initialize MQTT connection in non-blocking mode."""
        try:
            self.client.connect_async(BROKER, PORT)
            self.client.loop_start()  # Background connection
            self.mqtt_available = False
            print(f"MQTT starting async connection to {BROKER}:{PORT}")
        except Exception as exc:
            self.mqtt_available = False
            print(f"MQTT disabled: {exc}")
            self.show_error("MQTT is offline. Application is running in offline mode.", show_popup=False)

    def set_info_status(self, message):
        """Show informational status in scan page labels."""
        self.waitingForTagLabel.setText(message)
        self.waitingForTagLabel.show()
        self.tagDetectedLabel.hide()
        self.scanFailedLabel.hide()

    def show_error(self, message, show_popup=False):
        """Show error status in scan page labels and optional popup."""
        self.scanFailedLabel.setText(message)
        self.scanFailedLabel.show()
        self.tagDetectedLabel.hide()
        if show_popup:
            QMessageBox.warning(self, "Locker Error", message)

    def configure_page_functionality(self):
        """Wire up buttons and initialize take/return/history page controls."""
        self.takeConfirmPushButton.clicked.connect(self.handle_take_confirm)
        self.returnConfirmPushButton.clicked.connect(self.handle_return_confirm)
        self.historySearchPushButton.clicked.connect(self.load_history_table)
        self.historyConfirmPushButton.clicked.connect(self.load_history_table)

        today = QDate.currentDate()
        self.historyStartDateEdit.setDate(today.addDays(-7))
        self.historyEndDateEdit.setDate(today)

        self.refresh_locker_combo_boxes()
        self.refresh_history_filter_options()
        self.load_history_table()

    def get_sorted_connected_lockers(self):
        """Return connected locker aliases in deterministic order."""
        return sorted(self.connected_lockers)

    def refresh_locker_combo_boxes(self):
        """Update take/return combo boxes from DB products when available."""
        self.refresh_product_combo_boxes()

    def ensure_product_lockers(self):
        """Hardcode locker assignment: each active product uses locker == tuotenumero."""
        if not self.db_available or self.db_conn is None:
            return

        updated_count = 0
        try:
            with self.db_conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT t.tuotenumero
                    FROM public.tuote t
                    WHERE t.aktiivinen = TRUE
                    ORDER BY t.tuotenumero
                    """
                )
                active_rows = cur.fetchall()

                if not active_rows:
                    return

                for (tuotenumero,) in active_rows:
                    lokero_number = tuotenumero
                    auto_mac = f"STATICLOC-{lokero_number:06d}"

                    cur.execute(
                        """
                        INSERT INTO public.lokerikko (lokero, mac_osoite)
                        VALUES (%s, %s)
                        ON CONFLICT (lokero) DO NOTHING
                        """,
                        (lokero_number, auto_mac),
                    )

                    # Keep exactly one locker mapping per product.
                    cur.execute(
                        """
                        DELETE FROM public.tuotesijainti
                        WHERE tuotenumero = %s
                          AND lokero <> %s
                        """,
                        (tuotenumero, lokero_number),
                    )

                    cur.execute(
                        """
                        INSERT INTO public.tuotesijainti (lokero, tuotenumero)
                        VALUES (%s, %s)
                        ON CONFLICT (lokero, tuotenumero) DO NOTHING
                        """,
                        (lokero_number, tuotenumero),
                    )

                    updated_count += 1

            if updated_count > 0:
                print(f"Applied hardcoded lockers for {updated_count} products")
        except Exception as exc:
            print(f"Failed to ensure product lockers: {exc}")

    def refresh_product_combo_boxes(self):
        """Populate TAKE/RETURN product combos using loan schema tables."""
        self.take_items = []
        self.return_items = []

        self.takeProductComboBox.blockSignals(True)
        self.returnProductcCmboBox.blockSignals(True)
        self.takeProductComboBox.clear()
        self.returnProductcCmboBox.clear()

        if not self.db_available or self.db_conn is None:
            self.takeProductComboBox.addItem("Database offline")
            self.returnProductcCmboBox.addItem("Database offline")
            self.takeProductComboBox.blockSignals(False)
            self.returnProductcCmboBox.blockSignals(False)
            return

        self.ensure_product_lockers()

        try:
            with self.db_conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT t.tuotenumero, t.tuote, COALESCE(t.tuotekuvaus, ''), ts.lokero
                    FROM public.tuote t
                    LEFT JOIN public.tuotesijainti ts ON ts.tuotenumero = t.tuotenumero
                    WHERE t.aktiivinen = TRUE
                    ORDER BY t.tuote
                    """
                )
                take_rows = cur.fetchall()

                cur.execute(
                    """
                    SELECT l.lainausnumero, t.tuotenumero, t.tuote, COALESCE(t.tuotekuvaus, ''), l.lokero, l.rfid
                    FROM public.lainaus l
                    JOIN public.tuote t ON t.tuotenumero = l.tuotenumero
                    WHERE l.palautusaika IS NULL
                    ORDER BY l.lainausaika DESC
                    """
                )
                return_rows = cur.fetchall()

            for tuotenumero, tuote, kuvaus, lokero in take_rows:
                self.take_items.append(
                    {
                        "tuotenumero": tuotenumero,
                        "tuote": tuote,
                        "kuvaus": kuvaus,
                        "lokero": lokero,
                    }
                )
                self.takeProductComboBox.addItem(f"{tuote} (locker {lokero})")

            for lainausnumero, tuotenumero, tuote, kuvaus, lokero, rfid in return_rows:
                self.return_items.append(
                    {
                        "lainausnumero": lainausnumero,
                        "tuotenumero": tuotenumero,
                        "tuote": tuote,
                        "kuvaus": kuvaus,
                        "lokero": lokero,
                        "rfid": rfid,
                    }
                )
                self.returnProductcCmboBox.addItem(f"{tuote} (locker {lokero})")

            if not self.take_items:
                self.takeProductComboBox.addItem("No products found")
            if not self.return_items:
                self.returnProductcCmboBox.addItem("No borrowed products")

        except Exception as exc:
            self.takeProductComboBox.addItem("Load failed")
            self.returnProductcCmboBox.addItem("Load failed")
            print(f"Failed to load product combos: {exc}")

        self.takeProductComboBox.blockSignals(False)
        self.returnProductcCmboBox.blockSignals(False)

    def resolve_selected_item(self, combo_box, items):
        """Resolve selected model item from combobox index."""
        idx = combo_box.currentIndex()
        if idx < 0 or idx >= len(items):
            return None
        return items[idx]

    def resolve_locker_alias(self, lokero_number):
        """Map numeric locker id to UI/MQTT alias format."""
        return f"locker{lokero_number}"

    def resolve_active_rfid(self):
        """Resolve active borrower RFID from read tag or environment setting."""
        if self.current_rfid:
            return self.current_rfid
        env_rfid = os.getenv("RFID_LOCKER_RFID")
        if env_rfid:
            return env_rfid
        if DEBUG:
            return "532127170272"
        return None

    def get_active_user_name(self):
        """Resolve a user name for tool history entries."""
        return (
            os.getenv("RFID_LOCKER_USER")
            or os.getenv("USERNAME")
            or os.getenv("USER")
            or "unknown"
        )

    def handle_take_confirm(self):
        """Confirm TAKE flow using the new loan schema."""
        selected_item = self.resolve_selected_item(self.takeProductComboBox, self.take_items)
        if selected_item is None:
            QMessageBox.warning(self, "Take", "No available product selected.")
            return

        if selected_item.get("lokero") is None:
            QMessageBox.warning(self, "Take", "Selected product has no locker location (tuotesijainti missing).")
            return

        active_rfid = self.resolve_active_rfid()
        if not active_rfid:
            QMessageBox.warning(self, "Take", "RFID is required. Scan a tag first.")
            return

        locker_alias = self.resolve_locker_alias(selected_item["lokero"])

        sent = self.send_command(locker_alias, "open")
        if not sent:
            return

        success, error_text = self.create_loan(active_rfid, selected_item)
        if not success:
            QMessageBox.warning(self, "Take", error_text)
            return

        self.refresh_product_combo_boxes()
        self.refresh_history_filter_options()
        self.load_history_table()
        QMessageBox.information(self, "Take", f"{selected_item['tuote']} borrowed from locker {selected_item['lokero']}.")

    def handle_return_confirm(self):
        """Confirm RETURN flow using the new loan schema."""
        selected_item = self.resolve_selected_item(self.returnProductcCmboBox, self.return_items)
        if selected_item is None:
            QMessageBox.warning(self, "Return", "No borrowed product selected.")
            return

        locker_alias = self.resolve_locker_alias(selected_item["lokero"])

        sent = self.send_command(locker_alias, "open")
        if not sent:
            return

        success, error_text = self.return_loan(selected_item)
        if not success:
            QMessageBox.warning(self, "Return", error_text)
            return

        self.refresh_product_combo_boxes()
        self.refresh_history_filter_options()
        self.load_history_table()
        QMessageBox.information(self, "Return", f"{selected_item['tuote']} returned to locker {selected_item['lokero']}.")

    def create_loan(self, active_rfid, selected_item):
        """Create a new loan row for selected product."""
        if not self.db_available or self.db_conn is None:
            return False, "Database is offline."

        try:
            with self.db_conn.cursor() as cur:
                cur.execute("SELECT 1 FROM public.lainaaja WHERE rfid = %s AND aktiivinen = TRUE", (active_rfid,))
                if cur.fetchone() is None:
                    return False, f"Unknown or inactive RFID: {active_rfid}"

                cur.execute(
                    """
                    INSERT INTO public.lainaus (rfid, tuotenumero, lokero)
                    VALUES (%s, %s, %s)
                    """,
                    (active_rfid, selected_item["tuotenumero"], selected_item["lokero"]),
                )
            return True, None
        except Exception as exc:
            if "violates unique constraint" in str(exc).lower():
                return False, f"Product already loaned. Must be returned first."
            return False, f"Failed to create loan: {exc}"

    def return_loan(self, selected_item):
        """Mark selected active loan as returned."""
        if not self.db_available or self.db_conn is None:
            return False, "Database is offline."

        try:
            with self.db_conn.cursor() as cur:
                cur.execute(
                    """
                    UPDATE public.lainaus
                    SET palautusaika = CURRENT_TIMESTAMP
                    WHERE lainausnumero = %s
                      AND palautusaika IS NULL
                    """,
                    (selected_item["lainausnumero"],),
                )
                if cur.rowcount == 0:
                    return False, "Selected loan was already returned."
            return True, None
        except Exception as exc:
            return False, f"Failed to return loan: {exc}"

    def get_history_rows(self):
        """Read history rows from loan schema tables."""
        if self.db_available and self.db_conn is not None:
            try:
                with self.db_conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT
                            CONCAT(a.etunimi, ' ', a.sukunimi) AS user_name,
                            t.tuote AS tool_name,
                            CONCAT('Locker ', l.lokero, ' / RFID ', l.rfid) AS tool_description,
                            l.lainausaika AS start_at,
                            l.palautusaika AS end_at
                        FROM public.lainaus l
                        JOIN public.lainaaja a ON a.rfid = l.rfid
                        JOIN public.tuote t ON t.tuotenumero = l.tuotenumero
                        ORDER BY l.lainausaika DESC
                        """
                    )
                    rows = cur.fetchall()
                    return [
                        {
                            "user": row[0],
                            "tool": row[1],
                            "tool_description": row[2],
                            "start_at": row[3],
                            "end_at": row[4],
                        }
                        for row in rows
                    ]
            except Exception as exc:
                print(f"Failed to load loan history from DB: {exc}")

        return list(reversed(self.local_history_rows))

    def refresh_history_filter_options(self):
        """Populate user/tool filters for history page."""
        rows = self.get_history_rows()
        users = sorted({row["user"] for row in rows if row.get("user")})
        tools = sorted({row["tool"] for row in rows if row.get("tool")})

        self.historyUserComboBox.blockSignals(True)
        self.historyToolComboBox.blockSignals(True)

        self.historyUserComboBox.clear()
        self.historyToolComboBox.clear()

        self.historyUserComboBox.addItem("All")
        self.historyToolComboBox.addItem("All")

        if users:
            self.historyUserComboBox.addItems(users)
        if tools:
            self.historyToolComboBox.addItems(tools)

        self.historyUserComboBox.blockSignals(False)
        self.historyToolComboBox.blockSignals(False)

    def to_datetime(self, value):
        """Convert different date/time values to datetime."""
        if isinstance(value, datetime):
            return value
        if isinstance(value, str):
            try:
                return datetime.fromisoformat(value)
            except ValueError:
                return None
        return None

    def filter_history_rows(self, rows):
        """Apply date/user/tool filters from history page to rows."""
        start_date = self.historyStartDateEdit.date().toPython()
        end_date = self.historyEndDateEdit.date().toPython()
        start_dt = datetime.combine(start_date, datetime.min.time())
        end_dt = datetime.combine(end_date, datetime.max.time())

        selected_user = self.historyUserComboBox.currentText()
        selected_tool = self.historyToolComboBox.currentText()

        filtered = []
        for row in rows:
            row_start = self.to_datetime(row.get("start_at"))
            if row_start is None:
                continue

            if row_start < start_dt or row_start > end_dt:
                continue

            if selected_user != "All" and row.get("user") != selected_user:
                continue

            if selected_tool != "All" and row.get("tool") != selected_tool:
                continue

            filtered.append(row)

        return filtered

    def format_datetime(self, value):
        """Format datetime for history table cell."""
        dt_value = self.to_datetime(value)
        if dt_value is None:
            return ""
        return dt_value.strftime("%Y-%m-%d %H:%M:%S")

    def load_history_table(self):
        """Render filtered history rows into history table widget."""
        rows = self.filter_history_rows(self.get_history_rows())

        self.historyTableWidget.setRowCount(len(rows))
        for row_index, row in enumerate(rows):
            self.historyTableWidget.setItem(row_index, 0, QTableWidgetItem(str(row.get("user", ""))))
            self.historyTableWidget.setItem(row_index, 1, QTableWidgetItem(str(row.get("tool", ""))))
            self.historyTableWidget.setItem(row_index, 2, QTableWidgetItem(str(row.get("tool_description", ""))))
            self.historyTableWidget.setItem(row_index, 3, QTableWidgetItem(self.format_datetime(row.get("start_at"))))
            self.historyTableWidget.setItem(row_index, 4, QTableWidgetItem(self.format_datetime(row.get("end_at"))))

    # ==================== RFID Reading ====================
    def read_rfid_tag(self, non_blocking=False, show_popup_on_error=True):
        """Read RFID tag from SimpleMFRC522 reader.

        Uses non-blocking polling mode when non_blocking=True.
        """
        if SimpleMFRC522 is None:
            if not self.rfid_error_reported:
                self.show_error(f"RFID import failed: {RFID_IMPORT_ERROR}", show_popup=False)
                if show_popup_on_error:
                    QMessageBox.warning(self, "RFID Error", f"RFID import failed: {RFID_IMPORT_ERROR}")
                self.rfid_error_reported = True
            return None, None
        
        try:
            if self.rfid_reader is None:
                self.rfid_reader = SimpleMFRC522()

            if non_blocking and hasattr(self.rfid_reader, "read_no_block"):
                tag_id, tag_text = self.rfid_reader.read_no_block()
            else:
                tag_id, tag_text = self.rfid_reader.read()

            if not tag_id:
                return None, None

            now = time.monotonic()
            # Avoid flooding UI with the same tag repeatedly during continuous polling.
            if self.current_rfid == str(tag_id) and (now - self.last_rfid_read_at) < 1.5:
                return tag_id, tag_text

            self.current_rfid = str(tag_id)
            self.last_rfid_read_at = now
            self.tagDetectedLabel.setText(f"Tag detected: {tag_id}")
            self.tagDetectedLabel.show()
            self.scanFailedLabel.hide()
            self.waitingForTagLabel.setText("Tag read successfully")
            self.refresh_product_combo_boxes()
            print(f"RFID Tag Read - ID: {tag_id}, Text: {tag_text}")
            return tag_id, tag_text
        except Exception as exc:
            self.show_error(f"RFID read failed: {exc}", show_popup=False)
            if show_popup_on_error:
                QMessageBox.warning(self, "RFID Error", f"RFID read failed: {exc}")
            return None, None

    # ==================== Locker Control ====================
    def send_command(self, locker_id, operation):
        """Send control command to locker via MQTT."""
        if not self.mqtt_available:
            self.show_error("MQTT is offline. Command was not sent.", show_popup=True)
            return False

        if locker_id in self.locker_mac_map and locker_id not in self.connected_lockers:
            self.show_error(f"Error: {locker_id} disconnected.", show_popup=True)
            return False

        target_locker_id = self.locker_mac_map.get(locker_id, locker_id)
        msg = {
            "locker_id": target_locker_id,
            "operation": operation
        }
        self.client.publish(TOPIC_CONTROL, json.dumps(msg))
        response_timeout_ms = 9000 if operation == "blink" else self.COMMAND_RESPONSE_TIMEOUT_MS
        self.start_pending_operation(locker_id, operation, response_timeout_ms)
        self.set_info_status(f"Status: {locker_id} {operation} command sent...")
        print(f"Sent command: {msg}")
        return True

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
        self.show_error(error_msg, show_popup=True)
        print(error_msg)

    # ==================== MQTT Handlers ====================
    def on_connect(self, client, userdata, flags, rc):
        """MQTT connect callback."""
        if rc == 0:
            self.mqtt_available = True
            print("Connected to MQTT broker")
            self.set_info_status("Status: connected to MQTT broker")
        else:
            self.mqtt_available = False
            print(f"MQTT connect returned error code: {rc}")
            self.show_error(f"MQTT connect failed (code {rc})", show_popup=False)

        if self.mqtt_available:
            client.subscribe(TOPIC_ACTION)
            client.subscribe("locker/info")

    def on_disconnect(self, client, userdata, rc):
        """MQTT disconnect callback."""
        self.mqtt_available = False
        if rc != 0:
            self.show_error("MQTT disconnected unexpectedly.", show_popup=False)
            print(f"MQTT disconnected unexpectedly (code {rc})")
        else:
            print("MQTT disconnected")

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
            trigger = data.get("trigger") or data.get("lock", "unknown")

            if not locker_id:
                return

            if self.is_disconnect_event(event):
                disconnected_alias = self.mac_locker_map.get(locker_id, locker_id)
                self.remove_locker_by_identifier(locker_id)
                self.show_error(
                    f"Error: {disconnected_alias} disconnected. Cannot control until reconnect.",
                    show_popup=False,
                )
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
            self.refresh_locker_combo_boxes()

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
            self.set_info_status(f"Status: {ui_locker_id} {trigger} / {event}")

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

        alias = None
        if self.db_available and self.db_conn is not None:
            try:
                with self.db_conn.cursor() as cur:
                    cur.execute("SELECT lokero FROM public.lokerikko WHERE mac_osoite = %s", (mac,))
                    row = cur.fetchone()
                    if row is not None:
                        alias = f"locker{row[0]}"
            except Exception as exc:
                print(f"MAC->locker mapping lookup failed: {exc}")

        if alias is None:
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
        self.refresh_locker_combo_boxes()
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

    # ==================== LED Blinking Animations ====================
    def start_blink_animation(self, locker_id):
        """Start LED color blinking animation (RGB cycle)."""
        if locker_id not in self.locker_leds:
            return

        self.stop_door_blink_animation(locker_id)
        self.stop_blink_animation(locker_id)
        self.blink_animation_steps[locker_id] = 0

        timer = QTimer(self)
        timer.timeout.connect(lambda lid=locker_id: self.advance_blink_animation(lid))
        timer.start(300)
        self.blink_animation_timers[locker_id] = timer
        self.advance_blink_animation(locker_id)

    def advance_blink_animation(self, locker_id):
        """Advance LED blinking animation to next color in sequence."""
        sequence = [
            ("#dc2626", "RED"),
            ("#16a34a", "GREEN"),
            ("#2563eb", "BLUE"),
        ]
        step = self.blink_animation_steps.get(locker_id, 0)
        color, text = sequence[step % len(sequence)]
        self.set_led_indicator(locker_id, color, text)
        self.blink_animation_steps[locker_id] = step + 1

    def stop_blink_animation(self, locker_id):
        """Stop LED color blinking animation and reset to idle."""
        timer = self.blink_animation_timers.pop(locker_id, None)
        if timer is not None:
            timer.stop()
            timer.deleteLater()
        self.blink_animation_steps.pop(locker_id, None)

        led = self.locker_leds.get(locker_id)
        if led is not None:
            self.set_led_indicator(locker_id, "#64748b", "IDLE")

    def start_door_blink_animation(self, locker_id):
        """Start LED door-open blinking animation (blue/idle alternate)."""
        if locker_id not in self.locker_leds:
            return

        if locker_id in self.blink_animation_timers:
            return

        if locker_id in self.door_blink_timers:
            return

        self.stop_blink_animation(locker_id)
        self.stop_door_blink_animation(locker_id)
        self.door_blink_steps[locker_id] = 0

        timer = QTimer(self)
        timer.timeout.connect(lambda lid=locker_id: self.advance_door_blink_animation(lid))
        timer.start(220)
        self.door_blink_timers[locker_id] = timer
        self.advance_door_blink_animation(locker_id)

    def advance_door_blink_animation(self, locker_id):
        """Advance LED door-open blinking animation (toggle blue/idle)."""
        if not self.door_open_states.get(locker_id, False):
            self.stop_door_blink_animation(locker_id)
            return

        step = self.door_blink_steps.get(locker_id, 0)

        if step % 2 == 0:
            self.set_led_indicator(locker_id, "#2563eb", "BLUE")
        else:
            self.set_led_indicator(locker_id, "#64748b", "IDLE")

        self.door_blink_steps[locker_id] = step + 1

    def stop_door_blink_animation(self, locker_id):
        """Stop LED door-open blinking animation and reset to idle."""
        timer = self.door_blink_timers.pop(locker_id, None)
        if timer is not None:
            timer.stop()
            timer.deleteLater()
        self.door_blink_steps.pop(locker_id, None)

        led = self.locker_leds.get(locker_id)
        if led is not None:
            self.set_led_indicator(locker_id, "#64748b", "IDLE")

    def set_led_indicator(self, locker_id, color, text):
        """Set LED indicator color and text."""
        led = self.locker_leds.get(locker_id)
        if led is not None:
            led.setText(text)
            led.setStyleSheet(f"background-color: {color}; color: white; font-weight: bold;")

    # ==================== PostgreSQL ====================
    def init_database(self):
        """Connect to PostgreSQL and ensure loan schema tables exist."""
        try:
            self.db_conn = psycopg2.connect(
                host=os.getenv("PGHOST", "192.168.251.200"),
                port=int(os.getenv("PGPORT", "5432")),
                dbname=os.getenv("PGDATABASE", "rfid_lokero"),
                user=os.getenv("PGUSER", "postgres"),
                password=os.getenv("PGPASSWORD", "Q2werty7"),
            )
            self.db_conn.autocommit = True

            with self.db_conn.cursor() as cur:
                cur.execute(
                    """
                    DROP TABLE IF EXISTS public.tool_history;
                    DROP TABLE IF EXISTS public.locker_events;
                    DROP TABLE IF EXISTS public.rfid_reads;
                    """
                )
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS public.oikeustaso (
                        oikeustaso INTEGER PRIMARY KEY,
                        rooli VARCHAR(20) NOT NULL UNIQUE
                    )
                    """
                )
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS public.lainaaja (
                        etunimi VARCHAR(50) NOT NULL,
                        sukunimi VARCHAR(50) NOT NULL,
                        oikeustaso INTEGER NOT NULL,
                        tunnus VARCHAR(200) NOT NULL UNIQUE,
                        rfid VARCHAR(50) PRIMARY KEY,
                        aktiivinen BOOLEAN NOT NULL DEFAULT TRUE,
                        FOREIGN KEY (oikeustaso)
                            REFERENCES public.oikeustaso(oikeustaso)
                            ON UPDATE CASCADE
                            ON DELETE RESTRICT
                    )
                    """
                )
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS public.lokerikko (
                        lokero INTEGER PRIMARY KEY,
                        mac_osoite VARCHAR(20) NOT NULL UNIQUE
                    )
                    """
                )
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS public.tuote (
                        tuotenumero INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                        tuote VARCHAR(100) NOT NULL,
                        tuotekuvaus VARCHAR(500),
                        aktiivinen BOOLEAN NOT NULL DEFAULT TRUE
                    )
                    """
                )
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS public.tuotesijainti (
                        lokero INTEGER NOT NULL,
                        tuotenumero INTEGER NOT NULL,
                        PRIMARY KEY (lokero, tuotenumero),
                        FOREIGN KEY (tuotenumero)
                            REFERENCES public.tuote(tuotenumero)
                            ON DELETE RESTRICT,
                        FOREIGN KEY (lokero)
                            REFERENCES public.lokerikko(lokero)
                            ON DELETE RESTRICT
                    )
                    """
                )
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS public.lainaus (
                        lainausnumero INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                        rfid VARCHAR(50) NOT NULL,
                        tuotenumero INTEGER NOT NULL,
                        lokero INTEGER NOT NULL,
                        lainausaika TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                        palautusaika TIMESTAMP,
                        FOREIGN KEY (rfid)
                            REFERENCES public.lainaaja(rfid)
                            ON DELETE RESTRICT,
                        FOREIGN KEY (tuotenumero)
                            REFERENCES public.tuote(tuotenumero)
                            ON DELETE RESTRICT,
                        FOREIGN KEY (lokero)
                            REFERENCES public.lokerikko(lokero)
                            ON DELETE RESTRICT,
                        CONSTRAINT chk_aika CHECK (palautusaika IS NULL OR palautusaika > lainausaika)
                    )
                    """
                )
                cur.execute("CREATE INDEX IF NOT EXISTS idx_lainaus_rfid ON public.lainaus(rfid)")
                cur.execute("CREATE INDEX IF NOT EXISTS idx_lainaus_tuotenumero ON public.lainaus(tuotenumero)")
                cur.execute("CREATE INDEX IF NOT EXISTS idx_lainaus_lokero ON public.lainaus(lokero)")
                cur.execute(
                    """
                    CREATE UNIQUE INDEX IF NOT EXISTS unique_active_lainaus
                    ON public.lainaus(tuotenumero)
                    WHERE palautusaika IS NULL
                    """
                )

            self.db_available = True
            print("PostgreSQL enabled with loan schema tables")
        except Exception as exc:
            self.db_available = False
            self.db_conn = None
            print(f"PostgreSQL disabled: {exc}")

    def closeEvent(self, event):
        """Close MQTT loop and DB connection cleanly."""
        try:
            self.client.loop_stop()
            self.client.disconnect()
        except Exception:
            pass

        try:
            if self.db_conn is not None:
                self.db_conn.close()
        except Exception:
            pass

        super().closeEvent(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())