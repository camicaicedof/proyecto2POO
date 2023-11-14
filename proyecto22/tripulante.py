# Importación de la clase Persona
from persona import Persona

# Definición de la clase Tripulante que hereda de Persona
class Tripulante(Persona):
    # Constructor de la clase Tripulante
    def __init__(self, nombre, apellido, edad, cedula, fechaNacimiento, genero, direccion, numTel, correo, cargo, xp, hrsDiarias):
        # Llamada al constructor de la clase base (Persona)
        super().__init__(nombre, apellido, edad, cedula, fechaNacimiento, genero, direccion, numTel, correo)
        # Atributos específicos de la clase Tripulante
        self.cargo = cargo
        self.xp = xp
        self.hrsDiarias = hrsDiarias

    # Método para obtener información del tripulante
    def getInformacion(self):
        # Llamada al método de la clase base (Persona) para obtener información personal
        super().getInformacion()
        # Información específica del tripulante
        print("Cargo en el avión:", self.cargo)
        print("Años de experiencia:", self.xp)
        print("Horas diarias:", self.hrsDiarias)

    # Método de clase para crear un nuevo tripulante a partir de la entrada del usuario
    @classmethod
    def crearTripulante(cls):
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        edad = int(input("Ingrese edad: "))
        cedula = input("Ingrese cedula: ")
        fechaNacimiento = input("Ingrese fecha de nacimiento: ")
        genero = input("Ingrese genero: ")
        direccion = input("Ingrese direccion: ")
        numTel = input("Ingrese número de teléfono: ")
        correo = input("Ingrese correo: ")
        cargo = input("Ingrese cargo: ")
        xp = int(input("Ingrese experiencia (xp): "))
        hrsDiarias = int(input("Ingrese horas diarias de trabajo: "))

        # Creación de una nueva instancia de la clase Tripulante
        return cls(nombre, apellido, edad, cedula, fechaNacimiento, genero, direccion, numTel, correo, cargo, xp, hrsDiarias)
