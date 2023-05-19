# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add-pat.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSplitter, QWidget)
# import add-pat-res_rc
import res_rc

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.setWindowModality(Qt.WindowModal)
        widget.setEnabled(True)
        widget.resize(310, 220)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widget.sizePolicy().hasHeightForWidth())
        widget.setSizePolicy(sizePolicy)
        widget.setMinimumSize(QSize(310, 220))
        widget.setMaximumSize(QSize(310, 220))
        icon = QIcon()
        icon.addFile(u":/img/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        widget.setWindowIcon(icon)
        widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_add = QPushButton(widget)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setGeometry(QRect(190, 180, 111, 31))
        self.pushButton_add.setStyleSheet(u"QPushButton  {\n"
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
        self.label_info = QLabel(widget)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setGeometry(QRect(10, 180, 171, 31))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_info.setFont(font)
        self.splitter = QSplitter(widget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(10, 5, 291, 171))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy1)
        self.splitter.setOrientation(Qt.Vertical)
        self.label_title = QLabel(self.splitter)
        self.label_title.setObjectName(u"label_title")
        font1 = QFont()
        font1.setPointSize(16)
        self.label_title.setFont(font1)
        self.label_title.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.label_title)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_surname = QLineEdit(self.layoutWidget)
        self.lineEdit_surname.setObjectName(u"lineEdit_surname")
        font2 = QFont()
        font2.setPointSize(10)
        self.lineEdit_surname.setFont(font2)

        self.gridLayout.addWidget(self.lineEdit_surname, 2, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEdit_name = QLineEdit(self.layoutWidget)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setFont(font2)

        self.gridLayout.addWidget(self.lineEdit_name, 1, 1, 1, 1)

        self.lineEdit_Fam = QLineEdit(self.layoutWidget)
        self.lineEdit_Fam.setObjectName(u"lineEdit_Fam")
        self.lineEdit_Fam.setFont(font2)

        self.gridLayout.addWidget(self.lineEdit_Fam, 0, 1, 1, 1)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout.addWidget(self.label_5)

        self.dateEdit_birthdau = QDateEdit(self.layoutWidget1)
        self.dateEdit_birthdau.setObjectName(u"dateEdit_birthdau")
        self.dateEdit_birthdau.setFont(font2)
        self.dateEdit_birthdau.setMinimumDate(QDate(1900, 9, 14))
        self.dateEdit_birthdau.setCalendarPopup(True)
        self.dateEdit_birthdau.setCurrentSectionIndex(0)

        self.horizontalLayout.addWidget(self.dateEdit_birthdau)

        self.splitter.addWidget(self.layoutWidget1)
        QWidget.setTabOrder(self.lineEdit_Fam, self.lineEdit_name)
        QWidget.setTabOrder(self.lineEdit_name, self.lineEdit_surname)

        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
        self.pushButton_add.setText(QCoreApplication.translate("widget", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_info.setText("")
        self.label_title.setText(QCoreApplication.translate("widget", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
        self.label_2.setText(QCoreApplication.translate("widget", u"\u0418\u043c\u044f", None))
        self.label.setText(QCoreApplication.translate("widget", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("widget", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.lineEdit_name.setText("")
        self.lineEdit_name.setPlaceholderText("")
        self.label_5.setText(QCoreApplication.translate("widget", u"Дата заполнения:", None))
    # retranslateUi

