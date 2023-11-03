from persona import Persona
""" from vuelos import Vuelos """


class Pasajero(Persona):
    def __init__(self, nombre="", apellido="", edad=0, cedula="", fechaNacimiento="", genero="", direccion="", numTel="", correo="", nacionalidad="", infoMedica="", numMaletasBodega=0):
        super().__init__(nombre, apellido, edad, cedula,
                         fechaNacimiento, genero, direccion, numTel, correo)
        self.nacionalidad = nacionalidad
        self.infoMedica = infoMedica
        self.numMaletasBodega = numMaletasBodega
        self.vuelo = None  # Inicialmente no tiene un vuelo asignado

    def getNumMaletas(self):
        return self.numMaletasBodega

    def asignarVuelo(self, vuelo):
        if vuelo.disponible():
            self.vuelo = vuelo
            print("El vuelo se asignó correctamente.")
        else:
            print("El vuelo no está disponible.")

    # @classmethod
    def obtenerDatosPasajero(cls):
        nombre = input("Ingrese el nombre del pasajero: ")
        apellido = input("Ingrese el apellido del pasajero: ")
        edad = int(input("Ingrese la edad del pasajero: "))
        cedula = input("Ingrese la cédula del pasajero: ")
        fechaNacimiento = input(
            "Ingrese la fecha de nacimiento del pasajero: ")
        genero = input("Ingrese el género del pasajero: ")
        direccion = input("Ingrese la dirección del pasajero: ")
        numTel = input("Ingrese el número de teléfono del pasajero: ")
        correo = input("Ingrese el correo del pasajero: ")
        nacionalidad = input("Ingrese la nacionalidad del pasajero: ")
        infoMedica = input("Ingrese la información médica del pasajero: ")
        numMaletasBodega = int(input("Ingrese el número de maletas en la bodega: "))
        pasajero=Pasajero(nombre, apellido, edad, cedula, fechaNacimiento, genero, direccion, numTel, correo, nacionalidad, infoMedica, numMaletasBodega)
        return pasajero
        #return cls(nombre, apellido, edad, cedula, fechaNacimiento, genero, direccion, numTel, correo, nacionalidad, infoMedica, numMaletasBodega)

    def getInformacion(self):
        super().getInformacion()
        print("Número de Maletas en Bodega:", self.numMaletasBodega)
        print("Nacionalidad:", self.nacionalidad)
        print("Información Médica:", self.infoMedica)
        if self.vuelo:
            # Se asume que la clase Vuelos tiene un método getInformacion
            print("Vuelo Asignado:", self.vuelo.getInformacion())
