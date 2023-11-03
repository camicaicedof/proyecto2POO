class Persona:
    def __init__(self, nombre="", apellido="", edad=0, cedula="", fechaNacimiento="", genero="", direccion="", numTel="", correo=""):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.cedula = cedula
        self.fechaNacimiento = fechaNacimiento
        self.genero = genero
        self.direccion = direccion
        self.numTel = numTel
        self.correo = correo

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

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
