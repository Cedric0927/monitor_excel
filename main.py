import sys

from PySide2.QtCore import QThread, Signal
from PySide2.QtWidgets import QWidget, QApplication

from ui_window import Ui_Form


class CheckExcel(QWidget):
    def __init__(self):
        super(CheckExcel, self).__init__()
        self.__ui = Ui_Form()
        self.__ui.setupUi(self)
        self.my_thread = MyThread()
        self.my_thread.sinOut.connect(self.receive)

    def receive(self, value):
        pass

    def my_signal(self):
        self.__ui.pushButton.click(self.open_excel)
        self.__ui.pushButton_3.click(self.start_refresh)
        self.__ui.pushButton_2.click(self.stop_refresh)

    def open_excel(self):
        self.__ui.label.setText('你选择的文件为{}'.format(''))
        self.my_thread.start()

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


if __name__ == '__main__':
    stop = False
    app = QApplication(sys.argv)
    check = CheckExcel()
    check.showMaximized()
    sys.exit(app.exec_())
