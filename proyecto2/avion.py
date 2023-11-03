from aeronave import Aeronave


class Avion(Aeronave):
    def __init__(self, marca, capacidad, mediator):
        super().__init__(marca, capacidad, mediator)
        self.altitudMax = 0
        self.numMotores = 0
        self.categoria = 0

    def getAltitudMax(self):
        return self.altitudMax

    def getCategoria(self):
        return self.categoria

    def getNumMotores(self):
        return self.numMotores

    def print_info(self):
        super().printInfo()

    def obtenerDatos(self):
        try:
            self.numMotores = int(input("Ingrese el número de motores: "))
            print()

            self.categoria = int(input("Ingrese la categoría: "))
            print()

            self.altitudMax = int(input("Ingrese la altitud máxima: "))
            print()

        except ValueError:
            print("Error: Debe ingresar un número entero.")
