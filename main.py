import os.path
import sys

from PySide2.QtCore import QThread, Signal
from PySide2.QtWidgets import QWidget, QApplication, QFileDialog, QTableWidgetItem
from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter

from window import Ui_Form


class CheckExcel(QWidget):
    def __init__(self):
        super(CheckExcel, self).__init__()
        self.__ui = Ui_Form()
        self.__ui.setupUi(self)
        self.my_thread = MyThread()
        self.my_thread.sinOut.connect(self.receive)
        self.my_thread.start()
        self.my_signal()
        self.load_excel('')

    def receive(self, value):
        if value[0] == 'rows_heading':
            self.__ui.tableWidget.setHorizontalHeaderLabels(value[1:])
        elif value[0] == 'cols_heading':
            self.__ui.tableWidget.setHorizontalHeaderLabels(value[1:])
        # else
        pass

    def my_signal(self):
        self.__ui.pushButton.clicked.connect(self.open_excel)
        self.__ui.pushButton_3.clicked.connect(self.start_refresh)
        self.__ui.pushButton_2.clicked.connect(self.stop_refresh)

    def open_excel(self):
        file, filetype = QFileDialog.getOpenFileName(self, "Choose file", '', "*.xlsx")
        self.__ui.label.setText('你选择的文件为: {}'.format(os.path.basename(file)))
        self.load_excel(file)
        # self.my_thread.start()

    def load_excel(self, filepath):
        filepath = r'C:\Users\Cedric.Niu\Desktop\1.xlsx'
        wb = load_workbook(filepath, data_only=True)
        ws = wb.active
        rows_heading, cols_heading = [], []
        for each_row in range(4, 14):
            item = ws[f'A{each_row}']
            item_value = item.value if item else ''
            rows_heading.append(item_value)
            print(item_value)
        for each_col in range(3, 13):
            letter = get_column_letter(each_col)
            item = ws[f'{letter}2']
            item_value = item.value if item else ''
            cols_heading.append(item_value)
        self.__ui.tableWidget.setRowCount(len(rows_heading))
        self.__ui.tableWidget.setColumnCount(len(cols_heading))
        self.__ui.tableWidget.setVerticalHeaderLabels(rows_heading)
        self.__ui.tableWidget.setHorizontalHeaderLabels(cols_heading)
        all_value, single_value = [], []
        for each_row in range(4, 14):
            for each_col in range(3, 13):
                letter = get_column_letter(each_col)
                single_value.append(ws[f'{letter}{each_row}'].value)
            single_value = [each for each in single_value if each]
            all_value.append(single_value)
            single_value = []
        for row, each_row in enumerate(all_value):
            for col, each in enumerate(each_row):
                self.__ui.tableWidget.setItem(row, col, QTableWidgetItem())
                self.__ui.tableWidget.item(row, col).setText(str(each))

    def start_refresh(self):
        global stop
        stop = False
        self.my_thread.start()

    @staticmethod
    def stop_refresh():
        global stop
        stop = True


class MyThread(QThread):
    sinOut = Signal(list)

    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):
        pass
        # self.sinOut.emit(['rows_heading'] + rows_heading)


if __name__ == '__main__':
    stop = False
    app = QApplication(sys.argv)
    check = CheckExcel()
    check.showMaximized()
    sys.exit(app.exec_())
