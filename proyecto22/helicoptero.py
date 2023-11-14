from aeronave import Aeronave

class Helicoptero(Aeronave):
    def __init__(self, id, marca, capacidad, mediator, modelo, velMax, anoFab, numRotores, maxElevacion, uso):
        # Llama al constructor de la clase base (Aeronave) usando super()
        super().__init__(id, marca, capacidad, mediator, modelo, velMax, anoFab)
        
        # Inicializa atributos específicos de Helicoptero
        self.numRotores = numRotores
        self.maxElevacion = maxElevacion
        self.uso = uso

    def getNumRotores(self):
        # Método para obtener el número de rotores del helicóptero
        return self.numRotores

    def getMaxElevacion(self):
        # Método para obtener la máxima elevación del helicóptero
        return self.maxElevacion

    def getUso(self):
        # Método para obtener el tipo de uso del helicóptero
        return self.uso

    def print_info(self):
        # Llama al método de la clase base para imprimir información común de la aeronave
        super().printInfo()

    def obtenerDatos(self):
        # Método para obtener datos específicos del helicóptero desde la entrada del usuario
        try:
            # Solicita al usuario ingresar el número de rotores
            self.numRotores = int(input("Ingrese el número de rotores: "))
            print()

            # Solicita al usuario ingresar la máxima elevación
            self.maxElevacion = int(input("Ingrese la máxima elevación: "))
            print()

            # Solicita al usuario ingresar el tipo de uso
            self.uso = input("Ingrese el tipo de uso: ")
            print()

        except ValueError:
            # Captura errores si el usuario no ingresa un número entero
            print(
                "Error: Debe ingresar un número entero para el número de rotores y la máxima elevación.")
