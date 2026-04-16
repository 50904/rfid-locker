# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import RFIDmerkki_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(848, 797)
        MainWindow.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        MainWindow.setStyleSheet(u"background-color: rgb(65, 65, 65);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(115, 115, 115);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setMinimumSize(QSize(120, 80))
        self.stackedWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.scanPage = QWidget()
        self.scanPage.setObjectName(u"scanPage")
        self.verticalLayout_8 = QVBoxLayout(self.scanPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.scanPageFrame = QFrame(self.scanPage)
        self.scanPageFrame.setObjectName(u"scanPageFrame")
        self.scanPageFrame.setFrameShape(QFrame.Shape.Box)
        self.scanPageFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout_5 = QGridLayout(self.scanPageFrame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.scanPageLabel = QLabel(self.scanPageFrame)
        self.scanPageLabel.setObjectName(u"scanPageLabel")
        font = QFont()
        font.setPointSize(24)
        self.scanPageLabel.setFont(font)
        self.scanPageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.scanPageLabel, 1, 1, 1, 1)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.verticalSpacer_20, 0, 1, 1, 1)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_30, 1, 0, 1, 1)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_31, 1, 2, 1, 1)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.verticalSpacer_21, 2, 1, 1, 1)


        self.verticalLayout_8.addWidget(self.scanPageFrame)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_22)

        self.iconFrame = QFrame(self.scanPage)
        self.iconFrame.setObjectName(u"iconFrame")
        self.iconFrame.setFrameShape(QFrame.Shape.Box)
        self.iconFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout_4 = QGridLayout(self.iconFrame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_29, 4, 2, 1, 1)

        self.tagDetectedLabel = QLabel(self.iconFrame)
        self.tagDetectedLabel.setObjectName(u"tagDetectedLabel")
        font1 = QFont()
        font1.setPointSize(15)
        self.tagDetectedLabel.setFont(font1)
        self.tagDetectedLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.tagDetectedLabel, 8, 1, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_18, 2, 2, 1, 1)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_25, 8, 2, 1, 1)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_27, 9, 0, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_17, 2, 0, 1, 1)

        self.rfidPhotoLabel = QLabel(self.iconFrame)
        self.rfidPhotoLabel.setObjectName(u"rfidPhotoLabel")
        self.rfidPhotoLabel.setPixmap(QPixmap(u":/newPrefix/download.png"))

        self.gridLayout_4.addWidget(self.rfidPhotoLabel, 3, 1, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_24, 8, 0, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_19, 6, 0, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_26, 9, 2, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_20, 6, 2, 1, 1)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_28, 4, 0, 1, 1)

        self.scanFailedLabel = QLabel(self.iconFrame)
        self.scanFailedLabel.setObjectName(u"scanFailedLabel")
        self.scanFailedLabel.setFont(font1)
        self.scanFailedLabel.setScaledContents(False)
        self.scanFailedLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.scanFailedLabel, 9, 1, 1, 1)

        self.waitingForTagLabel = QLabel(self.iconFrame)
        self.waitingForTagLabel.setObjectName(u"waitingForTagLabel")
        self.waitingForTagLabel.setFont(font1)
        self.waitingForTagLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.waitingForTagLabel, 6, 1, 1, 1)

        self.scanTagLabel = QLabel(self.iconFrame)
        self.scanTagLabel.setObjectName(u"scanTagLabel")
        self.scanTagLabel.setFont(font)
        self.scanTagLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.scanTagLabel, 1, 1, 1, 1)


        self.verticalLayout_8.addWidget(self.iconFrame)

        self.menuBtnFrame = QFrame(self.scanPage)
        self.menuBtnFrame.setObjectName(u"menuBtnFrame")
        self.menuBtnFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.menuBtnFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.menuBtnFrame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_33 = QSpacerItem(534, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_33)

        self.scanPageMenuPushButton = QPushButton(self.menuBtnFrame)
        self.scanPageMenuPushButton.setObjectName(u"scanPageMenuPushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scanPageMenuPushButton.sizePolicy().hasHeightForWidth())
        self.scanPageMenuPushButton.setSizePolicy(sizePolicy)
        self.scanPageMenuPushButton.setMinimumSize(QSize(200, 60))
        self.scanPageMenuPushButton.setFont(font)
        self.scanPageMenuPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.scanPageMenuPushButton.setStyleSheet(u"background-color: rgb(65, 65, 65);")

        self.horizontalLayout_11.addWidget(self.scanPageMenuPushButton)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_32)


        self.verticalLayout_8.addWidget(self.menuBtnFrame)

        self.stackedWidget.addWidget(self.scanPage)
        self.menuPage = QWidget()
        self.menuPage.setObjectName(u"menuPage")
        self.verticalLayout_2 = QVBoxLayout(self.menuPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.menuLableFrame = QFrame(self.menuPage)
        self.menuLableFrame.setObjectName(u"menuLableFrame")
        self.menuLableFrame.setFrameShape(QFrame.Shape.Box)
        self.menuLableFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout = QHBoxLayout(self.menuLableFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.menuLableFrame)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(48)
        self.label.setFont(font2)
        self.label.setTextFormat(Qt.TextFormat.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setIndent(-1)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.menuLableFrame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.menuButtonFrame = QFrame(self.menuPage)
        self.menuButtonFrame.setObjectName(u"menuButtonFrame")
        sizePolicy1.setHeightForWidth(self.menuButtonFrame.sizePolicy().hasHeightForWidth())
        self.menuButtonFrame.setSizePolicy(sizePolicy1)
        self.menuButtonFrame.setFont(font)
        self.menuButtonFrame.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.menuButtonFrame.setFrameShape(QFrame.Shape.Box)
        self.menuButtonFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout = QGridLayout(self.menuButtonFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.menuPageScanPushButton = QPushButton(self.menuButtonFrame)
        self.menuPageScanPushButton.setObjectName(u"menuPageScanPushButton")
        self.menuPageScanPushButton.setFont(font)
        self.menuPageScanPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.menuPageScanPushButton.setStyleSheet(u"background-color: rgb(65, 65, 65);")

        self.gridLayout.addWidget(self.menuPageScanPushButton, 8, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_5, 9, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_6, 5, 1, 1, 1)

        self.returnPushButton = QPushButton(self.menuButtonFrame)
        self.returnPushButton.setObjectName(u"returnPushButton")
        sizePolicy1.setHeightForWidth(self.returnPushButton.sizePolicy().hasHeightForWidth())
        self.returnPushButton.setSizePolicy(sizePolicy1)
        self.returnPushButton.setFont(font)
        self.returnPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.returnPushButton.setStyleSheet(u"background-color: rgb(65, 65, 65);")

        self.gridLayout.addWidget(self.returnPushButton, 4, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_7, 3, 1, 1, 1)

        self.historyPushButton = QPushButton(self.menuButtonFrame)
        self.historyPushButton.setObjectName(u"historyPushButton")
        sizePolicy1.setHeightForWidth(self.historyPushButton.sizePolicy().hasHeightForWidth())
        self.historyPushButton.setSizePolicy(sizePolicy1)
        self.historyPushButton.setFont(font)
        self.historyPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.historyPushButton.setStyleSheet(u"background-color: rgb(65, 65, 65);")

        self.gridLayout.addWidget(self.historyPushButton, 6, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 4, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 4, 0, 1, 1)

        self.takePushButton = QPushButton(self.menuButtonFrame)
        self.takePushButton.setObjectName(u"takePushButton")
        sizePolicy1.setHeightForWidth(self.takePushButton.sizePolicy().hasHeightForWidth())
        self.takePushButton.setSizePolicy(sizePolicy1)
        self.takePushButton.setFont(font)
        self.takePushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.takePushButton.setStyleSheet(u"background-color: rgb(65, 65, 65);")

        self.gridLayout.addWidget(self.takePushButton, 2, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 6, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_4, 1, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 6, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 2, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 2, 1, 1)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_23, 7, 1, 1, 1)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_34, 8, 0, 1, 1)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_35, 8, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.menuButtonFrame)

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

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_10, 3, 0, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_11, 3, 2, 1, 1)

        self.takeProductcCmboBox = QComboBox(self.takeProductFrame)
        self.takeProductcCmboBox.setObjectName(u"takeProductcCmboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.takeProductcCmboBox.sizePolicy().hasHeightForWidth())
        self.takeProductcCmboBox.setSizePolicy(sizePolicy2)
        self.takeProductcCmboBox.setMinimumSize(QSize(0, 50))
        font3 = QFont()
        font3.setPointSize(18)
        self.takeProductcCmboBox.setFont(font3)
        self.takeProductcCmboBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.takeProductcCmboBox.setStyleSheet(u"background-color: rgb(65, 65, 65);")

        self.gridLayout_2.addWidget(self.takeProductcCmboBox, 3, 1, 1, 1)

        self.takeProductLabel = QLabel(self.takeProductFrame)
        self.takeProductLabel.setObjectName(u"takeProductLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.takeProductLabel.sizePolicy().hasHeightForWidth())
        self.takeProductLabel.setSizePolicy(sizePolicy3)
        self.takeProductLabel.setFont(font)
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
        sizePolicy.setHeightForWidth(self.takeBackPushButton.sizePolicy().hasHeightForWidth())
        self.takeBackPushButton.setSizePolicy(sizePolicy)
        self.takeBackPushButton.setMinimumSize(QSize(200, 60))
        self.takeBackPushButton.setFont(font)
        self.takeBackPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.takeBackPushButton.setStyleSheet(u"background-color: rgb(65, 65, 65);")

        self.horizontalLayout_2.addWidget(self.takeBackPushButton)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_12)

        self.takeConfirmPushButton = QPushButton(self.takeProductBtnFrame)
        self.takeConfirmPushButton.setObjectName(u"takeConfirmPushButton")
        sizePolicy.setHeightForWidth(self.takeConfirmPushButton.sizePolicy().hasHeightForWidth())
        self.takeConfirmPushButton.setSizePolicy(sizePolicy)
        self.takeConfirmPushButton.setMinimumSize(QSize(200, 60))
        self.takeConfirmPushButton.setFont(font)
        self.takeConfirmPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.takeConfirmPushButton.setStyleSheet(u"background-color: rgb(65, 65, 65);")

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

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_15, 3, 0, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_16, 3, 2, 1, 1)

        self.returnProductcCmboBox = QComboBox(self.returnProductFrame)
        self.returnProductcCmboBox.setObjectName(u"returnProductcCmboBox")
        sizePolicy2.setHeightForWidth(self.returnProductcCmboBox.sizePolicy().hasHeightForWidth())
        self.returnProductcCmboBox.setSizePolicy(sizePolicy2)
        self.returnProductcCmboBox.setMinimumSize(QSize(0, 50))
        self.returnProductcCmboBox.setFont(font3)
        self.returnProductcCmboBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.returnProductcCmboBox.setStyleSheet(u"background-color: rgb(65, 65, 65);")

        self.gridLayout_3.addWidget(self.returnProductcCmboBox, 3, 1, 1, 1)

        self.returnProductLabel = QLabel(self.returnProductFrame)
        self.returnProductLabel.setObjectName(u"returnProductLabel")
        sizePolicy3.setHeightForWidth(self.returnProductLabel.sizePolicy().hasHeightForWidth())
        self.returnProductLabel.setSizePolicy(sizePolicy3)
        self.returnProductLabel.setFont(font)
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
        sizePolicy.setHeightForWidth(self.returnBackPushButton.sizePolicy().hasHeightForWidth())
        self.returnBackPushButton.setSizePolicy(sizePolicy)
        self.returnBackPushButton.setMinimumSize(QSize(200, 60))
        self.returnBackPushButton.setFont(font)
        self.returnBackPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.returnBackPushButton.setStyleSheet(u"background-color: rgb(65, 65, 65);")

        self.horizontalLayout_3.addWidget(self.returnBackPushButton)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_14)

        self.returnConfirmPushButton = QPushButton(self.returnProductBtnFrame)
        self.returnConfirmPushButton.setObjectName(u"returnConfirmPushButton")
        sizePolicy.setHeightForWidth(self.returnConfirmPushButton.sizePolicy().hasHeightForWidth())
        self.returnConfirmPushButton.setSizePolicy(sizePolicy)
        self.returnConfirmPushButton.setMinimumSize(QSize(200, 60))
        self.returnConfirmPushButton.setFont(font)
        self.returnConfirmPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.returnConfirmPushButton.setStyleSheet(u"background-color: rgb(65, 65, 65);")

        self.horizontalLayout_3.addWidget(self.returnConfirmPushButton)


        self.verticalLayout_4.addWidget(self.returnProductBtnFrame)

        self.stackedWidget.addWidget(self.returnPage)
        self.historyPage = QWidget()
        self.historyPage.setObjectName(u"historyPage")
        self.verticalLayout_6 = QVBoxLayout(self.historyPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.historyPageFrame = QFrame(self.historyPage)
        self.historyPageFrame.setObjectName(u"historyPageFrame")
        self.historyPageFrame.setFrameShape(QFrame.Shape.Box)
        self.historyPageFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_7 = QVBoxLayout(self.historyPageFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_7.addItem(self.verticalSpacer_19)

        self.historyPageLabel = QLabel(self.historyPageFrame)
        self.historyPageLabel.setObjectName(u"historyPageLabel")
        sizePolicy3.setHeightForWidth(self.historyPageLabel.sizePolicy().hasHeightForWidth())
        self.historyPageLabel.setSizePolicy(sizePolicy3)
        self.historyPageLabel.setFont(font)
        self.historyPageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.historyPageLabel)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_7.addItem(self.verticalSpacer_18)


        self.verticalLayout_6.addWidget(self.historyPageFrame)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_6.addItem(self.verticalSpacer_17)

        self.historyFilterFrame = QFrame(self.historyPage)
        self.historyFilterFrame.setObjectName(u"historyFilterFrame")
        self.historyFilterFrame.setFrameShape(QFrame.Shape.Box)
        self.historyFilterFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_8 = QHBoxLayout(self.historyFilterFrame)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.historyStartDateFrame = QFrame(self.historyFilterFrame)
        self.historyStartDateFrame.setObjectName(u"historyStartDateFrame")
        self.historyStartDateFrame.setFrameShape(QFrame.Shape.Box)
        self.historyStartDateFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.historyStartDateFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.historySartDateLabel = QLabel(self.historyStartDateFrame)
        self.historySartDateLabel.setObjectName(u"historySartDateLabel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.historySartDateLabel.sizePolicy().hasHeightForWidth())
        self.historySartDateLabel.setSizePolicy(sizePolicy4)
        font4 = QFont()
        font4.setPointSize(16)
        self.historySartDateLabel.setFont(font4)
        self.historySartDateLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.historySartDateLabel)

        self.historyStartDateEdit = QDateEdit(self.historyStartDateFrame)
        self.historyStartDateEdit.setObjectName(u"historyStartDateEdit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.historyStartDateEdit.sizePolicy().hasHeightForWidth())
        self.historyStartDateEdit.setSizePolicy(sizePolicy5)
        self.historyStartDateEdit.setMinimumSize(QSize(0, 30))
        self.historyStartDateEdit.setFont(font3)
        self.historyStartDateEdit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.historyStartDateEdit.setStyleSheet(u"background-color: rgb(65, 65, 65);")
        self.historyStartDateEdit.setCalendarPopup(True)

        self.horizontalLayout_4.addWidget(self.historyStartDateEdit)


        self.horizontalLayout_8.addWidget(self.historyStartDateFrame)

        self.historyEndDateFrame = QFrame(self.historyFilterFrame)
        self.historyEndDateFrame.setObjectName(u"historyEndDateFrame")
        self.historyEndDateFrame.setFrameShape(QFrame.Shape.Box)
        self.historyEndDateFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.historyEndDateFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.historyEndDateLabel = QLabel(self.historyEndDateFrame)
        self.historyEndDateLabel.setObjectName(u"historyEndDateLabel")
        sizePolicy4.setHeightForWidth(self.historyEndDateLabel.sizePolicy().hasHeightForWidth())
        self.historyEndDateLabel.setSizePolicy(sizePolicy4)
        self.historyEndDateLabel.setFont(font4)
        self.historyEndDateLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.historyEndDateLabel)

        self.historyEndDateEdit = QDateEdit(self.historyEndDateFrame)
        self.historyEndDateEdit.setObjectName(u"historyEndDateEdit")
        self.historyEndDateEdit.setMinimumSize(QSize(0, 30))
        self.historyEndDateEdit.setFont(font3)
        self.historyEndDateEdit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.historyEndDateEdit.setStyleSheet(u"background-color: rgb(65, 65, 65);")
        self.historyEndDateEdit.setCalendarPopup(True)

        self.horizontalLayout_5.addWidget(self.historyEndDateEdit)


        self.horizontalLayout_8.addWidget(self.historyEndDateFrame)

        self.historyUserFrame = QFrame(self.historyFilterFrame)
        self.historyUserFrame.setObjectName(u"historyUserFrame")
        self.historyUserFrame.setFrameShape(QFrame.Shape.Box)
        self.historyUserFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.historyUserFrame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.historyUserLabel = QLabel(self.historyUserFrame)
        self.historyUserLabel.setObjectName(u"historyUserLabel")
        sizePolicy4.setHeightForWidth(self.historyUserLabel.sizePolicy().hasHeightForWidth())
        self.historyUserLabel.setSizePolicy(sizePolicy4)
        self.historyUserLabel.setFont(font4)
        self.historyUserLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.historyUserLabel)

        self.historyUserComboBox = QComboBox(self.historyUserFrame)
        self.historyUserComboBox.setObjectName(u"historyUserComboBox")
        self.historyUserComboBox.setMinimumSize(QSize(0, 0))
        self.historyUserComboBox.setFont(font4)
        self.historyUserComboBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.historyUserComboBox.setStyleSheet(u"background-color: rgb(65, 65, 65);")

        self.horizontalLayout_6.addWidget(self.historyUserComboBox)


        self.horizontalLayout_8.addWidget(self.historyUserFrame)

        self.historyToolFrame = QFrame(self.historyFilterFrame)
        self.historyToolFrame.setObjectName(u"historyToolFrame")
        self.historyToolFrame.setFrameShape(QFrame.Shape.Box)
        self.historyToolFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.historyToolFrame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.historyToolLable = QLabel(self.historyToolFrame)
        self.historyToolLable.setObjectName(u"historyToolLable")
        sizePolicy4.setHeightForWidth(self.historyToolLable.sizePolicy().hasHeightForWidth())
        self.historyToolLable.setSizePolicy(sizePolicy4)
        self.historyToolLable.setFont(font4)
        self.historyToolLable.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.historyToolLable)

        self.historyToolComboBox = QComboBox(self.historyToolFrame)
        self.historyToolComboBox.setObjectName(u"historyToolComboBox")
        self.historyToolComboBox.setFont(font4)
        self.historyToolComboBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.historyToolComboBox.setStyleSheet(u"background-color: rgb(65, 65, 65);")

        self.horizontalLayout_7.addWidget(self.historyToolComboBox)


        self.horizontalLayout_8.addWidget(self.historyToolFrame)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_21)

        self.historySearchPushButton = QPushButton(self.historyFilterFrame)
        self.historySearchPushButton.setObjectName(u"historySearchPushButton")
        sizePolicy4.setHeightForWidth(self.historySearchPushButton.sizePolicy().hasHeightForWidth())
        self.historySearchPushButton.setSizePolicy(sizePolicy4)
        self.historySearchPushButton.setMinimumSize(QSize(100, 30))
        self.historySearchPushButton.setFont(font)
        self.historySearchPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.historySearchPushButton.setStyleSheet(u"background-color: rgb(65, 65, 65);")

        self.horizontalLayout_8.addWidget(self.historySearchPushButton)


        self.verticalLayout_6.addWidget(self.historyFilterFrame)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_6.addItem(self.verticalSpacer_16)

        self.historyTableFrame = QFrame(self.historyPage)
        self.historyTableFrame.setObjectName(u"historyTableFrame")
        self.historyTableFrame.setFrameShape(QFrame.Shape.Box)
        self.historyTableFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_9 = QHBoxLayout(self.historyTableFrame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.historyTableWidget = QTableWidget(self.historyTableFrame)
        if (self.historyTableWidget.columnCount() < 5):
            self.historyTableWidget.setColumnCount(5)
        font5 = QFont()
        font5.setPointSize(12)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font5);
        self.historyTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font5);
        self.historyTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font5);
        self.historyTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font5);
        self.historyTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font5);
        self.historyTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.historyTableWidget.setObjectName(u"historyTableWidget")
        self.historyTableWidget.setFont(font5)
        self.historyTableWidget.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.historyTableWidget.setAutoFillBackground(False)
        self.historyTableWidget.setStyleSheet(u"background-color: rgb(65, 65, 65);")
        self.historyTableWidget.setFrameShape(QFrame.Shape.Box)
        self.historyTableWidget.setFrameShadow(QFrame.Shadow.Plain)
        self.historyTableWidget.setAlternatingRowColors(True)
        self.historyTableWidget.setTextElideMode(Qt.TextElideMode.ElideRight)
        self.historyTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.historyTableWidget.horizontalHeader().setStretchLastSection(True)
        self.historyTableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.historyTableWidget.verticalHeader().setMinimumSectionSize(24)
        self.historyTableWidget.verticalHeader().setDefaultSectionSize(30)
        self.historyTableWidget.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_9.addWidget(self.historyTableWidget)


        self.verticalLayout_6.addWidget(self.historyTableFrame)

        self.historyBtnFrame = QFrame(self.historyPage)
        self.historyBtnFrame.setObjectName(u"historyBtnFrame")
        self.historyBtnFrame.setFrameShape(QFrame.Shape.Box)
        self.historyBtnFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_10 = QHBoxLayout(self.historyBtnFrame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_22 = QSpacerItem(1117, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_22)

        self.historyBackPushButton = QPushButton(self.historyBtnFrame)
        self.historyBackPushButton.setObjectName(u"historyBackPushButton")
        sizePolicy.setHeightForWidth(self.historyBackPushButton.sizePolicy().hasHeightForWidth())
        self.historyBackPushButton.setSizePolicy(sizePolicy)
        self.historyBackPushButton.setMinimumSize(QSize(200, 60))
        self.historyBackPushButton.setFont(font)
        self.historyBackPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.historyBackPushButton.setStyleSheet(u"background-color: rgb(65, 65, 65);")

        self.horizontalLayout_10.addWidget(self.historyBackPushButton)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_23)

        self.historyConfirmPushButton = QPushButton(self.historyBtnFrame)
        self.historyConfirmPushButton.setObjectName(u"historyConfirmPushButton")
        sizePolicy.setHeightForWidth(self.historyConfirmPushButton.sizePolicy().hasHeightForWidth())
        self.historyConfirmPushButton.setSizePolicy(sizePolicy)
        self.historyConfirmPushButton.setMinimumSize(QSize(200, 60))
        self.historyConfirmPushButton.setFont(font)
        self.historyConfirmPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.historyConfirmPushButton.setStyleSheet(u"background-color: rgb(65, 65, 65);")

        self.horizontalLayout_10.addWidget(self.historyConfirmPushButton)


        self.verticalLayout_6.addWidget(self.historyBtnFrame)

        self.stackedWidget.addWidget(self.historyPage)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 848, 33))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.scanPageLabel.setText(QCoreApplication.translate("MainWindow", u"SCAN PAGE", None))
        self.tagDetectedLabel.setText(QCoreApplication.translate("MainWindow", u"Tag detected", None))
        self.rfidPhotoLabel.setText("")
        self.scanFailedLabel.setText(QCoreApplication.translate("MainWindow", u"Scan failed", None))
        self.waitingForTagLabel.setText(QCoreApplication.translate("MainWindow", u"Waiting for tag...", None))
        self.scanTagLabel.setText(QCoreApplication.translate("MainWindow", u"SCAN TAG", None))
        self.scanPageMenuPushButton.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"RFID-Locker", None))
        self.menuPageScanPushButton.setText(QCoreApplication.translate("MainWindow", u"SCAN", None))
        self.returnPushButton.setText(QCoreApplication.translate("MainWindow", u"RETURN", None))
        self.historyPushButton.setText(QCoreApplication.translate("MainWindow", u"HISTORY", None))
        self.takePushButton.setText(QCoreApplication.translate("MainWindow", u"TAKE", None))
        self.takeProductLabel.setText(QCoreApplication.translate("MainWindow", u"SELECT PRODUCT TO TAKE", None))
        self.takeBackPushButton.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.takeConfirmPushButton.setText(QCoreApplication.translate("MainWindow", u"CONFIRM", None))
        self.returnProductLabel.setText(QCoreApplication.translate("MainWindow", u"SELECT PRODUCT TO RETURN", None))
        self.returnBackPushButton.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.returnConfirmPushButton.setText(QCoreApplication.translate("MainWindow", u"CONFIRM", None))
        self.historyPageLabel.setText(QCoreApplication.translate("MainWindow", u"HISTORY PAGE", None))
        self.historySartDateLabel.setText(QCoreApplication.translate("MainWindow", u"Start date", None))
        self.historyEndDateLabel.setText(QCoreApplication.translate("MainWindow", u"End date", None))
        self.historyUserLabel.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.historyToolLable.setText(QCoreApplication.translate("MainWindow", u"Tool", None))
        self.historySearchPushButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem = self.historyTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"User", None));
        ___qtablewidgetitem1 = self.historyTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Tool", None));
        ___qtablewidgetitem2 = self.historyTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Tool description", None));
        ___qtablewidgetitem3 = self.historyTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Start date", None));
        ___qtablewidgetitem4 = self.historyTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"End date", None));
        self.historyBackPushButton.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.historyConfirmPushButton.setText(QCoreApplication.translate("MainWindow", u"CONFIRM", None))
    # retranslateUi

