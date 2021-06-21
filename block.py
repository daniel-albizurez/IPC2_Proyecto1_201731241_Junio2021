from matrizDispersa import Matriz
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore, QtGui
import random

class Jugador:
    def __init__(self, nick, valor, color) -> None:
        self.nick = nick
        self.valor = valor
        self.color = color

class Juego:
    def __init__(self, m, n) -> None:
        self.j1 = None
        self.j2 = None
        self.jugadorEnTurno = None
        self.turno = random.randint(1,2)
        self.piezaActual = self.generarPieza()
        self.limX = m
        self.limY = n
        self.tableroMatriz = Matriz(m,n)
        self.oportunidad = 1
    
    def definirJugador(self, nick, color):
        if  self.j1:
            self.j2 = Jugador(nick, 2, color)
        else:
            self.j1 = Jugador(nick, 1, color)
    
    def cambioDeTurno(self):
        if self.turno == 1:
            self.jugadorEnTurno = self.j2
            self.turno = 2
        else:
            self.jugadorEnTurno = self.j1
            self.turno = 1
        self.oportunidad = 1
        self.piezaActual = self.generarPieza()

    def generarPieza(self):
        return random.randint(1,6)

    def colocarPieza(self, x, y, pieza, turno, tablero):
        permitido = True
        rangoX = 0
        rangoY = 0
        if pieza == 1:
            rangoX = 2
            rangoY = 4
            permitido &= x+rangoX <= self.limX
            permitido &= y+rangoY <= self.limY
            for i in range(y, y+rangoY):
                permitido &= self.tableroMatriz.buscar(x, i) == None
                permitido &= self.evaluarAlrededor(x, i, turno)
            #for i in range(x, x+rangoX):
            permitido &= self.tableroMatriz.buscar(x+1, y+3) == None            
            permitido &= self.evaluarAlrededor(x+1, y+3, turno)
        elif pieza == 2:
            permitido &= x>0
            #rangoX = x
            #x = x-1
            rangoY = 4
            permitido &= x+rangoX <= self.limX
            permitido &= y+rangoY <= self.limY
            for i in range(y, y+rangoY):
                permitido &= self.tableroMatriz.buscar(x, i) == None
                permitido &= self.evaluarAlrededor(x, i, turno)
            #for i in range(x, x+rangoX):
            permitido &= self.tableroMatriz.buscar(x-1, y+3) == None            
            permitido &= self.evaluarAlrededor(x-1, y+3, turno)
        elif pieza == 3:
            rangoX = 4
            permitido &= x+rangoX <= self.limX
            permitido &= y+rangoY <= self.limY
            for i in range(x, x+rangoX):
                permitido &= self.tableroMatriz.buscar(i, y) == None            
                permitido &= self.evaluarAlrededor(i, y, turno)
        elif pieza == 4:
            for i in range(x, x+2):
                for j in range(y, y+2):
                    permitido &= self.tableroMatriz.buscar(i, j) == None
                    permitido &= self.evaluarAlrededor(i, j, turno)
        elif pieza == 5:
            permitido &= y>0

            for i in range(x+1, x+3):
                for j in range(y-1, y+1):
                    permitido &= self.tableroMatriz.buscar(i, j) == None
                    permitido &= self.evaluarAlrededor(i, j, turno)
            permitido &= self.tableroMatriz.buscar(x, y) == None
            permitido &= self.evaluarAlrededor(x,y, turno)
            permitido &= self.tableroMatriz.buscar(x+3, y) == None
            permitido &= self.evaluarAlrededor(x+3, y, turno)
        elif pieza == 6:
            rangoY = 4
            permitido &= x+rangoX <= self.limX
            permitido &= y+rangoY <= self.limY
            for i in range(y, y+rangoY):
                permitido &= self.tableroMatriz.buscar(x, i) == None            
                permitido &= self.evaluarAlrededor(x, i, turno)
                
        if permitido:           
            if pieza == 1:
                for i in range(y, y+4):
                    self.colocarEnTabla(x, i, tablero)
                """ for i in range(x, x+2):
                    #self.tableroMatriz.agregar(i, y+3, turno)
                    self.colocarEnTabla(i, y+3, tablero) """
                self.colocarEnTabla(x+1, y+3, tablero)
            elif pieza == 2:
                for i in range(y, y+4):
                    """ self.tableroMatriz.agregar(x+1, i, turno)
                    tablero.setItem(i,x+1,QTableWidgetItem(turno))
                    tablero.item(i,x+1).setBackground(QtGui.QColor(self.jugadorEnTurno.color))
                    tablero.item(i,x+1).setForeground(QtGui.QColor(self.jugadorEnTurno.color))
                    tablero.item(i,x+1).setFlags(QtCore.Qt.ItemIsEnabled) """
                    self.colocarEnTabla(x, i, tablero)
                """ for i in range(x, x+2):
                    self.colocarEnTabla(i, y+3, tablero)
                    self.tableroMatriz.agregar(i, y+3, turno)
                    tablero.setItem(y+3,i,QTableWidgetItem(turno))
                    tablero.setItem(y+3,i,QTableWidgetItem(turno))
                    tablero.item(y+3,i).setBackground(QtGui.QColor(self.jugadorEnTurno.color))
                    tablero.item(y+3,i).setForeground(QtGui.QColor(self.jugadorEnTurno.color))
                    tablero.item(y+3,i).setFlags(QtCore.Qt.ItemIsEnabled) """
                self.colocarEnTabla(x-1, y+3, tablero)
            elif pieza == 3:
                for i in range(x, x+rangoX):
                    self.colocarEnTabla(i, y, tablero)
                    """ self.tableroMatriz.agregar(i, y, turno)
                    tablero.setItem(y,i,QTableWidgetItem(turno))
                    tablero.setItem(y,i,QTableWidgetItem(turno))
                    tablero.item(y,i).setBackground(QtGui.QColor(self.jugadorEnTurno.color))
                    tablero.item(y,i).setForeground(QtGui.QColor(self.jugadorEnTurno.color))
                    tablero.item(y,i).setFlags(QtCore.Qt.ItemIsEnabled) """
            elif pieza == 4:
                for i in range(x, x+2):
                    for j in range(y, y+2):
                        self.colocarEnTabla(i, j, tablero)
                        """ self.tableroMatriz.agregar(i, j, turno)
                        tablero.setItem(j,i,QTableWidgetItem(turno))
                        tablero.setItem(j,i,QTableWidgetItem(turno))
                        tablero.item(j,i).setBackground(QtGui.QColor(self.jugadorEnTurno.color))
                        tablero.item(j,i).setForeground(QtGui.QColor(self.jugadorEnTurno.color))
                        tablero.item(j,i).setFlags(QtCore.Qt.ItemIsEnabled) """
            elif pieza == 5:
                for i in range(x+1, x+3):
                    for j in range(y-1, y+1):
                        self.colocarEnTabla(i,j, tablero)
                self.colocarEnTabla(x, y, tablero)
                self.colocarEnTabla(x+3, y, tablero)
            elif pieza == 6:
                for i in range(y, y+rangoY):
                    self.colocarEnTabla(x, i, tablero)

            self.cambioDeTurno()
        else:
            self.oportunidad += 1
            if self.oportunidad > 2:
                self.cambioDeTurno()


    def colocarEnTabla(self, x, y, tablero):
        self.tableroMatriz.agregar(x, y, self.turno)
        tablero.setItem(y,x,QTableWidgetItem(self.turno))
        tablero.setItem(y,x,QTableWidgetItem(self.turno))
        tablero.item(y,x).setBackground(QtGui.QColor(self.jugadorEnTurno.color))
        tablero.item(y,x).setForeground(QtGui.QColor(self.jugadorEnTurno.color))
        tablero.item(y,x).setFlags(QtCore.Qt.ItemIsEnabled)

    def evaluarAlrededor(self, x, y, turno):
        permitido = True
        derecha = self.tableroMatriz.buscar(x+1, y)
        permitido &= derecha.data != turno if derecha else True
        izquierda = self.tableroMatriz.buscar(x-1, y)
        permitido &= izquierda.data != turno if izquierda else True
        abajo = self.tableroMatriz.buscar(x, y-1)
        permitido &= abajo.data != turno if abajo else True
        arriba = self.tableroMatriz.buscar(x, y+1)
        permitido &= arriba.data != turno if arriba else True
        return permitido


#            self.tablero.agregar(x,y,turno)
#            permitido &= self.tablero.buscar(x, y) == None

""" prueba = Juego(10, 10)
prueba.colocarPieza(1,5,1,2)
prueba.colocarPieza(1,1,1,1)
prueba.colocarPieza(2,3,prueba.generarPieza(),1) """
#prueba.tableroMatriz.mostrar()
