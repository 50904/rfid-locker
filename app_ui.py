# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1122, 874)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(115, 115, 115);")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.Box)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setMinimumSize(QSize(120, 80))
        self.stackedWidget.setFrameShape(QFrame.Shape.Box)
        self.scanPage = QWidget()
        self.scanPage.setObjectName(u"scanPage")
        self.stackedWidget.addWidget(self.scanPage)
        self.menuPage = QWidget()
        self.menuPage.setObjectName(u"menuPage")
        self.verticalLayout_2 = QVBoxLayout(self.menuPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.lableFrame = QFrame(self.menuPage)
        self.lableFrame.setObjectName(u"lableFrame")
        self.lableFrame.setFrameShape(QFrame.Shape.Box)
        self.lableFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout = QHBoxLayout(self.lableFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.lableFrame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.TextFormat.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setIndent(-1)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.lableFrame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.buttonFrame = QFrame(self.menuPage)
        self.buttonFrame.setObjectName(u"buttonFrame")
        sizePolicy.setHeightForWidth(self.buttonFrame.sizePolicy().hasHeightForWidth())
        self.buttonFrame.setSizePolicy(sizePolicy)
        self.buttonFrame.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.buttonFrame.setFrameShape(QFrame.Shape.Box)
        self.buttonFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout = QGridLayout(self.buttonFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 4, 2, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 6, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 6, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 2, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_5, 7, 1, 1, 1)

        self.historyPushButton = QPushButton(self.buttonFrame)
        self.historyPushButton.setObjectName(u"historyPushButton")
        sizePolicy.setHeightForWidth(self.historyPushButton.sizePolicy().hasHeightForWidth())
        self.historyPushButton.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(22)
        self.historyPushButton.setFont(font1)
        self.historyPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.historyPushButton.setStyleSheet(u"background-color: rgb(65, 65, 65);")

        self.gridLayout.addWidget(self.historyPushButton, 6, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_7, 3, 1, 1, 1)

        self.returnPushButton = QPushButton(self.buttonFrame)
        self.returnPushButton.setObjectName(u"returnPushButton")
        sizePolicy.setHeightForWidth(self.returnPushButton.sizePolicy().hasHeightForWidth())
        self.returnPushButton.setSizePolicy(sizePolicy)
        self.returnPushButton.setFont(font1)
        self.returnPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.returnPushButton.setStyleSheet(u"background-color: rgb(65, 65, 65);")

        self.gridLayout.addWidget(self.returnPushButton, 4, 1, 1, 1)

        self.takePushButton = QPushButton(self.buttonFrame)
        self.takePushButton.setObjectName(u"takePushButton")
        sizePolicy.setHeightForWidth(self.takePushButton.sizePolicy().hasHeightForWidth())
        self.takePushButton.setSizePolicy(sizePolicy)
        self.takePushButton.setFont(font1)
        self.takePushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.takePushButton.setStyleSheet(u"background-color: rgb(65, 65, 65);")

        self.gridLayout.addWidget(self.takePushButton, 2, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 4, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_6, 5, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_4, 1, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.buttonFrame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.menuPage)
        self.takePage = QWidget()
        self.takePage.setObjectName(u"takePage")
        self.verticalLayout_5 = QVBoxLayout(self.takePage)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.takeProductFrame = QFrame(self.takePage)
        self.takeProductFrame.setObjectName(u"takeProductFrame")
        self.takeProductFrame.setFrameShape(QFrame.Shape.Box)
        self.takeProductFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout_2 = QGridLayout(self.takeProductFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_10, 4, 1, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.verticalSpacer_9, 2, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_10, 3, 0, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_11, 3, 2, 1, 1)

        self.takeProductcCmboBox = QComboBox(self.takeProductFrame)
        self.takeProductcCmboBox.setObjectName(u"takeProductcCmboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.takeProductcCmboBox.sizePolicy().hasHeightForWidth())
        self.takeProductcCmboBox.setSizePolicy(sizePolicy1)
        self.takeProductcCmboBox.setMinimumSize(QSize(500, 50))

        self.gridLayout_2.addWidget(self.takeProductcCmboBox, 3, 1, 1, 1)

        self.takeProductLabel = QLabel(self.takeProductFrame)
        self.takeProductLabel.setObjectName(u"takeProductLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.takeProductLabel.sizePolicy().hasHeightForWidth())
        self.takeProductLabel.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(24)
        self.takeProductLabel.setFont(font2)
        self.takeProductLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.takeProductLabel, 1, 1, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.verticalSpacer_11, 0, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.takeProductFrame)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_5.addItem(self.verticalSpacer_8)

        self.takeProductBtnFrame = QFrame(self.takePage)
        self.takeProductBtnFrame.setObjectName(u"takeProductBtnFrame")
        self.takeProductBtnFrame.setFrameShape(QFrame.Shape.Box)
        self.takeProductBtnFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.takeProductBtnFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_9)

        self.takeBackPushButton = QPushButton(self.takeProductBtnFrame)
        self.takeBackPushButton.setObjectName(u"takeBackPushButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.takeBackPushButton.sizePolicy().hasHeightForWidth())
        self.takeBackPushButton.setSizePolicy(sizePolicy3)
        self.takeBackPushButton.setMinimumSize(QSize(200, 60))

        self.horizontalLayout_2.addWidget(self.takeBackPushButton)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_12)

        self.takeConfirmPushButton = QPushButton(self.takeProductBtnFrame)
        self.takeConfirmPushButton.setObjectName(u"takeConfirmPushButton")
        sizePolicy3.setHeightForWidth(self.takeConfirmPushButton.sizePolicy().hasHeightForWidth())
        self.takeConfirmPushButton.setSizePolicy(sizePolicy3)
        self.takeConfirmPushButton.setMinimumSize(QSize(200, 60))

        self.horizontalLayout_2.addWidget(self.takeConfirmPushButton)


        self.verticalLayout_5.addWidget(self.takeProductBtnFrame)

        self.stackedWidget.addWidget(self.takePage)
        self.returnPage = QWidget()
        self.returnPage.setObjectName(u"returnPage")
        self.verticalLayout_4 = QVBoxLayout(self.returnPage)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.returnProductFrame = QFrame(self.returnPage)
        self.returnProductFrame.setObjectName(u"returnProductFrame")
        self.returnProductFrame.setFrameShape(QFrame.Shape.Box)
        self.returnProductFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout_3 = QGridLayout(self.returnProductFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_12, 4, 1, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.verticalSpacer_13, 2, 1, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_15, 3, 0, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_16, 3, 2, 1, 1)

        self.returnProductcCmboBox = QComboBox(self.returnProductFrame)
        self.returnProductcCmboBox.setObjectName(u"returnProductcCmboBox")
        sizePolicy1.setHeightForWidth(self.returnProductcCmboBox.sizePolicy().hasHeightForWidth())
        self.returnProductcCmboBox.setSizePolicy(sizePolicy1)
        self.returnProductcCmboBox.setMinimumSize(QSize(500, 50))

        self.gridLayout_3.addWidget(self.returnProductcCmboBox, 3, 1, 1, 1)

        self.returnProductLabel = QLabel(self.returnProductFrame)
        self.returnProductLabel.setObjectName(u"returnProductLabel")
        sizePolicy2.setHeightForWidth(self.returnProductLabel.sizePolicy().hasHeightForWidth())
        self.returnProductLabel.setSizePolicy(sizePolicy2)
        self.returnProductLabel.setFont(font2)
        self.returnProductLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.returnProductLabel, 1, 1, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.verticalSpacer_14, 0, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.returnProductFrame)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_4.addItem(self.verticalSpacer_15)

        self.returnProductBtnFrame = QFrame(self.returnPage)
        self.returnProductBtnFrame.setObjectName(u"returnProductBtnFrame")
        self.returnProductBtnFrame.setFrameShape(QFrame.Shape.Box)
        self.returnProductBtnFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.returnProductBtnFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_13)

        self.returnBackPushButton = QPushButton(self.returnProductBtnFrame)
        self.returnBackPushButton.setObjectName(u"returnBackPushButton")
        sizePolicy3.setHeightForWidth(self.returnBackPushButton.sizePolicy().hasHeightForWidth())
        self.returnBackPushButton.setSizePolicy(sizePolicy3)
        self.returnBackPushButton.setMinimumSize(QSize(200, 60))

        self.horizontalLayout_3.addWidget(self.returnBackPushButton)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_14)

        self.returnConfirmPushButton = QPushButton(self.returnProductBtnFrame)
        self.returnConfirmPushButton.setObjectName(u"returnConfirmPushButton")
        sizePolicy3.setHeightForWidth(self.returnConfirmPushButton.sizePolicy().hasHeightForWidth())
        self.returnConfirmPushButton.setSizePolicy(sizePolicy3)
        self.returnConfirmPushButton.setMinimumSize(QSize(200, 60))

        self.horizontalLayout_3.addWidget(self.returnConfirmPushButton)


        self.verticalLayout_4.addWidget(self.returnProductBtnFrame)

        self.stackedWidget.addWidget(self.returnPage)
        self.historyPage = QWidget()
        self.historyPage.setObjectName(u"historyPage")
        self.stackedWidget.addWidget(self.historyPage)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.verticalLayout_3.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1122, 33))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"RFID-Locker", None))
        self.historyPushButton.setText(QCoreApplication.translate("MainWindow", u"HISTORY", None))
        self.returnPushButton.setText(QCoreApplication.translate("MainWindow", u"RETURN", None))
        self.takePushButton.setText(QCoreApplication.translate("MainWindow", u"TAKE", None))
        self.takeProductLabel.setText(QCoreApplication.translate("MainWindow", u"SELECT PRODUCT", None))
        self.takeBackPushButton.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.takeConfirmPushButton.setText(QCoreApplication.translate("MainWindow", u"CONFIRM", None))
        self.returnProductLabel.setText(QCoreApplication.translate("MainWindow", u"SELECT PRODUCT", None))
        self.returnBackPushButton.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.returnConfirmPushButton.setText(QCoreApplication.translate("MainWindow", u"CONFIRM", None))
    # retranslateUi

