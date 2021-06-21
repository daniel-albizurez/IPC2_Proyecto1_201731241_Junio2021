from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
import sys
import ayuda

class Ayuda(QtWidgets.QMainWindow, ayuda.Ui_Dialog):
    def __init__(self, parent = None):
        super(Ayuda, self).__init__(parent)
        self.setupUi(self)