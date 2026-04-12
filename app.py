# LIBRARIES AND MODULES
# ---------------------

import os # Route confiration
import sys # Startup arguments
import json # JSON handling
 
from PySide6 import QtWidgets # QtWidgets
from PySide6.QtCore import QThreadPool, Slot, Qt, QByteArray # Threading, slot-decorators and Qt
from PySide6.QtGui import QPixmap, QCursor # Picture handling and cursor changes

from app_ui import Ui_MainWindow # Translated GUI class

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.threadPool = QThreadPool.globalInstance()
        self.setupUi(self)

        # connections for the menuPage buttons
        self.takePushButton.clicked.connect(self.go_to_takePage)
        self.returnPushButton.clicked.connect(self.go_to_returnPage)
        self.historyPushButton.clicked.connect(self.go_to_historyPage)

        # connections for the back buttons on each page
        self.takeBackPushButton.clicked.connect(self.go_to_menuPage)
        self.returnBackPushButton.clicked.connect(self.go_to_menuPage)
        self.historyBackPushButton.clicked.connect(self.go_to_menuPage)

    # Functions that takes the user to the connenected page
    def go_to_menuPage(self):
     self.stackedWidget.setCurrentWidget(self.menuPage)
    
    def go_to_takePage(self):
     self.stackedWidget.setCurrentWidget(self.takePage)
    
    def go_to_returnPage(self):
     self.stackedWidget.setCurrentWidget(self.returnPage)
    
    def go_to_historyPage(self):
     self.stackedWidget.setCurrentWidget(self.historyPage)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())