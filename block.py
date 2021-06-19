from matrizDispersa import Matriz
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
        self.limX = m
        self.limY = n
        self.tableroMatriz = Matriz(m,n)
    
    def definirJugador(self, nick, color):
        if  self.j1:
            self.j2 = Jugador(nick, 2, color)
        else:
            self.j1 = Jugador(nick, 1, color)
    
    def cambioDeTurno(self, turno):
        if turno ==1:
            turno = 2
        else:
            turno = 1
        return turno

    def generarPieza(self):
        return random.randint(1,6)

    def colocarPieza(self, x, y, pieza, turno):
        permitido = True
        if pieza == 1:
            for i in range(y, y+4):
                permitido &= self.tableroMatriz.buscar(x, i) == None
                derecha = self.tableMatriz.buscar(x-1, i)
                permitido &= derecha.data != turno if derecha else True
                izquierda = self.tableMatriz.buscar(x+1, i)
                permitido &= izquierda.data != turno if izquierda else True
                arriba = self.tableMatriz.buscar(x, i+1)
                permitido &= arriba.data != turno if arriba else True
                abajo = self.tableMatriz.buscar(x, i-1)
                permitido &= abajo.data != turno if abajo else True
            for i in range(x, x+2):
                permitido &= self.tableroMatriz.buscar(i, y+3) == None
        if permitido:
            if pieza == 1:
                for i in range(y, y+4):
                    self.tableroMatriz.agregar(x, i, turno)
                for i in range(x, x+2):
                    self.tableroMatriz.agregar(i, y+3, turno)
        
        return permitido

#            self.tablero.agregar(x,y,turno)
#            permitido &= self.tablero.buscar(x, y) == None

prueba = Juego(10, 10)
prueba.colocarPieza(1,5,1,2)
prueba.colocarPieza(1,1,1,1)
prueba.colocarPieza(2,3,prueba.generarPieza(),1)
#prueba.tableroMatriz.mostrar()
