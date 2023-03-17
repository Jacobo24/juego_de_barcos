from clases import Tablero, Barco

CASO_NO_JUGADO = chr(0x2610)
CASO_TOCADO = chr(0x2611)
CASO_AGUA = chr(0x2612)


class Casilla:
    def __init__(self, letra, numero):
        self.letra = letra
        self.numero = numero
        self.estado = CASO_NO_JUGADO
        self.barco = None
    def __str__(self):
        return self.estado
    def jugar(self):
        if self.barco:
            self.estado = CASO_TOCADO
            self.barco.casillas.remove(self)
        else:
            self.estado = CASO_AGUA