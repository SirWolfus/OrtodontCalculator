import sys
import sqlite3
import pickle
import db_module
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QWidget
from add_pat import Ui_widget

class Pat_Window(QWidget):
    def __init__(self):
        super(Pat_Window,self).__init__()
        self.ui = Ui_widget()
        self.ui.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Pat_Window()
    window.show()
    sys.exit(app.exec())