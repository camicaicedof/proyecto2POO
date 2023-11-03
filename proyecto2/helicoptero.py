from aeronave import Aeronave


class Helicoptero(Aeronave):
    def __init__(self, marca, capacidad, mediator):
        super().__init__(marca, capacidad, mediator)
        self.numRotores = 0
        self.maxElevacion = 0
        self.uso = ""

    def getNumRotores(self):
        return self.numRotores

    def getMaxElevacion(self):
        return self.maxElevacion

    def getUso(self):
        return self.uso

    def printInfo(self):
        super().printInfo()

    def obtenerDatos(self):
        try:
            self.numRotores = int(input("Ingrese el número de rotores: "))
            print()

            self.maxElevacion = int(input("Ingrese la máxima elevación: "))
            print()

            self.uso = input("Ingrese el tipo de uso: ")
            print()

        except ValueError:
            print(
                "Error: Debe ingresar un número entero para el número de rotores y la máxima elevación.")
