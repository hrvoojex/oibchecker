#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""OIB check"""

import sys
from PyQt5 import QtWidgets, QtCore
from gui_design import Ui_Form


class oib(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.pushButton.clicked.connect(self.print_result)

    def check_oib(self, oib):
        if len(self.oib_broj) != 11:
            return False

        if not self.oib_broj.isdigit():
            return False

        a = 10
        for i in range(0, 10):
            a = a + int(oib[i:i + 1])
            a = a % 10
            if a == 0:
                a = 10
            a *= 2
            a = a % 11

        kontrolni = 11 - a
        if kontrolni == 10:
            kontrolni = 0
        return kontrolni == int(oib[10:11])

    def print_result(self):
        # Read from lineEdit
        self.oib_broj = self.lineEdit.text()
        # Check if OIB is ok and print the message
        if self.check_oib(self.oib_broj):
            self.label_3.setText("Ispravan!")
        else:
            self.label_3.setText("Neispravan!")

    def keyPressEvent(self, e):
        """Action when return or escape is pressed"""
        if e.key() == QtCore.Qt.Key_Return:
            self.print_result()
        # self.close is MaApp close() which is QWidget's close()
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = oib()
    w.move(400, 400)
    w.setWindowTitle("Provjera ispravnosti OIB-a")
    w.show()
    sys.exit(app.exec_())
