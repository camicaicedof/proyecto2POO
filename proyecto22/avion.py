from aeronave import Aeronave

class Avion(Aeronave):
    def __init__(self, id, marca, capacidad, mediator, modelo, velMax, anoFab, altitudMax, numMotores, categoria):
        # Llama al constructor de la clase base (Aeronave) usando super()
        super().__init__(id, marca, capacidad, mediator, modelo, velMax, anoFab)
        
        # Inicializa atributos específicos de Avion
        self.altitudMax = altitudMax
        self.numMotores = numMotores
        self.categoria = categoria

    def getAltitudMax(self):
        # Método para obtener la altitud máxima del avión
        return self.altitudMax

    def getCategoria(self):
        # Método para obtener la categoría del avión
        return self.categoria

    def getNumMotores(self):
        # Método para obtener el número de motores del avión
        return self.numMotores

    def print_info(self):
        # Llama al método de la clase base para imprimir información común de la aeronave
        super().printInfo()

    def obtenerDatos(self):
        # Método para obtener datos específicos del avión desde la entrada del usuario
        try:
            # Solicita al usuario ingresar el número de motores
            self.numMotores = int(input("Ingrese el número de motores: "))
            print()

            # Solicita al usuario ingresar la categoría
            self.categoria = int(input("Ingrese la categoría: "))
            print()

            # Solicita al usuario ingresar la altitud máxima
            self.altitudMax = int(input("Ingrese la altitud máxima: "))
            print()

        except ValueError:
            # Captura errores si el usuario no ingresa un número entero
            print("Error: Debe ingresar un número entero.")
