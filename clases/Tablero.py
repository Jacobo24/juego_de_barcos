from clases import Casilla, Barco

class Tablero:
    def __init__(self):
        self.casillas = {}
        self.barcos = []
        
        # Crear las casillas del tablero
        for letra in 'ABCDEFGHIJ':
            for numero in range(1, 11):
                nombre_casilla = letra + str(numero)
                self.casillas[nombre_casilla] = Casilla(letra, numero)




