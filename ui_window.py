# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(742, 527)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
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
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        if (self.tableWidget.rowCount() < 5):
            self.tableWidget.setRowCount(5)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 5, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 6, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 7, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 8, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setItem(0, 9, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setItem(1, 9, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget.setItem(2, 3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget.setItem(2, 4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget.setItem(2, 5, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget.setItem(2, 6, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget.setItem(2, 7, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget.setItem(2, 8, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget.setItem(2, 9, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget.setItem(3, 9, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget.setItem(4, 9, __qtablewidgetitem40)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(125)
        self.tableWidget.verticalHeader().setDefaultSectionSize(55)

        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        font = QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)

        self.gridLayout.addWidget(self.checkBox, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)

        self.gridLayout.addWidget(self.comboBox, 1, 3, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(41)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2)

        self.spinBox = QSpinBox(self.groupBox)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout.addWidget(self.spinBox)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)


        self.retranslateUi(Form)

        self.comboBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5b89\u5168App", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"1", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"2", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"3", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"4", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"5", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"6", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"7", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"8", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"9", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"10", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"\u5b89\u5168\u751f\u4ea7\u5929\u6570", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"\u76ee\u6807\u5929\u6570", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"\u594b\u6597\u5929\u6570", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"\u4e0a\u6b21\u635f\u5de5\u65f6\u95f4", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form", u"\u5e73\u53f0\u7535\u8bdd", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem15 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Form", u"145", None));
        ___qtablewidgetitem16 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Form", u"44427", None));
        ___qtablewidgetitem17 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Form", u"44427", None));
        ___qtablewidgetitem18 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Form", u"44427", None));
        ___qtablewidgetitem19 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Form", u"44427", None));
        ___qtablewidgetitem20 = self.tableWidget.item(0, 5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Form", u"44427", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 6)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Form", u"44427", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 7)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Form", u"44427", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 8)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Form", u"44427", None));
        ___qtablewidgetitem24 = self.tableWidget.item(0, 9)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Form", u"2721", None));
        ___qtablewidgetitem25 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Form", u"200", None));
        ___qtablewidgetitem26 = self.tableWidget.item(1, 9)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Form", u"2800", None));
        ___qtablewidgetitem27 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Form", u"55", None));
        ___qtablewidgetitem28 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Form", u"-44427", None));
        ___qtablewidgetitem29 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("Form", u"-44427", None));
        ___qtablewidgetitem30 = self.tableWidget.item(2, 3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("Form", u"-44427", None));
        ___qtablewidgetitem31 = self.tableWidget.item(2, 4)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("Form", u"-44427", None));
        ___qtablewidgetitem32 = self.tableWidget.item(2, 5)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("Form", u"-44427", None));
        ___qtablewidgetitem33 = self.tableWidget.item(2, 6)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("Form", u"-44427", None));
        ___qtablewidgetitem34 = self.tableWidget.item(2, 7)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("Form", u"-44427", None));
        ___qtablewidgetitem35 = self.tableWidget.item(2, 8)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("Form", u"-44427", None));
        ___qtablewidgetitem36 = self.tableWidget.item(2, 9)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("Form", u"79", None));
        ___qtablewidgetitem37 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("Form", u"2021/3/27", None));
        ___qtablewidgetitem38 = self.tableWidget.item(3, 9)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("Form", u"2014/3/8", None));
        ___qtablewidgetitem39 = self.tableWidget.item(4, 9)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("Form", u"0752-5965911", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u5de5\u5177", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u6570\u636e\u53d8\u5316\u662f\u5426\u53d8\u989c\u8272", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u7ea2\u8272", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u9ec4\u8272", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"\u84dd\u8272", None))

        self.pushButton.setText(QCoreApplication.translate("Form", u"\u9009\u62e9Excel \u6587\u4ef6", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u672a\u9009\u62e9\u6587\u4ef6", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u5237\u65b0", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u505c\u6b62\u5237\u65b0", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u5237\u65b0\u65f6\u95f4", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u79d2", None))
    # retranslateUi

