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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1619, 1179)
        MainWindow.setStyleSheet(u"")
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


        self.verticalLayout_2.addWidget(self.menuLableFrame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.menuButtonFrame = QFrame(self.menuPage)
        self.menuButtonFrame.setObjectName(u"menuButtonFrame")
        sizePolicy.setHeightForWidth(self.menuButtonFrame.sizePolicy().hasHeightForWidth())
        self.menuButtonFrame.setSizePolicy(sizePolicy)
        self.menuButtonFrame.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.menuButtonFrame.setFrameShape(QFrame.Shape.Box)
        self.menuButtonFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout = QGridLayout(self.menuButtonFrame)
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

        self.historyPushButton = QPushButton(self.menuButtonFrame)
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

        self.returnPushButton = QPushButton(self.menuButtonFrame)
        self.returnPushButton.setObjectName(u"returnPushButton")
        sizePolicy.setHeightForWidth(self.returnPushButton.sizePolicy().hasHeightForWidth())
        self.returnPushButton.setSizePolicy(sizePolicy)
        self.returnPushButton.setFont(font1)
        self.returnPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.returnPushButton.setStyleSheet(u"background-color: rgb(65, 65, 65);")

        self.gridLayout.addWidget(self.returnPushButton, 4, 1, 1, 1)

        self.takePushButton = QPushButton(self.menuButtonFrame)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.takeProductcCmboBox.sizePolicy().hasHeightForWidth())
        self.takeProductcCmboBox.setSizePolicy(sizePolicy1)
        self.takeProductcCmboBox.setMinimumSize(QSize(0, 50))
        self.takeProductcCmboBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.takeProductcCmboBox.setStyleSheet(u"background-color: rgb(65, 65, 65);")

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
        self.takeBackPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.takeBackPushButton.setStyleSheet(u"background-color: rgb(65, 65, 65);")

        self.horizontalLayout_2.addWidget(self.takeBackPushButton)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_12)

        self.takeConfirmPushButton = QPushButton(self.takeProductBtnFrame)
        self.takeConfirmPushButton.setObjectName(u"takeConfirmPushButton")
        sizePolicy3.setHeightForWidth(self.takeConfirmPushButton.sizePolicy().hasHeightForWidth())
        self.takeConfirmPushButton.setSizePolicy(sizePolicy3)
        self.takeConfirmPushButton.setMinimumSize(QSize(200, 60))
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
        sizePolicy1.setHeightForWidth(self.returnProductcCmboBox.sizePolicy().hasHeightForWidth())
        self.returnProductcCmboBox.setSizePolicy(sizePolicy1)
        self.returnProductcCmboBox.setMinimumSize(QSize(0, 50))
        self.returnProductcCmboBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.returnProductcCmboBox.setStyleSheet(u"background-color: rgb(65, 65, 65);")

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
        self.returnBackPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.returnBackPushButton.setStyleSheet(u"background-color: rgb(65, 65, 65);")

        self.horizontalLayout_3.addWidget(self.returnBackPushButton)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_14)

        self.returnConfirmPushButton = QPushButton(self.returnProductBtnFrame)
        self.returnConfirmPushButton.setObjectName(u"returnConfirmPushButton")
        sizePolicy3.setHeightForWidth(self.returnConfirmPushButton.sizePolicy().hasHeightForWidth())
        self.returnConfirmPushButton.setSizePolicy(sizePolicy3)
        self.returnConfirmPushButton.setMinimumSize(QSize(200, 60))
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

        self.historyPageistoryLabel_2 = QLabel(self.historyPageFrame)
        self.historyPageistoryLabel_2.setObjectName(u"historyPageistoryLabel_2")
        sizePolicy2.setHeightForWidth(self.historyPageistoryLabel_2.sizePolicy().hasHeightForWidth())
        self.historyPageistoryLabel_2.setSizePolicy(sizePolicy2)
        self.historyPageistoryLabel_2.setFont(font2)
        self.historyPageistoryLabel_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.historyPageistoryLabel_2)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_7.addItem(self.verticalSpacer_18)


        self.verticalLayout_6.addWidget(self.historyPageFrame)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_6.addItem(self.verticalSpacer_17)

        self.frame_6 = QFrame(self.historyPage)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.Box)
        self.frame_6.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame_6)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.Box)
        self.frame_2.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)
        font3 = QFont()
        font3.setPointSize(12)
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_17)

        self.dateEdit = QDateEdit(self.frame_2)
        self.dateEdit.setObjectName(u"dateEdit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy5)
        self.dateEdit.setMinimumSize(QSize(0, 30))
        self.dateEdit.setFont(font3)
        self.dateEdit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dateEdit.setStyleSheet(u"background-color: rgb(65, 65, 65);")
        self.dateEdit.setCalendarPopup(True)

        self.horizontalLayout_4.addWidget(self.dateEdit)


        self.horizontalLayout_8.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame_6)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.Box)
        self.frame_3.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_18)

        self.dateEdit_2 = QDateEdit(self.frame_3)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setMinimumSize(QSize(0, 30))
        self.dateEdit_2.setFont(font3)
        self.dateEdit_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dateEdit_2.setStyleSheet(u"background-color: rgb(65, 65, 65);")
        self.dateEdit_2.setCalendarPopup(True)

        self.horizontalLayout_5.addWidget(self.dateEdit_2)


        self.horizontalLayout_8.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_6)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.Box)
        self.frame_4.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_19)

        self.comboBox_4 = QComboBox(self.frame_4)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setFont(font3)
        self.comboBox_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBox_4.setStyleSheet(u"background-color: rgb(65, 65, 65);")

        self.horizontalLayout_6.addWidget(self.comboBox_4)


        self.horizontalLayout_8.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.Box)
        self.frame_5.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)
        self.label_5.setFont(font3)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_20)

        self.comboBox_5 = QComboBox(self.frame_5)
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setFont(font3)
        self.comboBox_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBox_5.setStyleSheet(u"background-color: rgb(65, 65, 65);")

        self.horizontalLayout_7.addWidget(self.comboBox_5)


        self.horizontalLayout_8.addWidget(self.frame_5)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_21)

        self.historySeachPushButton = QPushButton(self.frame_6)
        self.historySeachPushButton.setObjectName(u"historySeachPushButton")
        sizePolicy4.setHeightForWidth(self.historySeachPushButton.sizePolicy().hasHeightForWidth())
        self.historySeachPushButton.setSizePolicy(sizePolicy4)
        self.historySeachPushButton.setMinimumSize(QSize(100, 30))
        self.historySeachPushButton.setStyleSheet(u"background-color: rgb(65, 65, 65);")

        self.horizontalLayout_8.addWidget(self.historySeachPushButton)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_6.addItem(self.verticalSpacer_16)

        self.frame_7 = QFrame(self.historyPage)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.Box)
        self.frame_7.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.frame_7)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFrameShape(QFrame.Shape.Box)
        self.tableWidget.setFrameShadow(QFrame.Shadow.Plain)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_9.addWidget(self.tableWidget)


        self.verticalLayout_6.addWidget(self.frame_7)

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
        sizePolicy3.setHeightForWidth(self.historyBackPushButton.sizePolicy().hasHeightForWidth())
        self.historyBackPushButton.setSizePolicy(sizePolicy3)
        self.historyBackPushButton.setMinimumSize(QSize(200, 60))
        self.historyBackPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.historyBackPushButton.setStyleSheet(u"background-color: rgb(65, 65, 65);")

        self.horizontalLayout_10.addWidget(self.historyBackPushButton)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_23)

        self.historyConfirmPushButton = QPushButton(self.historyBtnFrame)
        self.historyConfirmPushButton.setObjectName(u"historyConfirmPushButton")
        sizePolicy3.setHeightForWidth(self.historyConfirmPushButton.sizePolicy().hasHeightForWidth())
        self.historyConfirmPushButton.setSizePolicy(sizePolicy3)
        self.historyConfirmPushButton.setMinimumSize(QSize(200, 60))
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
        self.menubar.setGeometry(QRect(0, 0, 1619, 33))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"RFID-Locker", None))
        self.historyPushButton.setText(QCoreApplication.translate("MainWindow", u"HISTORY", None))
        self.returnPushButton.setText(QCoreApplication.translate("MainWindow", u"RETURN", None))
        self.takePushButton.setText(QCoreApplication.translate("MainWindow", u"TAKE", None))
        self.takeProductLabel.setText(QCoreApplication.translate("MainWindow", u"SELECT PRODUCT TO TAKE", None))
        self.takeBackPushButton.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.takeConfirmPushButton.setText(QCoreApplication.translate("MainWindow", u"CONFIRM", None))
        self.returnProductLabel.setText(QCoreApplication.translate("MainWindow", u"SELECT PRODUCT TO RETURN", None))
        self.returnBackPushButton.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.returnConfirmPushButton.setText(QCoreApplication.translate("MainWindow", u"CONFIRM", None))
        self.historyPageistoryLabel_2.setText(QCoreApplication.translate("MainWindow", u"HISTORY PAGE", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Start date", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"End date", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Tool", None))
        self.historySeachPushButton.setText(QCoreApplication.translate("MainWindow", u"Seach", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Start date", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"End date", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"User", None))
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Tool", None))
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Tool description", None))
        self.historyBackPushButton.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.historyConfirmPushButton.setText(QCoreApplication.translate("MainWindow", u"CONFIRM", None))
    # retranslateUi

