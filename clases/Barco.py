from clases import Tablero
from clases import Case
from clases import Conventions
from random import choice
from itertools import product, repeat
from juego import ORIENTACIONES, HORIZONTAL, VERTICAL

instances = []
casillas_ocupadas = set()

 # performance / legibilidad:
num_lineas = Conventions.tablero_num_lineas
num_columnas = Conventions.tablero_num_columnas
num2l = Conventions.generar_num_linea
num2c = Conventions.generar_num_columna

def __init__(self, longitud, orientacion, tocado, hundido):
        self.longitud = longitud
        self.orientacion = choice(ORIENTACIONES)
        self.tocado = False
        self.hundido = False

def horizontal(self):
        if self.orientacion == HORIZONTAL:
            rang = choice(range(num_lineas))
            primero = choice(range(num_columnas + 1 - LONGITUDES_BARCOS))
            letra = num2l(rang)
            cifras = [num2c(x) for x in range(primero, primero + LONGITUDES_BARCOS)]
            self.casillas = {Case.instances[l + c]
                          for l, c in product(repeat(letra, LONGITUDES_BARCOS), cifras)}
                
        else:
            rang = choice(range(num_columnas))
            primero = choice(range(num_lineas + 1 - LONGITUDES_BARCOS))
            cifra = num2c(rang)
            letras = [num2l(x) for x in range(primero, primero + LONGITUDES_BARCOS)]
            # Crear el barco
            self.casillas = {Case.instances[l + c]
                       for l, c in product(letras, repeat(cifra, LONGITUDES_BARCOS))}
def instancial(self):
            for existente in instances:
                if self.casillas.intersection(existente.casillas):
                    break  # break relativo al "for existente in barcos:"
            else:
                # Agregar el barco en el contenedor de barcos
                instances.append(self)
                # Informar la casilla que contiene un barco.
                for casilla in self.casillas:
                    casilla.barco = self
                # Agregar estas casillas a las casillas ocupadas :
                for casillas_ocupadas in self.casillas
                break  # break relativo al "while True:"

def generar_barcos(self):
        While True:
        self_longitud = choice(Conventions.barcos_longitud)
        self_orientacion = choice(ORIENTACIONES)
        self_tocado = False
        self_hundido = False

@classmethod
def generar_barcos(cls):
        for longitud in Conventions.barcos_longitud:
            cls(longitud, HORIZONTAL, False, False)