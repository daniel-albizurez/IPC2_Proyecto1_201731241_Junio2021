from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
import sys
import modificar

class App(QtWidgets.QMainWindow, modificar.Ui_MainWindow):
    def __init__(self, parent = None):
        super(App, self).__init__(parent)
        self.setupUi(self)