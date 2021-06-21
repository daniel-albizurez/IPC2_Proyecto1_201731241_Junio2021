from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QButtonGroup, QTableWidgetItem
import sys
import interfaz
import ayuda
import modificar

class Principal(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self, parent = None):
        super(Principal, self).__init__(parent)
        self.setupUi(self)
        """ self.color = "blue"
        self.pieza = 2 """
        """ self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(10)
        
        self.pushButton.clicked.connect(self.agregar) """

class Ayuda(QtWidgets.QDialog, ayuda.Ui_Dialog):
    def __init__(self, parent = None):
        super(Ayuda, self).__init__(parent)
        self.setModal(True)
        self.setupUi(self)

class Modif(QtWidgets.QDialog, modificar.Ui_Dialog):
    def __init__(self, parent = None):
        super(Modif, self).__init__(parent)
        self.setModal(True)
        self.setupUi(self)
        self.buttonG1 = QButtonGroup(self)
        self.buttonG1.addButton(self.azul1,1)
        self.azul1.setChecked(True)
        self.buttonG1.addButton(self.amarillo1,2)
        self.buttonG1.addButton(self.rojo1,3)
        self.buttonG1.addButton(self.verde1,4)
        self.buttonG2 = QButtonGroup(self)
        self.buttonG2.addButton(self.azul2,1)
        self.buttonG2.addButton(self.amarillo2,2)
        self.buttonG2.addButton(self.rojo2,3)
        self.buttonG2.addButton(self.verde2,4)

    """ def agregar(self):     
        x = int(self.spinX.text())
        y = int(self.spinY.text())
        self.tableWidget.setItem(x,y, QTableWidgetItem("Hola"))
        self.tableWidget.item(x,y).setBackground(QtGui.QColor(self.color))
        self.tableWidget.item(x,y).setForeground(QtGui.QColor(self.color))
        self.tableWidget.item(x,y).setFlags(QtCore.Qt.ItemIsEnabled)
        image_path = 'C:/Users/DANIEL/Documents/U/USAC/IPC2 Vaqueras/Prueba/Grafico/piezas/'+str(self.pieza)+'.png' #path to your image file
        image_profile = QtGui.QImage(image_path) #QImage object
        image_profile = image_profile.scaled(513,123, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation) # To scale image for example and keep its Aspect Ration    
        self.label_3.setPixmap(QtGui.QPixmap.fromImage(image_profile))
        #self.label_3.setPixmap(pieza) """