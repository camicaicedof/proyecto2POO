from persona import Persona


class Tripulante(Persona):
    def __init__(self, nombre, apellido, edad, cedula, fechaNacimiento, genero, direccion, numTel, correo, cargo, xp, hrsDiarias):
        super().__init__(nombre, apellido, edad, cedula,
                         fechaNacimiento, genero, direccion, numTel, correo)
        self.cargo = cargo
        self.xp = xp
        self.hrsDiarias = hrsDiarias

    def getInformacion(self):
        super().getInformacion()
        print("Cargo en el avion:", self.cargo)
        print("Años de experiencia:", self.xp)
        print("Horas diarias:", self.hrsDiarias)

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

        return cls(nombre, apellido, edad, cedula, fechaNacimiento, genero, direccion, numTel, correo, cargo, xp, hrsDiarias)
