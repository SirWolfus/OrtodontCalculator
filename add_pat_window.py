import sys
import sqlite3
import pickle
import db_module
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PySide6.QtCore import QDate
from add_pat import Ui_widget


class Pat_Window(QWidget):
    def __init__(self):
        super(Pat_Window, self).__init__()
        self.ui = Ui_widget()
        self.ui.setupUi(self)
        self.ui.pushButton_add.clicked.connect(self.add_data)

    def add_data(self):
        result = db_module.db_pat_insert(self.ui.lineEdit_Fam.text(), self.ui.lineEdit_name.text(),
                                self.ui.lineEdit_surname.text(),
                                self.ui.dateEdit_birthdau.date().toString('yyyy-MM-dd'))

        self.ui.label_info.setText(result)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Pat_Window()
    window.show()
    sys.exit(app.exec())
