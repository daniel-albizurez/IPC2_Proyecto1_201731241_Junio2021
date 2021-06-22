from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QFileDialog, QTableWidgetItem
import sys
import ventana
import block
import xmlManager

class Main:
    def __init__(self) -> None:
        self.form = None
        self.juego = None


    def main(self):
        app = QApplication(sys.argv)    
        self.nuevaPartida(app)
        app.exec_()

    def definirTablero(self, form,x, y):
        form.spinX.setMaximum(x)
        form.spinY.setMaximum(y)
        form.spinX.setMinimum(1)
        form.spinY.setMinimum(1)
        while form.tableWidget.rowCount()>0:
            form.tableWidget.removeRow(0)
        form.tableWidget.setRowCount(y)
        form.tableWidget.setColumnCount(x)

    def mostrarPieza(self, pieza, label, labelTurno, jugador):
        image_path = 'C:/Users/DANIEL/Documents/U/USAC/IPC2 Vaqueras/Prueba/Grafico/piezas/'+str(pieza)+'.png' #path to your image file
        image_profile = QtGui.QImage(image_path) #QImage object
        image_profile = image_profile.scaled(513,123, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation) # To scale image for example and keep its Aspect Ration    
        label.setPixmap(QtGui.QPixmap.fromImage(image_profile))
        labelTurno.setText("Jugador: "+ jugador.nick)
        #Condicion ganadora
        if self.juego.espaciosDisponibles() < 15 or self.juego.turnosPerdidos >= 3:
            self.form.pushButton.setEnabled(False)
            ganador = self.juego.ganador()
            if ganador:
                self.form.pushButton.setText("El ganador es: " + ganador.nick + " con puntos " + str(ganador.puntaje))
            else:
                self.form.pushButton.setText("Empate")

    def ayuda(self):
        modal = ventana.Ayuda()
        modal.show()
        modal.exec_()

    def modificar(self) -> block.Juego:
        modal = ventana.Modif()
        self.juego = None
        modal.pushButton.clicked.connect(lambda:
            self.definirJuego(modal)
        )
        modal.pushButton.clicked.connect(modal.close)
        modal.show()
        modal.exec_()

    def definirJuego(self, modal):
        x = int(modal.spinBox.text())
        y = int(modal.spinBox_2.text())
        color1 = self.definirColor(modal.buttonG1)
        color2 = self.definirColor(modal.buttonG2)
        if color1 != color2:
            self.juego = block.Juego(x, y)
            self.juego.definirJugador(modal.plainTextEdit.toPlainText(), color1)
            self.juego.definirJugador(modal.plainTextEdit_2.toPlainText(), color2)
        else:
            self.juego = None
            self.labelAviso.setText("Seleccione colores distintos")

    def definirColor(self, buttonGroup):
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

    def nuevaPartida(self, app):
        app.closeAllWindows()
        
        self.form = ventana.Principal()
        """ juego = block.Juego(10, 10)
        definirTablero(form, 10,10)

        juego.definirJugador("hola", "blue")
        juego.definirJugador("a", "yellow")
        juego.cambioDeTurno() """
        self.modificar()
        cont = 0
        while self.juego is None:
            self.modificar()
            cont += 1
            if cont >= 2:
                break
        if self.juego:
            self.juego.cambioDeTurno()
            self.mostrarPieza(self.juego.piezaActual, self.form.labelPieza, self.form.labelTurno, self.juego.jugadorEnTurno)
            self.definirTablero(self.form, self.juego.limX, self.juego.limY)

            self.form.pushButton.clicked.connect(lambda: self.juego.colocarPieza(
                int(self.form.spinX.text())-1,
                int(self.form.spinY.text())-1,
                self.juego.piezaActual,
                self.juego.turno,
                self.form.tableWidget
            ))
            self.form.pushButton.clicked.connect(lambda: self.mostrarPieza(
                self.juego.piezaActual,
                self.form.labelPieza,
                self.form.labelTurno,
                self.juego.jugadorEnTurno
                ))

            self.form.actionReglas.triggered.connect(self.ayuda)
            self.form.actionNueva.triggered.connect(lambda: self.nuevaPartida(app))
            self.form.actionGuardar.triggered.connect(self.guardarPartida)
            self.form.actionAbrir.triggered.connect(self.abrirPartida)
            #form.pushButton.clicked.connect(juego.tableroMatriz.generarDot)
            self.form.show()

    def abrirPartida(self):
        nombre = QFileDialog.getOpenFileName(self.form, 'Abrir partida', 'c:\\', 'XML (*.xml)')

        manager = xmlManager.Manager
        self.juego = manager.read(nombre[0])
        self.definirTablero(self.form, self.juego.limX, self.juego.limY)
        imagen = self.juego.imagen
        y = 0
        x = -1
        for i in range(len(imagen)):
            dato = imagen[i]
            x += 1
            if dato == '\n':
                y += 1
                x = -1
            elif  dato != '-':
                color = ""
                if dato == '1':
                    color = self.juego.j1.color
                elif dato == '2':
                    color = self.juego.j2.color
                self.juego.colocarEnTabla(x, y, int(dato),color , self.form.tableWidget)
            self.juego.cambioDeTurno()
            self.mostrarPieza(self.juego.piezaActual, self.form.labelPieza, self.form.labelTurno, self.juego.jugadorEnTurno)

    def guardarPartida(self):
        nombre = QFileDialog.getSaveFileName(self.form, 'Abrir partida', 'c:\\', 'XML (*.xml)')

        manager = xmlManager.Manager
        manager.write(self.juego, nombre[0])
if __name__ =='__main__':
    principal = Main()
    principal.main()