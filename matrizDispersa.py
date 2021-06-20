
class NodoCabecera:
    def __init__(self, posicion) -> None:
        self.posicion = posicion
        self.next = None
        self.primero = None

class ListaCabecera:
    def  __init__(self) -> None:
        self.head = None
        self.primero = None
    
    def insertar(self, data):
        temp = NodoCabecera(data)
        if self.head:
            ultimo = self.head
            while ultimo.next != None:
                ultimo = ultimo.next
            ultimo.next = temp
        else:
            self.head = temp
    
class NodoLista:
    def __init__(self, data, x, y) -> None:
        self.data = data
        self.arriba = None
        self.derecha = None
        self.izquierda = None
        self.abajo = None
        self.x = x
        self.y = y

class ListaEnLista:
    def __init__(self) -> None:
        self.head = None
        self.next = None

    def insertar(self, x, y, listaX, listaY, data) -> bool:
        temp = NodoLista(data, x, y)
        #Creo el nodo a insertar
        xTemp = listaX.head
        yTemp = listaY.head
        #Busco las cabeceras correctas
        while xTemp.posicion != int(x):
            xTemp = xTemp.next
            
        while yTemp.posicion != int(y):
            yTemp = yTemp.next
        
        auxX = None
        auxY = None

        #Busco o genero el primero de la cabecera
        if xTemp.primero:
            auxX = xTemp.primero
        else:
            xTemp.primero = temp
                    
        if yTemp.primero:
            auxY = yTemp.primero
        else:
            yTemp.primero = temp
        
        """ contX = 0
        contY = 0 """
        #Me muevo en la matriz hacia abajo (x) o derecha (y) 
        """ while auxX and auxX.abajo != None and contX<y-1:
            auxX = auxX.abajo
            contX += 1 """
        
        """ while auxY and auxY.derecha != None and contY<x-1:
            auxY = auxY.derecha
            contY += 1 """

        while auxX and auxX.y < y and auxX.abajo != None:
            auxX = auxX.abajo

        while auxY and auxY.x < x and auxY.derecha != None:
            auxY = auxY.derecha

        if auxX and auxX.y < y:
            temp.abajo = auxX.abajo
            temp.arriba = auxX
            auxX.abajo = temp
        elif auxX and auxX.y > y:
            temp.arriba = auxX.arriba
            if auxX.arriba: auxX.arriba.abajo = temp
            temp.abajo = auxX
            auxX.arriba = temp
        elif auxX and auxX.y == y:
            return False

        if auxY and  auxY.x < x:
            temp.derecha = auxY.derecha
            if auxY.derecha: auxY.derecha.abajo = temp
            temp.izquierda = auxY
            auxY.derecha = temp
        elif auxY and  auxY.x > x:
            temp.derecha = auxY
            temp.izquierda = auxY.izquierda
            auxY.izquierda = temp
        elif auxY and  auxY.x == x:
            return False

        
        while xTemp.primero.arriba != None:
            xTemp.primero = xTemp.primero.arriba
        while yTemp.primero.izquierda != None:
            yTemp.primero = yTemp.primero.izquierda
        
        return True

    def  mostrar(self, listaX, listaY, limX, limY):
        tempXHead = listaX.head
        tempYHead = listaY.head
        #Prueba de recorrido en X

        print("\n Recorrido en X")
        cont = 0
        while cont < limX:
            while tempXHead and tempXHead.posicion == cont:
                temp = tempXHead.primero
                contY = 0
                string = ""
                while temp != None:
                    string += " ["+ str(temp.x) + "," + str(temp.y) +"] "+ str(temp.data) + "\t <> \t"
                    contY += 1
                    temp = temp.abajo
                string += "\n"
                for i in range(contY):
                    string += " /\ \/ \t\t\t"
                print(string)
                tempXHead = tempXHead.next
                cont += 1

        #Prueba de recorrido en Y
        print("\n Recorrido en Y")
        cont = 0
        while cont < limY:
            while tempYHead and tempYHead.posicion == cont:
                temp = tempYHead.primero
                contX = 0
                string = ""
                while temp != None:
                    string += " ["+ str(temp.x) + "," + str(temp.y) +"] "+str(temp.data) + "\t >< \t"
                    contX += 1
                    temp = temp.derecha
                string += "\n"
                string += contX * " /\ \/ \t\t\t"
                string += "\n"
                print(string)
                tempYHead = tempYHead.next
                cont += 1

    def generarDot(self, listaX, listaY, limX, limY):
        tempYHead = listaY.head
        cont = 0
        string = "digraph {node [shape = box]"

        for j in range(0, limY+1):
            rank = "{ rank = same;"
            for i in range(0, limX+1):
                temp = self.buscar(listaX, i, j, limX, limY)
                data = ""
                if temp:
                    data = temp.data
                else:
                    data = "-"
                tag = "\""+ str(i) + "," + str(j) +"\""
                #["+ str(i) + "," + str(j) +"] 
                string += "\n" + tag + " [label=\""+str(data) + "\", group= "+str(i)+"]\n"
                if j<limY:    
                    string+= tag + " -> " + "\"" + str(i) + "," + str(j+1) + "\"\n"
                if j>0:    
                    string+= tag + " -> " + "\"" + str(i) + "," + str(j-1) + "\"\n"
                if i> 0: 
                    string+= tag + " -> " + "\"" + str(i-1) + "," + str(j) + "\"\n"
                if  i<limX:    
                    string+= tag + " -> " + "\"" + str(i+1) + "," + str(j) + "\"\n"
                rank += "\""+ str(i) + "," + str(j) +"\"; "
            string += rank +"}"
        string += "}"  + "\n"
        return string

    def buscar(self, listaX, x, y, limX, limY):
        tempXHead = listaX.head
        #Prueba de busqueda a partir de X

        #print("\n Buscado en X")
        cont = 0
        while cont < limX:
            while tempXHead:
                temp = tempXHead.primero
                while temp and temp.x == x:
                    #string += " ["+ str(temp.x) + "," + str(temp.y) +"] "+temp.data + "\t"
                    if temp.y == y:
                        return temp
                    elif temp.y < y:
                        temp = temp.abajo
                    elif temp.y>y:
                        return None
                tempXHead = tempXHead.next
                cont += 1


import os
class Matriz:
    def __init__(self, x, y) -> None:
        self.x = x-1
        self.y = y-1
        self.listaX = ListaCabecera()
        self.listaY = ListaCabecera()
        for i in range(int(x)):
            self.listaX.insertar(i)
        for i in range(int(y)):
            self.listaY.insertar(i)
    
    def agregar(self, x, y, data):
        listaTemporal = ListaEnLista()
        if x <= self.x and y <= self.y:
            if not listaTemporal.insertar(x, y, self.listaX, self.listaY, data):
                print("Espacio ya ocupado [%d, %d]" % (x, y))
    
    def mostrar(self):
        listaTemporal = ListaEnLista()
        listaTemporal.mostrar(self.listaX, self.listaY, self.x, self.y)

    def generarDot(self):
        listaTemporal = ListaEnLista()
        estructura = listaTemporal.generarDot(self.listaX, self.listaY, self.x, self.y)
        f = open("matriz.dot", "w")
        f.write(estructura)
        f.close()

        os.system("dot -Tjpg matriz.dot -o matriz.png")
        os.startfile("matriz.png")

    def buscar(self, x, y) -> NodoLista:
        listaTemporal = ListaEnLista()
        temp = listaTemporal.buscar(self.listaX, x, y, self.x, self.y)
        """ if temp:
            print(temp.data)
        else:
            print("Coordenada inexistente") """
        return temp

    def __getitem__(self, key):
        return self.buscar(key[0], key[1])
    def __setitem__(self, key, value):
        return self.agregar(key[0], key[1], value) 


""" matriz = Matriz(4,3)
matriz.agregar(1,1, "Hola")
matriz.agregar(1,0, "H")
matriz.agregar(0,1, "A")
matriz[2,1] = "Aloha"
matriz[2,1] = "A"
matriz.agregar(3,2, "A")
matriz.agregar(0,0, "Adios")
matriz.agregar(0,0, "B")
matriz.mostrar()
print(matriz[2,1].data) """