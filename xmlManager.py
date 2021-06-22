from block import Juego
import xml.dom.minidom
import xml.etree.ElementTree as ET

class Manager:
    def read(nombre):
        matrices = ET.parse(nombre).getroot()

        filas = int(matrices[0][1].text)
        columnas = int(matrices[0][2].text)
        color1 = matrices[0][3].text
        color2 = matrices[0][4].text
        imagen = matrices[0][5].text

        juego = Juego(columnas, filas)

        juego.definirJugador("J1", color1)
        juego.definirJugador("J2", color2)
        juego.imagen = imagen
        return juego


        

    def write( juego, nombre):
        filas = str(juego.limY)
        columnas = str(juego.limX)
        color1 = juego.j1.color
        color2 = juego.j2.color
        imagen = juego.tableroMatriz.imprimir()
        
        matrices = ET.Element('matrices')
        nodoMatriz = ET.SubElement(matrices, 'matriz')
        nodoNombre = ET.SubElement(nodoMatriz, 'nombre')
        nodoNombre.text = nombre
        nodoFilas = ET.SubElement(nodoMatriz, 'filas')
        nodoFilas.text = filas
        nodoColumnas = ET.SubElement(nodoMatriz, 'columnas')
        nodoColumnas.text = columnas 
        nodoColor1 = ET.SubElement(nodoMatriz, 'color1')
        nodoColor1.text = color1 
        nodoColor2 = ET.SubElement(nodoMatriz, 'color2')
        nodoColor2.text = color2
        nodoImagen = ET.SubElement(nodoMatriz, 'imagen')
        nodoImagen.text = imagen

        stringData = ET.tostring(matrices, encoding='unicode', method='xml')
        f = open(nombre, "w")
        f.write(stringData)
        f.close()
        

