from torreControl import TorreControl
""" from vuelos import Vuelos """


class Aeropuerto:
    instancia = None

    def __init__(self):
        self.vuelos = []
        self.torreControl = TorreControl()

    @classmethod
    def obtenerInstancia(cls):
        if cls.instancia is None:
            cls.instancia = cls()
        return cls.instancia

    def agregarDestino(self, vuelo):
        self.vuelos.append(vuelo)

    def printDestinos(self):
        l=[]
        if not self.vuelos:
            l.append("No hay vuelos")
        else:
            for vuelo in enumerate(self.vuelos, 1):
                #print(f"{i}.")
                l.append(vuelo.printVuelo())
        return l

    def disponibilidadVuelos(self):
        return bool(self.vuelos)

    def disponibilidadAeronaves(self):
        return self.torreControl.disponibilidadNaves()

    def asignarVuelo(self):
        for vuelo in self.vuelos:
            self.torreControl.seleccionarAeronave(vuelo)

    def obtenerVuelo(self, pos):
        return self.vuelos[pos]

    def agregarAeronave(self, nave):
        self.torreControl.aeronaves.append(nave)