from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
import sys
import ventana
import block

def main():
    app = QApplication(sys.argv)
    form = ventana.App()
    juego = block.Juego(10, 10)
    definirTablero(form, 10,10)

    juego.definirJugador("hola", "blue")
    juego.definirJugador("a", "yellow")
    juego.cambioDeTurno()
    mostrarPieza(juego.piezaActual, form.label_3)

    form.pushButton.clicked.connect(lambda: juego.colocarPieza(
        int(form.spinX.text())-1,
        int(form.spinY.text())-1,
        juego.piezaActual,
        juego.turno,
        form.tableWidget
    ))
    form.pushButton.clicked.connect(lambda: mostrarPieza(
        juego.piezaActual,
        form.label_3
        ))
    #form.pushButton.clicked.connect(juego.tableroMatriz.generarDot)
    form.show()
    app.exec_()

def definirTablero(form,x, y):
    form.spinX.setMaximum(x)
    form.spinY.setMaximum(y)
    form.spinX.setMinimum(1)
    form.spinY.setMinimum(1)
    form.tableWidget.setRowCount(y)
    form.tableWidget.setColumnCount(x)

def mostrarPieza(pieza, label):
    image_path = 'C:/Users/DANIEL/Documents/U/USAC/IPC2 Vaqueras/Prueba/Grafico/piezas/'+str(pieza)+'.png' #path to your image file
    image_profile = QtGui.QImage(image_path) #QImage object
    image_profile = image_profile.scaled(513,123, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation) # To scale image for example and keep its Aspect Ration    
    label.setPixmap(QtGui.QPixmap.fromImage(image_profile))


if __name__ =='__main__':
    main()