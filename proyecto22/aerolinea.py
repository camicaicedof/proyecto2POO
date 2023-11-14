# Importa la clase Vuelos desde el módulo vuelos
from vuelos import Vuelos

class Aerolinea():

    def __init__(self, nombre):
        # Constructor de la clase Aerolinea, inicializa el nombre de la aerolínea y la lista de vuelos
        self.nombre = nombre
        self.vuelos = []

    def getNombre(self):
        # Método para obtener el nombre de la aerolínea
        return self.nombre()

    def getVuelos(self):
        # Método para obtener la lista de vuelos de la aerolínea
        return self.vuelos()

    def agregarVuelo(self, vuelo):
        # Método para agregar un vuelo a la lista de vuelos de la aerolínea
        self.vuelos.append(vuelo)
