import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from window_ortocalc import Ui_MainWindow


class OrtoCalc(QMainWindow):
    def __init__(self):
        super(OrtoCalc, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.pat_clear = [0 for i in range(24)]
        self.ind_pat_clear = [0 for i in range(4)]

        self.pat_norm = [10.61, 6.59, 7.11, 7.71, 6.82, 8.52,
                         8.52, 6.82, 7.71, 7.11, 6.59, 10.61,
                         11.43, 7.12, 6.94, 6.39, 6.21, 5.19,
                         5.19, 6.21, 6.39, 6.94, 7.12, 11.43]
        self.ind_pat_norm = [36, 47, 26, 35]

        self.pat_macro = [10.75, 6.96, 6.69, 8.61, 7.73, 9.71,
                          9.71, 7.73, 8.61, 6.69, 6.96, 10.75,
                          11.18, 7.51, 7.36, 7.39, 6.67, 6.08,
                          6.08, 6.67, 7.39, 7.36, 7.51, 11.18]
        self.ind_pat_macro = [41, 53.6, 30, 39.2]

        self.pat_micro = [9.82, 6.42, 6.58, 8.09, 6.81, 8.39,
                          8.39, 6.81, 8.09, 6.58, 6.42, 9.82,
                          10.39, 6.73, 7.02, 6.71, 6.24, 5.03,
                          5.03, 6.24, 6.71, 7.02, 6.73, 10.39]

        self.ind_pat_micro = [35.7, 46.7, 26.5, 34.6]

        # Поля
        self.ui.pon_1.setText(f'Ширина ряда 14 - 24 - Расчет не проведен')
        self.ui.pon_2.setText(f'Ширина ряда 16 - 26 - Расчет не проведен')
        self.ui.pon_3.setText(f'Ширина ряда 34 - 44 - Расчет не проведен')
        self.ui.pon_4.setText(f'Ширина ряда 36 - 46 - Расчет не проведен')
        self.ui.ton_1.setText(f'Сумма 4х резцов ВЧ: --')
        self.ui.ton_2.setText(f'Сумма 4х резцов НЧ: --')
        self.ui.ton_3.setText(f'Заполните данные')
        self.ui.bolton_Anterior.setText(f'Anterior Ratio (n = 77,2%): --')
        self.ui.bolton_Overall.setText(f'Overall Ratio (n = 91,3%): --')

        # Кнопки
        self.ui.calculate_btn.clicked.connect(self.calculate_all)
        self.ui.normodent.clicked.connect(self.btn_norm)
        self.ui.macrodent.clicked.connect(self.btn_macro)
        self.ui.microdent.clicked.connect(self.btn_micro)
        self.ui.clear_btn.clicked.connect(self.btn_clear)

    def calculate_all(self):  # Расчет всех методов
        self.pon_method()
        self.ton_method()
        self.bolton_method()

    def jaw_re(self) -> list:
        return [self.ui.zub_16.value(), self.ui.zub_15.value(), self.ui.zub_14.value(), self.ui.zub_13.value(),
                self.ui.zub_12.value(), self.ui.zub_11.value(),
                self.ui.zub_21.value(), self.ui.zub_22.value(), self.ui.zub_23.value(), self.ui.zub_24.value(),
                self.ui.zub_25.value(), self.ui.zub_26.value(), self.ui.zub_36.value(), self.ui.zub_35.value(),
                self.ui.zub_34.value(), self.ui.zub_33.value(),
                self.ui.zub_32.value(), self.ui.zub_31.value(),
                self.ui.zub_41.value(), self.ui.zub_42.value(), self.ui.zub_43.value(), self.ui.zub_44.value(),
                self.ui.zub_45.value(), self.ui.zub_46.value()]

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
        self.field_setter(self.pat_norm, self.ind_pat_norm)

    def btn_macro(self):  # макродентия
        self.field_setter(self.pat_macro, self.ind_pat_macro)

    def btn_micro(self):  # микродентия
        self.field_setter(self.pat_micro, self.ind_pat_micro)

    def btn_clear(self):  # очистка
        self.field_setter(self.pat_clear, self.ind_pat_clear)

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
