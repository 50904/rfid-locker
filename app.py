# LIBRARIES AND MODULES
# ---------------------

import os # Route confiration
import sys # Startup arguments
import json # JSON handling
 
from PySide6 import QtWidgets # QtWidgets
from PySide6.QtCore import QThreadPool, Slot, Qt, QByteArray # Threading, slot-decorators and Qt
from PySide6.QtGui import QPixmap, QCursor # Picture handling and cursor changes

from app_ui import Ui_MainWindow # Translated GUI class

class MainWindows(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.threadPool = QThreadPool.globalInstance()
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindows()
    window.show()

    sys.exit(app.exec())