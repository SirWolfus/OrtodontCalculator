# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main-window-ortocalc.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QGraphicsView, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(1500, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1500, 600))
        MainWindow.setMaximumSize(QSize(1500, 600))
        icon = QIcon()
        icon.addFile(u":/img/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"font: 12pt \"Book Antiqua\";\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(1500, 600))
        self.centralwidget.setMaximumSize(QSize(1500, 600))
        self.centralwidget.setStyleSheet(u"")
        self.zub_fram = QFrame(self.centralwidget)
        self.zub_fram.setObjectName(u"zub_fram")
        self.zub_fram.setGeometry(QRect(10, 86, 981, 511))
        self.zub_fram.setStyleSheet(u"background-color: None;")
        self.zub_fram.setFrameShape(QFrame.StyledPanel)
        self.zub_fram.setFrameShadow(QFrame.Raised)
        self.layoutWidget_3 = QWidget(self.zub_fram)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 206, 471, 26))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.zub_36 = QDoubleSpinBox(self.layoutWidget_3)
        self.zub_36.setObjectName(u"zub_36")
        self.zub_36.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));")
        self.zub_36.setSingleStep(0.500000000000000)

        self.horizontalLayout_4.addWidget(self.zub_36)

        self.zub_35 = QDoubleSpinBox(self.layoutWidget_3)
        self.zub_35.setObjectName(u"zub_35")
        self.zub_35.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));")
        self.zub_35.setSingleStep(0.500000000000000)

        self.horizontalLayout_4.addWidget(self.zub_35)

        self.zub_34 = QDoubleSpinBox(self.layoutWidget_3)
        self.zub_34.setObjectName(u"zub_34")
        self.zub_34.setStyleSheet(u" background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));")
        self.zub_34.setSingleStep(0.500000000000000)

        self.horizontalLayout_4.addWidget(self.zub_34)

        self.zub_33 = QDoubleSpinBox(self.layoutWidget_3)
        self.zub_33.setObjectName(u"zub_33")
        self.zub_33.setStyleSheet(u" background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));")
        self.zub_33.setSingleStep(0.500000000000000)

        self.horizontalLayout_4.addWidget(self.zub_33)

        self.zub_32 = QDoubleSpinBox(self.layoutWidget_3)
        self.zub_32.setObjectName(u"zub_32")
        self.zub_32.setStyleSheet(u" background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));")
        self.zub_32.setSingleStep(0.500000000000000)

        self.horizontalLayout_4.addWidget(self.zub_32)

        self.zub_31 = QDoubleSpinBox(self.layoutWidget_3)
        self.zub_31.setObjectName(u"zub_31")
        self.zub_31.setStyleSheet(u" background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));")
        self.zub_31.setSingleStep(0.500000000000000)

        self.horizontalLayout_4.addWidget(self.zub_31)

        self.layoutWidget = QWidget(self.zub_fram)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(500, 30, 471, 26))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.zub_21 = QDoubleSpinBox(self.layoutWidget)
        self.zub_21.setObjectName(u"zub_21")
        self.zub_21.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));")
        self.zub_21.setSingleStep(0.500000000000000)

        self.horizontalLayout_2.addWidget(self.zub_21)

        self.zub_22 = QDoubleSpinBox(self.layoutWidget)
        self.zub_22.setObjectName(u"zub_22")
        self.zub_22.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));")
        self.zub_22.setSingleStep(0.500000000000000)

        self.horizontalLayout_2.addWidget(self.zub_22)

        self.zub_23 = QDoubleSpinBox(self.layoutWidget)
        self.zub_23.setObjectName(u"zub_23")
        self.zub_23.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));")
        self.zub_23.setSingleStep(0.500000000000000)

        self.horizontalLayout_2.addWidget(self.zub_23)

        self.zub_24 = QDoubleSpinBox(self.layoutWidget)
        self.zub_24.setObjectName(u"zub_24")
        self.zub_24.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));")
        self.zub_24.setSingleStep(0.500000000000000)

        self.horizontalLayout_2.addWidget(self.zub_24)

        self.zub_25 = QDoubleSpinBox(self.layoutWidget)
        self.zub_25.setObjectName(u"zub_25")
        self.zub_25.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));")
        self.zub_25.setSingleStep(0.500000000000000)

        self.horizontalLayout_2.addWidget(self.zub_25)

        self.zub_26 = QDoubleSpinBox(self.layoutWidget)
        self.zub_26.setObjectName(u"zub_26")
        self.zub_26.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));")
        self.zub_26.setSingleStep(0.500000000000000)

        self.horizontalLayout_2.addWidget(self.zub_26)

        self.layoutWidget_2 = QWidget(self.zub_fram)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(500, 206, 471, 26))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.zub_41 = QDoubleSpinBox(self.layoutWidget_2)
        self.zub_41.setObjectName(u"zub_41")
        self.zub_41.setStyleSheet(u" background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));")
        self.zub_41.setSingleStep(0.500000000000000)

        self.horizontalLayout_3.addWidget(self.zub_41)

        self.zub_42 = QDoubleSpinBox(self.layoutWidget_2)
        self.zub_42.setObjectName(u"zub_42")
        self.zub_42.setStyleSheet(u" background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));")
        self.zub_42.setSingleStep(0.500000000000000)

        self.horizontalLayout_3.addWidget(self.zub_42)

        self.zub_43 = QDoubleSpinBox(self.layoutWidget_2)
        self.zub_43.setObjectName(u"zub_43")
        self.zub_43.setStyleSheet(u" background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));")
        self.zub_43.setSingleStep(0.500000000000000)

        self.horizontalLayout_3.addWidget(self.zub_43)

        self.zub_44 = QDoubleSpinBox(self.layoutWidget_2)
        self.zub_44.setObjectName(u"zub_44")
        self.zub_44.setStyleSheet(u" background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));")
        self.zub_44.setSingleStep(0.500000000000000)

        self.horizontalLayout_3.addWidget(self.zub_44)

        self.zub_45 = QDoubleSpinBox(self.layoutWidget_2)
        self.zub_45.setObjectName(u"zub_45")
        self.zub_45.setStyleSheet(u" background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));")
        self.zub_45.setSingleStep(0.500000000000000)

        self.horizontalLayout_3.addWidget(self.zub_45)

        self.zub_46 = QDoubleSpinBox(self.layoutWidget_2)
        self.zub_46.setObjectName(u"zub_46")
        self.zub_46.setStyleSheet(u" background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));")
        self.zub_46.setSingleStep(0.500000000000000)

        self.horizontalLayout_3.addWidget(self.zub_46)

        self.layoutWidget1 = QWidget(self.zub_fram)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 30, 471, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.zub_16 = QDoubleSpinBox(self.layoutWidget1)
        self.zub_16.setObjectName(u"zub_16")
        self.zub_16.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));\n"
"")
        self.zub_16.setSingleStep(0.500000000000000)

        self.horizontalLayout.addWidget(self.zub_16)

        self.zub_15 = QDoubleSpinBox(self.layoutWidget1)
        self.zub_15.setObjectName(u"zub_15")
        self.zub_15.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));")
        self.zub_15.setSingleStep(0.500000000000000)

        self.horizontalLayout.addWidget(self.zub_15)

        self.zub_14 = QDoubleSpinBox(self.layoutWidget1)
        self.zub_14.setObjectName(u"zub_14")
        self.zub_14.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));")
        self.zub_14.setSingleStep(0.500000000000000)

        self.horizontalLayout.addWidget(self.zub_14)

        self.zub_13 = QDoubleSpinBox(self.layoutWidget1)
        self.zub_13.setObjectName(u"zub_13")
        self.zub_13.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));")
        self.zub_13.setSingleStep(0.500000000000000)

        self.horizontalLayout.addWidget(self.zub_13)

        self.zub_12 = QDoubleSpinBox(self.layoutWidget1)
        self.zub_12.setObjectName(u"zub_12")
        self.zub_12.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));")
        self.zub_12.setSingleStep(0.500000000000000)

        self.horizontalLayout.addWidget(self.zub_12)

        self.zub_11 = QDoubleSpinBox(self.layoutWidget1)
        self.zub_11.setObjectName(u"zub_11")
        self.zub_11.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));")
        self.zub_11.setSingleStep(0.500000000000000)

        self.horizontalLayout.addWidget(self.zub_11)

        self.zub_14_24 = QDoubleSpinBox(self.zub_fram)
        self.zub_14_24.setObjectName(u"zub_14_24")
        self.zub_14_24.setGeometry(QRect(192, 384, 66, 24))
        self.zub_14_24.setStyleSheet(u" background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));")
        self.zub_14_24.setSingleStep(0.500000000000000)
        self.zub_16_26 = QDoubleSpinBox(self.zub_fram)
        self.zub_16_26.setObjectName(u"zub_16_26")
        self.zub_16_26.setGeometry(QRect(192, 448, 66, 24))
        self.zub_16_26.setStyleSheet(u" background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));")
        self.zub_16_26.setSingleStep(0.500000000000000)
        self.zub_36_46 = QDoubleSpinBox(self.zub_fram)
        self.zub_36_46.setObjectName(u"zub_36_46")
        self.zub_36_46.setGeometry(QRect(670, 441, 66, 24))
        self.zub_36_46.setStyleSheet(u" background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));")
        self.zub_36_46.setSingleStep(0.500000000000000)
        self.zub_34_44 = QDoubleSpinBox(self.zub_fram)
        self.zub_34_44.setObjectName(u"zub_34_44")
        self.zub_34_44.setGeometry(QRect(670, 381, 66, 24))
        self.zub_34_44.setStyleSheet(u" background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));")
        self.zub_34_44.setSingleStep(0.500000000000000)
        self.clear_btn = QPushButton(self.zub_fram)
        self.clear_btn.setObjectName(u"clear_btn")
        self.clear_btn.setGeometry(QRect(850, 480, 120, 28))
        self.clear_btn.setStyleSheet(u"QPushButton  {\n"
"	background-color: rgb(255, 255, 255); \n"
"  font-weight: 600;\n"
"  border-radius: 6px;\n"
"  border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));;\n"
"  border: 2px solid rgb(55, 111, 167);\n"
"}\n"
"\n"
"QPushButton:pressed  {\n"
"  background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0  rgba(162, 216, 255, 255), stop:1  rgba(255, 255, 255, 255));;\n"
"  border: 2px solid rgb(55, 111, 167);\n"
"}")
        self.bcgrnd_img = QGraphicsView(self.centralwidget)
        self.bcgrnd_img.setObjectName(u"bcgrnd_img")
        self.bcgrnd_img.setGeometry(QRect(0, 55, 1000, 540))
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.bcgrnd_img.sizePolicy().hasHeightForWidth())
        self.bcgrnd_img.setSizePolicy(sizePolicy2)
        self.bcgrnd_img.setAcceptDrops(False)
        self.bcgrnd_img.setStyleSheet(u"background-image: url(:/img/img/podlogka.png);")
        self.bcgrnd_img.setFrameShape(QFrame.NoFrame)
        self.bcgrnd_img.setLineWidth(0)
        self.bcgrnd_img.setInteractive(False)
        self.pon_frame = QFrame(self.centralwidget)
        self.pon_frame.setObjectName(u"pon_frame")
        self.pon_frame.setGeometry(QRect(1000, 50, 491, 181))
        self.pon_frame.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"border-radius:10px;")
        self.pon = QVBoxLayout(self.pon_frame)
        self.pon.setObjectName(u"pon")
        self.pon_name = QLabel(self.pon_frame)
        self.pon_name.setObjectName(u"pon_name")
        font = QFont()
        font.setFamilies([u"Book Antiqua"])
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.pon_name.setFont(font)
        self.pon_name.setStyleSheet(u"font-size: 16pt;\n"
"font-weight: bold;")

        self.pon.addWidget(self.pon_name)

        self.pon_1 = QLabel(self.pon_frame)
        self.pon_1.setObjectName(u"pon_1")
        font1 = QFont()
        font1.setFamilies([u"Book Antiqua"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.pon_1.setFont(font1)

        self.pon.addWidget(self.pon_1)

        self.pon_2 = QLabel(self.pon_frame)
        self.pon_2.setObjectName(u"pon_2")
        self.pon_2.setFont(font1)

        self.pon.addWidget(self.pon_2)

        self.pon_3 = QLabel(self.pon_frame)
        self.pon_3.setObjectName(u"pon_3")
        self.pon_3.setFont(font1)

        self.pon.addWidget(self.pon_3)

        self.pon_4 = QLabel(self.pon_frame)
        self.pon_4.setObjectName(u"pon_4")
        self.pon_4.setFont(font1)

        self.pon.addWidget(self.pon_4)

        self.ton_frame = QFrame(self.centralwidget)
        self.ton_frame.setObjectName(u"ton_frame")
        self.ton_frame.setGeometry(QRect(1000, 240, 491, 111))
        self.ton_frame.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"border-radius:10px;")
        self.ton = QGridLayout(self.ton_frame)
        self.ton.setObjectName(u"ton")
        self.ton.setContentsMargins(-1, 5, -1, 5)
        self.ton_name = QLabel(self.ton_frame)
        self.ton_name.setObjectName(u"ton_name")
        font2 = QFont()
        font2.setFamilies([u"Book Antiqua"])
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setItalic(False)
        self.ton_name.setFont(font2)
        self.ton_name.setStyleSheet(u"font-size: 13pt;\n"
"font-weight: bold;")

        self.ton.addWidget(self.ton_name, 0, 0, 1, 1)

        self.ton_1 = QLabel(self.ton_frame)
        self.ton_1.setObjectName(u"ton_1")

        self.ton.addWidget(self.ton_1, 1, 0, 1, 1)

        self.ton_2 = QLabel(self.ton_frame)
        self.ton_2.setObjectName(u"ton_2")
        self.ton_2.setWordWrap(False)

        self.ton.addWidget(self.ton_2, 1, 1, 1, 1)

        self.ton_3 = QLabel(self.ton_frame)
        self.ton_3.setObjectName(u"ton_3")
        self.ton_3.setTextFormat(Qt.AutoText)
        self.ton_3.setScaledContents(False)
        self.ton_3.setWordWrap(True)

        self.ton.addWidget(self.ton_3, 2, 0, 1, 2)

        self.bolton_frame = QFrame(self.centralwidget)
        self.bolton_frame.setObjectName(u"bolton_frame")
        self.bolton_frame.setGeometry(QRect(1000, 360, 491, 74))
        self.bolton_frame.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"border-radius:10px;")
        self.bolton = QVBoxLayout(self.bolton_frame)
        self.bolton.setObjectName(u"bolton")
        self.bolton_name = QLabel(self.bolton_frame)
        self.bolton_name.setObjectName(u"bolton_name")
        self.bolton_name.setStyleSheet(u"font-size: 13pt;\n"
"font-weight: bold;")

        self.bolton.addWidget(self.bolton_name)

        self.bolton_Anterior = QLabel(self.bolton_frame)
        self.bolton_Anterior.setObjectName(u"bolton_Anterior")

        self.bolton.addWidget(self.bolton_Anterior)

        self.bolton_Overall = QLabel(self.bolton_frame)
        self.bolton_Overall.setObjectName(u"bolton_Overall")

        self.bolton.addWidget(self.bolton_Overall)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(14, 10, 1481, 32))
        self.horizontalLayout_11 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pat_label = QLabel(self.layoutWidget2)
        self.pat_label.setObjectName(u"pat_label")
        font3 = QFont()
        font3.setFamilies([u"Book Antiqua"])
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(False)
        self.pat_label.setFont(font3)
        self.pat_label.setStyleSheet(u"font-weight: bold;")

        self.horizontalLayout_9.addWidget(self.pat_label)

        self.pat_selector = QComboBox(self.layoutWidget2)
        self.pat_selector.setObjectName(u"pat_selector")
        self.pat_selector.setMinimumSize(QSize(0, 25))
        self.pat_selector.setStyleSheet(u"border: 1px solid rgb(0, 0, 0);")
        self.pat_selector.setEditable(True)
        self.pat_selector.setInsertPolicy(QComboBox.NoInsert)
        self.pat_selector.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.pat_selector.setModelColumn(0)

        self.horizontalLayout_9.addWidget(self.pat_selector)

        self.horizontalLayout_9.setStretch(1, 90)

        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.add_pat_btn = QPushButton(self.layoutWidget2)
        self.add_pat_btn.setObjectName(u"add_pat_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.add_pat_btn.sizePolicy().hasHeightForWidth())
        self.add_pat_btn.setSizePolicy(sizePolicy3)
        self.add_pat_btn.setMinimumSize(QSize(0, 25))
        self.add_pat_btn.setStyleSheet(u"QPushButton  {\n"
"	background-color: rgb(255, 255, 255); \n"
"  font-weight: 600;\n"
"  border-radius: 6px;\n"
"  border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));;\n"
"  border: 2px solid rgb(55, 111, 167);\n"
"}\n"
"\n"
"QPushButton:pressed  {\n"
"  background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0  rgba(162, 216, 255, 255), stop:1  rgba(255, 255, 255, 255));;\n"
"  border: 2px solid rgb(55, 111, 167);\n"
"}")

        self.horizontalLayout_5.addWidget(self.add_pat_btn)

        self.del_pat_btn = QPushButton(self.layoutWidget2)
        self.del_pat_btn.setObjectName(u"del_pat_btn")
        sizePolicy3.setHeightForWidth(self.del_pat_btn.sizePolicy().hasHeightForWidth())
        self.del_pat_btn.setSizePolicy(sizePolicy3)
        self.del_pat_btn.setMinimumSize(QSize(0, 25))
        self.del_pat_btn.setStyleSheet(u"QPushButton  {\n"
"	background-color: rgb(255, 255, 255); \n"
"  font-weight: 600;\n"
"  border-radius: 6px;\n"
"  border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));;\n"
"  border: 2px solid rgb(55, 111, 167);\n"
"}\n"
"\n"
"QPushButton:pressed  {\n"
"  background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0  rgba(162, 216, 255, 255), stop:1  rgba(255, 255, 255, 255));;\n"
"  border: 2px solid rgb(55, 111, 167);\n"
"}")

        self.horizontalLayout_5.addWidget(self.del_pat_btn)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_10.setStretch(0, 7)
        self.horizontalLayout_10.setStretch(1, 3)

        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.normodent = QPushButton(self.layoutWidget2)
        self.normodent.setObjectName(u"normodent")
        sizePolicy3.setHeightForWidth(self.normodent.sizePolicy().hasHeightForWidth())
        self.normodent.setSizePolicy(sizePolicy3)
        self.normodent.setMinimumSize(QSize(0, 25))
        self.normodent.setStyleSheet(u"QPushButton  {\n"
"	background-color: rgb(255, 255, 255); \n"
"  font-weight: 600;\n"
"  border-radius: 6px;\n"
"  border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));;\n"
"  border: 2px solid rgb(55, 111, 167);\n"
"}\n"
"\n"
"QPushButton:pressed  {\n"
"  background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0  rgba(162, 216, 255, 255), stop:1  rgba(255, 255, 255, 255));;\n"
"  border: 2px solid rgb(55, 111, 167);\n"
"}")

        self.horizontalLayout_6.addWidget(self.normodent)

        self.macrodent = QPushButton(self.layoutWidget2)
        self.macrodent.setObjectName(u"macrodent")
        sizePolicy3.setHeightForWidth(self.macrodent.sizePolicy().hasHeightForWidth())
        self.macrodent.setSizePolicy(sizePolicy3)
        self.macrodent.setMinimumSize(QSize(0, 25))
        self.macrodent.setStyleSheet(u"QPushButton  {\n"
"	background-color: rgb(255, 255, 255); \n"
"  font-weight: 600;\n"
"  border-radius: 6px;\n"
"  border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));;\n"
"  border: 2px solid rgb(55, 111, 167);\n"
"}\n"
"\n"
"QPushButton:pressed  {\n"
"  background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0  rgba(162, 216, 255, 255), stop:1  rgba(255, 255, 255, 255));;\n"
"  border: 2px solid rgb(55, 111, 167);\n"
"}")

        self.horizontalLayout_6.addWidget(self.macrodent)

        self.microdent = QPushButton(self.layoutWidget2)
        self.microdent.setObjectName(u"microdent")
        sizePolicy3.setHeightForWidth(self.microdent.sizePolicy().hasHeightForWidth())
        self.microdent.setSizePolicy(sizePolicy3)
        self.microdent.setMinimumSize(QSize(0, 25))
        self.microdent.setStyleSheet(u"QPushButton  {\n"
"	background-color: rgb(255, 255, 255); \n"
"  font-weight: 600;\n"
"  border-radius: 6px;\n"
"  border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));;\n"
"  border: 2px solid rgb(55, 111, 167);\n"
"}\n"
"\n"
"QPushButton:pressed  {\n"
"  background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0  rgba(162, 216, 255, 255), stop:1  rgba(255, 255, 255, 255));;\n"
"  border: 2px solid rgb(55, 111, 167);\n"
"}")

        self.horizontalLayout_6.addWidget(self.microdent)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_11.setStretch(0, 71)
        self.horizontalLayout_11.setStretch(1, 36)
        self.main_info_label = QLabel(self.centralwidget)
        self.main_info_label.setObjectName(u"main_info_label")
        self.main_info_label.setGeometry(QRect(1000, 560, 491, 31))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(1000, 440, 491, 92))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.from_pat_btn = QPushButton(self.widget)
        self.from_pat_btn.setObjectName(u"from_pat_btn")
        sizePolicy3.setHeightForWidth(self.from_pat_btn.sizePolicy().hasHeightForWidth())
        self.from_pat_btn.setSizePolicy(sizePolicy3)
        self.from_pat_btn.setMinimumSize(QSize(0, 40))
        self.from_pat_btn.setBaseSize(QSize(0, 40))
        self.from_pat_btn.setStyleSheet(u"QPushButton  {\n"
"	background-color: rgb(255, 255, 255); \n"
"  font-weight: 600;\n"
"  border-radius: 6px;\n"
"  border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));;\n"
"  border: 2px solid rgb(55, 111, 167);\n"
"}\n"
"\n"
"QPushButton:pressed  {\n"
"  background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0  rgba(162, 216, 255, 255), stop:1  rgba(255, 255, 255, 255));;\n"
"  border: 2px solid rgb(55, 111, 167);\n"
"}")

        self.horizontalLayout_7.addWidget(self.from_pat_btn)

        self.save_pat_btn = QPushButton(self.widget)
        self.save_pat_btn.setObjectName(u"save_pat_btn")
        sizePolicy3.setHeightForWidth(self.save_pat_btn.sizePolicy().hasHeightForWidth())
        self.save_pat_btn.setSizePolicy(sizePolicy3)
        self.save_pat_btn.setMinimumSize(QSize(0, 40))
        self.save_pat_btn.setStyleSheet(u"QPushButton  {\n"
"	background-color: rgb(255, 255, 255); \n"
"  font-weight: 600;\n"
"  border-radius: 6px;\n"
"  border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));;\n"
"  border: 2px solid rgb(55, 111, 167);\n"
"}\n"
"\n"
"QPushButton:pressed  {\n"
"  background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0  rgba(162, 216, 255, 255), stop:1  rgba(255, 255, 255, 255));;\n"
"  border: 2px solid rgb(55, 111, 167);\n"
"}")

        self.horizontalLayout_7.addWidget(self.save_pat_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.calculate_btn = QPushButton(self.widget)
        self.calculate_btn.setObjectName(u"calculate_btn")
        self.calculate_btn.setMinimumSize(QSize(0, 40))
        self.calculate_btn.setFont(font3)
        self.calculate_btn.setStyleSheet(u"QPushButton  {\n"
"	background-color: rgb(255, 255, 255); \n"
"  font-weight: 600;\n"
"  border-radius: 6px;\n"
"  border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));;\n"
"  border: 2px solid rgb(55, 111, 167);\n"
"}\n"
"\n"
"QPushButton:pressed  {\n"
"  background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0  rgba(162, 216, 255, 255), stop:1  rgba(255, 255, 255, 255));;\n"
"  border: 2px solid rgb(55, 111, 167);\n"
"}")

        self.horizontalLayout_8.addWidget(self.calculate_btn)

        self.calculate_btn_3 = QPushButton(self.widget)
        self.calculate_btn_3.setObjectName(u"calculate_btn_3")
        self.calculate_btn_3.setMinimumSize(QSize(0, 40))
        self.calculate_btn_3.setStyleSheet(u"QPushButton  {\n"
"	background-color: rgb(255, 255, 255); \n"
"  font-weight: 600;\n"
"  border-radius: 6px;\n"
"  border: 1px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(162, 216, 255, 255));;\n"
"  border: 2px solid rgb(55, 111, 167);\n"
"}\n"
"\n"
"QPushButton:pressed  {\n"
"  background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0  rgba(162, 216, 255, 255), stop:1  rgba(255, 255, 255, 255));;\n"
"  border: 2px solid rgb(55, 111, 167);\n"
"}")

        self.horizontalLayout_8.addWidget(self.calculate_btn_3)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        MainWindow.setCentralWidget(self.centralwidget)
        self.layoutWidget2.raise_()
        self.layoutWidget2.raise_()
        self.ton_frame.raise_()
        self.bolton_frame.raise_()
        self.pon_frame.raise_()
        self.bcgrnd_img.raise_()
        self.zub_fram.raise_()
        self.from_pat_btn.raise_()
        self.save_pat_btn.raise_()
        self.main_info_label.raise_()
        QWidget.setTabOrder(self.zub_16, self.zub_15)
        QWidget.setTabOrder(self.zub_15, self.zub_14)
        QWidget.setTabOrder(self.zub_14, self.zub_13)
        QWidget.setTabOrder(self.zub_13, self.zub_12)
        QWidget.setTabOrder(self.zub_12, self.zub_11)
        QWidget.setTabOrder(self.zub_11, self.zub_21)
        QWidget.setTabOrder(self.zub_21, self.zub_22)
        QWidget.setTabOrder(self.zub_22, self.zub_23)
        QWidget.setTabOrder(self.zub_23, self.zub_24)
        QWidget.setTabOrder(self.zub_24, self.zub_25)
        QWidget.setTabOrder(self.zub_25, self.zub_26)
        QWidget.setTabOrder(self.zub_26, self.zub_36)
        QWidget.setTabOrder(self.zub_36, self.zub_35)
        QWidget.setTabOrder(self.zub_35, self.zub_34)
        QWidget.setTabOrder(self.zub_34, self.zub_33)
        QWidget.setTabOrder(self.zub_33, self.zub_32)
        QWidget.setTabOrder(self.zub_32, self.zub_31)
        QWidget.setTabOrder(self.zub_31, self.zub_41)
        QWidget.setTabOrder(self.zub_41, self.zub_42)
        QWidget.setTabOrder(self.zub_42, self.zub_43)
        QWidget.setTabOrder(self.zub_43, self.zub_44)
        QWidget.setTabOrder(self.zub_44, self.zub_45)
        QWidget.setTabOrder(self.zub_45, self.zub_46)
        QWidget.setTabOrder(self.zub_46, self.zub_14_24)
        QWidget.setTabOrder(self.zub_14_24, self.zub_16_26)
        QWidget.setTabOrder(self.zub_16_26, self.zub_34_44)
        QWidget.setTabOrder(self.zub_34_44, self.zub_36_46)
        QWidget.setTabOrder(self.zub_36_46, self.bcgrnd_img)
        QWidget.setTabOrder(self.bcgrnd_img, self.pat_selector)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0440\u0442\u043e\u0434\u043e\u043d\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440 by SirWolf (v2023)", None))
        self.clear_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.pon_name.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u041f\u043e\u043d\u0430", None))
        self.pon_1.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u0438\u043d\u0430 \u0440\u044f\u0434\u0430 14 - 24 - \u0420\u0430\u0441\u0447\u0435\u0442 \u043d\u0435 \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d", None))
        self.pon_2.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u0438\u043d\u0430 \u0440\u044f\u0434\u0430 16 - 26 - \u0420\u0430\u0441\u0447\u0435\u0442 \u043d\u0435 \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d", None))
        self.pon_3.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u0438\u043d\u0430 \u0440\u044f\u0434\u0430 34 - 44 - \u0420\u0430\u0441\u0447\u0435\u0442 \u043d\u0435 \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d", None))
        self.pon_4.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u0438\u043d\u0430 \u0440\u044f\u0434\u0430 36 - 46 - \u0420\u0430\u0441\u0447\u0435\u0442 \u043d\u0435 \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d", None))
        self.ton_name.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u0422\u043e\u043d\u0430", None))
        self.ton_1.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430 4\u0445 \u0440\u0435\u0437\u0446\u043e\u0432 \u0412\u0427: --", None))
        self.ton_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430 4\u0445 \u0440\u0435\u0437\u0446\u043e\u0432 \u041d\u0427: --", None))
        self.ton_3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.bolton_name.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u0411\u043e\u043b\u0442\u043e\u043d\u0430", None))
        self.bolton_Anterior.setText(QCoreApplication.translate("MainWindow", u"Anterior Ratio (n = 77,2%): --", None))
        self.bolton_Overall.setText(QCoreApplication.translate("MainWindow", u"Overall Ratio (n = 91,3%): --", None))
        self.pat_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0446\u0438\u0435\u043d\u0442", None))
        self.add_pat_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.del_pat_btn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.normodent.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u043e\u0434\u0435\u043d\u0442\u0438\u044f", None))
        self.macrodent.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043a\u0440\u043e\u0434\u0435\u043d\u0442\u0438\u044f", None))
        self.microdent.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043a\u0440\u043e\u0434\u0435\u043d\u0442\u0438\u044f", None))
        self.main_info_label.setText("")
        self.from_pat_btn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0438\u0437 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
        self.save_pat_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0443", None))
        self.calculate_btn.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.calculate_btn_3.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u0432 \u0431\u0443\u0444\u0435\u0440 \u043e\u0431\u043c\u0435\u043d\u0430", None))
    # retranslateUi

