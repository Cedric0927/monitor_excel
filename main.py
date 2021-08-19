import sys

# from PySide2.QtCore import QObject
from PySide2.QtWidgets import QWidget, QApplication

# from os import exec
from ui_window import Ui_Form


class CheckExcel(QWidget):
    def __init__(self):
        super(CheckExcel, self).__init__()
        self.__ui = Ui_Form()
        self.__ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    check = CheckExcel()
    check.showMaximized()
    sys.exit(app.exec_())
