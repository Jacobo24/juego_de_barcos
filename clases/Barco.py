from clases import Casilla, Tablero
from random import choice
from itertools import product, repeat

class Barco:
    def __init__(self, nombre, longitud):
        self.nombre = nombre
        self.longitud = longitud
        self.casillas = []
        self.orientacion = None
    def __str__(self):
        return self.nombre