from aeronave import Aeronave

class JetPrivado(Aeronave):
    def __init__(self, id, marca, capacidad, mediator, modelo, velMax, anoFab, propietario, servicios, destinos):
        # Llama al constructor de la clase base (Aeronave) usando super()
        super().__init__(id, marca, capacidad, mediator, modelo, velMax, anoFab)
        
        # Inicializa atributos específicos de JetPrivado
        self.propietario = propietario
        self.listaServicios = servicios
        self.listaDestinos = destinos

    def getPropietario(self):
        # Método para obtener el propietario del jet privado
        return self.propietario

    def print_info(self):
        # Llama al método de la clase base para imprimir información común de la aeronave
        super().printInfo()

    def obtenerDatos(self):
        # Método para obtener datos específicos del jet privado desde la entrada del usuario
        try:
            # Solicita al usuario ingresar el nombre del propietario
            self.propietario = input("Ingrese el nombre del propietario: ")
            print()
        except Exception as e:
            # Captura cualquier excepción que pueda ocurrir durante la entrada del usuario
            print("Error:", e)
