# Definición de la clase Persona
class Persona:
    # Constructor de la clase, que inicializa los atributos con valores predeterminados
    def __init__(self, nombre="", apellido="", edad=0, cedula="", fechaNacimiento="", genero="", direccion="", numTel="", correo=""):
        # Inicialización de los atributos con los valores proporcionados o valores predeterminados
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.cedula = cedula
        self.fechaNacimiento = fechaNacimiento
        self.genero = genero
        self.direccion = direccion
        self.numTel = numTel
        self.correo = correo

    # Método para obtener el nombre de la persona
    def getNombre(self):
        return self.nombre

    # Método para obtener la edad de la persona
    def getEdad(self):
        return self.edad

    # Método para imprimir la información de la persona
    def getInformacion(self):
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("Edad:", self.edad, "years")
        print("Cedula:", self.cedula)
        print("Fecha de Nacimiento:", self.fechaNacimiento)
        print("Genero:", self.genero)
        print("Direccion:", self.direccion)
        print("Numero de Telefono:", self.numTel)
        print("Correo Electronico:", self.correo)
