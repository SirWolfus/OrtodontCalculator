import sys
import pyperclip
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from window_ortocalc import Ui_MainWindow
from add_pat_window import Ui_widget
from MethodCalculate import MethodCalculate as mc
from db_connection import Data as conn
from datetime import datetime as dt


class OrtoCalc(QMainWindow):

    def __init__(self):
        super(OrtoCalc, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.w = None  # Хранит количество дополнительно открытых окон
        self.mc = mc()  # Класс Калькулятор методов, нужен ли о н подумать
        self.conn = conn()  # Класс коннектор для SQL

        # Кнопки
        self.ui.calculate_btn.clicked.connect(self.calculate_all)  # Расчитать все
        self.ui.normodent.clicked.connect(self.btn_norm)  # Нормодентия
        self.ui.macrodent.clicked.connect(self.btn_macro)  # Макродентия
        self.ui.microdent.clicked.connect(self.btn_micro)  # Микродентия
        self.ui.clear_btn.clicked.connect(self.btn_clear)  # Очищаем данные
        self.ui.add_pat_btn.clicked.connect(self.db_add)  # Добавляем пациента в базу
        self.ui.del_pat_btn.clicked.connect(self.db_del)  # Удаляем пациента из базы
        self.ui.save_pat_btn.clicked.connect(self.save_data_to_pat)  # Сохраняем данные в пациента
        self.ui.from_pat_btn.clicked.connect(self.load_data_from_pat)  # Заполняем данные из пациента
        self.ui.calculate_btn_3.clicked.connect(self.copy_to_bufer)  # Копируем в буфер

        # Селектор
        self.ui.pat_selector.addItems(sorted(self.conn.add_box_pat()))
        self.ui.pat_selector.setCurrentText(None)

    def set_info_label(self, info):  # заполняем поле инфо
        self.ui.main_info_label.setText(info)

    def message_window(self, title='Внимание', text='Тест'):
        res = QMessageBox.question(self, title, text)
        return res

    def save_data_to_pat(self):

        if self.conn.add_box_pat().get(str(self.ui.pat_selector.currentText()),
                                       False) and self.ui.pat_selector.currentText() != '':
            if self.message_window('Внимание', 'Новые данные будут сохранены для пациента.') == QMessageBox.Yes:
                id = self.conn.add_box_pat()[str(self.ui.pat_selector.currentText())]
                date = dt.date(dt.now()).strftime('%d.%m.%Y')
                info1 = '*'.join([str(i) for i in self.jaw_re()])
                info2 = '*'.join([str(i) for i in self.jaw_index_re()])
                if self.conn.save_patient(id, date, info1, info2):
                    self.ui.pat_selector.clear()
                    self.ui.pat_selector.addItems(self.conn.add_box_pat())
                    self.ui.pat_selector.setCurrentText(f"{self.ui.pat_selector.currentText().split(' :')[0]} : {date}")
                    self.set_info_label('Данные успешно сохранены!')
            else:
                self.set_info_label('Отмена сохранения')
        else:
            self.set_info_label('Выберите пациента!!!')

    def load_data_from_pat(self):
        if self.conn.add_box_pat().get(str(self.ui.pat_selector.currentText()),
                                       False) and self.ui.pat_selector.currentText() != '':
            if self.message_window('Внимание', 'Новые данные будут сохранены для пациента.') == QMessageBox.Yes:
                id = self.conn.add_box_pat()[str(self.ui.pat_selector.currentText())]
                try:
                    info1, info2 = self.conn.return_pat_data(id)
                    self.field_setter(info1, info2)
                    self.set_info_label('Данные загружены!')
                except:
                    self.set_info_label('Ошибка')
            else:
                self.set_info_label('Отмена сохранения')
        else:
            self.set_info_label('Выберите пациента!!!')

    def db_add(self):
        if self.w is None:
            self.new_window = QtWidgets.QDialog()
            self.ui_window = Ui_widget()
            self.ui_window.setupUi(self.new_window)
            self.ui_window.dateEdit_birthdau.setDate(dt.now())
            self.new_window.show()
            self.ui_window.pushButton_add.clicked.connect(self.add_to_base)
        else:
            self.w.close()
            self.w = None

    def db_del(self):
        if self.conn.add_box_pat().get(str(self.ui.pat_selector.currentText()),
                                       False) and self.ui.pat_selector.currentText() != '':
            if self.message_window('Внимание', 'Пациент будет удален из базы.') == QMessageBox.Yes:
                id = self.conn.add_box_pat()[str(self.ui.pat_selector.currentText())]
                try:
                    self.conn.del_pat(id)
                    self.ui.pat_selector.clear()
                    self.ui.pat_selector.addItems(self.conn.add_box_pat())
                    self.ui.pat_selector.setCurrentText(None)
                    self.set_info_label('Пациент удален!')
                except:
                    self.set_info_label('Ошибка')
            else:
                self.set_info_label('Отмена удаления')
        else:
            self.set_info_label('Выберите пациента!!!')

    def add_to_base(self):
        name = f'{self.ui_window.lineEdit_Fam.text()} {self.ui_window.lineEdit_name.text()} ' \
               f'{self.ui_window.lineEdit_surname.text()}'
        date = self.ui_window.dateEdit_birthdau.text()
        info1 = '*'.join([str(i) for i in mc.pat_clear])
        info2 = '*'.join([str(i) for i in mc.ind_pat_clear])
        if self.conn.filter_pat(name, date):
            self.set_info_label('Повтор данных!')
        else:
            self.conn.add_new_patient(name, date, info1, info2)
            self.new_window.close()
            self.ui.pat_selector.clear()
            self.ui.pat_selector.addItems(self.conn.add_box_pat())
            self.ui.pat_selector.setCurrentText(f'{name} : {date}')
            self.set_info_label('Пациент успешно добавлен.')

    def copy_to_bufer(self):
        text = \
            f'''Пациент: {self.ui.pat_selector.currentText()} 
    Метод Пона.
{self.ui.pon_1.text()}
{self.ui.pon_2.text()}
{self.ui.pon_3.text()}
{self.ui.pon_4.text()}
    Метод Тона.
{self.ui.ton_1.text()}
{self.ui.ton_2.text()}
{self.ui.ton_3.text()}
    Метод Болтона.
{self.ui.bolton_Anterior.text()}
{self.ui.bolton_Overall.text()}'''
        pyperclip.copy(text)
        self.set_info_label('Данные скопированы в буфер обмена.')

    def calculate_all(self):  # Расчет всех методов
        self.pon_method()
        self.ton_method()
        self.bolton_method()
        self.set_info_label('Расчет выполнен')

    def jaw_re_field(self) -> list:
        return [self.ui.zub_16, self.ui.zub_15, self.ui.zub_14, self.ui.zub_13,
                self.ui.zub_12, self.ui.zub_11,
                self.ui.zub_21, self.ui.zub_22, self.ui.zub_23, self.ui.zub_24,
                self.ui.zub_25, self.ui.zub_26, self.ui.zub_36, self.ui.zub_35,
                self.ui.zub_34, self.ui.zub_33,
                self.ui.zub_32, self.ui.zub_31,
                self.ui.zub_41, self.ui.zub_42, self.ui.zub_43, self.ui.zub_44,
                self.ui.zub_45, self.ui.zub_46]

    def jaw_index_field(self) -> list:
        return [self.ui.zub_14_24, self.ui.zub_16_26, self.ui.zub_34_44, self.ui.zub_36_46]

    def jaw_re(self) -> list:
        return [i.value() for i in self.jaw_re_field()]

    def jaw_index_re(self) -> list:
        return [i.value() for i in self.jaw_index_field()]

    def pon_method(self):  # методо Пона
        jaw_ton = self.jaw_re()

        def pon_result(n):
            if n > 0:
                return f'расширение(+{round(n, 2)})'
            elif n < 0:
                return f'сужение({round(n, 2)})'
            else:
                return f'норма (0,00)'

        index_14 = round((sum(jaw_ton[4:8]) * 100) / 85, 2)
        index_16 = round((sum(jaw_ton[4:8]) * 100) / 65, 2)
        index_34 = round((sum(jaw_ton[16:20]) * 100) / 85, 2)
        index_36 = round((sum(jaw_ton[16:20]) * 100) / 65, 2)

        index_14_24 = pon_result(self.ui.zub_14_24.value() - index_14)
        index_16_26 = pon_result(self.ui.zub_16_26.value() - index_16)
        index_34_44 = pon_result(self.ui.zub_34_44.value() - index_34)
        index_36_46 = pon_result(self.ui.zub_36_46.value() - index_36)

        self.ui.pon_1.setText(f'Ширина ряда 14 - 24 равна {index_14} мм - {index_14_24}')
        self.ui.pon_2.setText(f'Ширина ряда 16 - 26 равна {index_16} мм - {index_16_26}')
        self.ui.pon_3.setText(f'Ширина ряда 34 - 44 равна {index_34} мм - {index_34_44}')
        self.ui.pon_4.setText(f'Ширина ряда 36 - 46 равна {index_36} мм - {index_36_46}')

    def ton_method(self):
        index_up = sum(self.jaw_re()[4:8])
        index_low = sum(self.jaw_re()[16:20])

        self.ui.ton_1.setText(f'Сумма 4х резцов ВЧ: {index_up} мм')
        self.ui.ton_2.setText(f'Сумма 4х резцов НЧ: {index_low} мм')

        if round(index_low, 2) == 0:
            self.ui.ton_3.setText(f'Все отлично')
        else:
            if round(index_up / index_low, 2) > 1.35:
                self.ui.ton_3.setText(
                    f'Необходима либо сепарация верхних резцов на {round(index_up - (index_low * 1.35), 2)} мм, '
                    f'либо реставрация нижних резцов на {round((index_up / 1.35) - index_low, 2)} мм')
            else:
                self.ui.ton_3.setText(
                    f'Необходима либо реставрация верхних резцов на {round((index_low * 1.35) - index_up, 2)} мм, '
                    f'либо сепарация нижних резцов на {round(index_low - (index_up / 1.35), 2)}')

    def bolton_method(self):  # Методо Болтона
        def bolton_res(n1, n2):
            if n2 != 0 and n1 != 0:
                return f'{round((n1 / n2) * 100, 2)}%'
            else:
                return 'Все ОК'

        self.ui.bolton_Anterior.setText(
            f'Anterior Ratio (n = 77,2%): {bolton_res(sum(self.jaw_re()[15:21]), sum(self.jaw_re()[3:9]))}')
        self.ui.bolton_Overall.setText(
            f'Overall Ratio (n = 91,3%): {bolton_res(sum(self.jaw_re()[12:]), sum(self.jaw_re()[0:12]))}')

    def btn_norm(self):  # нормодентия
        self.field_setter(mc.pat_norm, mc.ind_pat_norm)

    def btn_macro(self):  # макродентия
        self.field_setter(mc.pat_macro, mc.ind_pat_macro)

    def btn_micro(self):  # микродентия
        self.field_setter(mc.pat_micro, mc.ind_pat_micro)

    def btn_clear(self):  # очистка
        self.field_setter(mc.pat_clear, mc.ind_pat_clear)

    def field_setter(self, pat, ind):  # установщик всех полей
        jaw = self.jaw_re_field()
        jaw_ind = self.jaw_index_field()
        pat_ind = ind
        pattern = pat
        for i in range(len(jaw)):
            jaw[i].setValue(pattern[i])

        for i in range(len(ind)):
            jaw_ind[i].setValue(pat_ind[i])

        self.calculate_all()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = OrtoCalc()
    window.show()
    sys.exit(app.exec())
