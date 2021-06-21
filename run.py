from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
import sys
import ventana
import block

def main():
    app = QApplication(sys.argv)
    form = ventana.Principal()
    """ juego = block.Juego(10, 10)
    definirTablero(form, 10,10)

    juego.definirJugador("hola", "blue")
    juego.definirJugador("a", "yellow")
    juego.cambioDeTurno() """
    juego = modificar()
    cont = 0
    while juego is None:
        juego = modificar()
        cont += 1
        if cont >= 2:
            break
    if juego:
        juego.cambioDeTurno()
        mostrarPieza(juego.piezaActual, form.labelPieza, form.labelTurno, juego.jugadorEnTurno)
        definirTablero(form, juego.limX, juego.limY)

        form.pushButton.clicked.connect(lambda: juego.colocarPieza(
            int(form.spinX.text())-1,
            int(form.spinY.text())-1,
            juego.piezaActual,
            juego.turno,
            form.tableWidget
        ))
        form.pushButton.clicked.connect(lambda: mostrarPieza(
            juego.piezaActual,
            form.labelPieza,
            form.labelTurno,
            juego.jugadorEnTurno
            ))

        form.actionReglas.triggered.connect(ayuda)
        #form.actionNueva.triggered.connect(modificar)
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

def mostrarPieza(pieza, label, labelTurno, jugador):
    image_path = 'C:/Users/DANIEL/Documents/U/USAC/IPC2 Vaqueras/Prueba/Grafico/piezas/'+str(pieza)+'.png' #path to your image file
    image_profile = QtGui.QImage(image_path) #QImage object
    image_profile = image_profile.scaled(513,123, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation) # To scale image for example and keep its Aspect Ration    
    label.setPixmap(QtGui.QPixmap.fromImage(image_profile))
    labelTurno.setText("Jugador: "+ jugador.nick)

def ayuda():
    modal = ventana.Ayuda()
    modal.show()
    modal.exec_()

def modificar() -> block.Juego:
    modal = ventana.Modif()
    modal.juego = None
    modal.pushButton.clicked.connect(lambda:
        definirJuego(modal)
    )
    modal.pushButton.clicked.connect(modal.close)
    modal.show()
    modal.exec_()
    return modal.juego

def definirJuego(modal):
    x = int(modal.spinBox.text())
    y = int(modal.spinBox_2.text())
    color1 = definirColor(modal.buttonG1)
    color2 = definirColor(modal.buttonG2)
    if color1 != color2:
        modal.juego = block.Juego(x, y)
        modal.juego.definirJugador(modal.plainTextEdit.toPlainText(), color1)
        modal.juego.definirJugador(modal.plainTextEdit_2.toPlainText(), color2)
    else:
        modal.juego = None
        modal.labelAviso.setText("Seleccione colores distintos")

def definirColor(buttonGroup):
    color = ""
    if buttonGroup.checkedId() == 1:
        color = "blue"
    elif buttonGroup.checkedId() == 2:
        color = "yellow"
    elif buttonGroup.checkedId() == 3:
        color = "red"
    elif buttonGroup.checkedId() == 4:
        color = "green"
    return color

if __name__ =='__main__':
    main()