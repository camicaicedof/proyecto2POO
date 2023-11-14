from persona import Persona
from vuelos import Vuelos

# La clase Pasajero hereda de la clase Persona
class Pasajero(Persona):
    # Constructor de la clase Pasajero que toma varios parámetros, algunos de los cuales tienen valores predeterminados
    def __init__(self, nombre="", apellido="", edad=0, cedula="", fechaNacimiento="", genero="", direccion="", numTel="", correo="", nacionalidad="", infoMedica="", numMaletasBodega=0):
        # Llama al constructor de la clase padre (Persona) usando super()
        super().__init__(nombre, apellido, edad, cedula,
                         fechaNacimiento, genero, direccion, numTel, correo)
        # Atributos específicos de Pasajero
        self.nacionalidad = nacionalidad
        self.infoMedica = infoMedica
        self.numMaletasBodega = numMaletasBodega
        self.vuelo = []  # Lista para almacenar información de vuelos asignados al pasajero

    # Método para obtener el número de maletas del pasajero
    def getNumMaletas(self):
        return self.numMaletasBodega

    # Método para asignar un vuelo al pasajero
    def asignarVuelo(self, vuelo: Vuelos):
        # Obtiene la información del vuelo y la agrega a la lista de vuelos del pasajero
        p = vuelo.printVuelo()
        self.vuelo.append(p)

    # Método para convertir la información del pasajero a un diccionario
    def to_dict(self):
        return {
            "Nombre": self.nombre,
            "Apellido": self.apellido,
            "Edad": self.edad,
            "Cedula": self.cedula,
            "FechaNacimiento": self.fechaNacimiento,
            "Genero": self.genero,
            "Direccion": self.direccion,
            "Celular": self.numTel,
            "Correo": self.correo,
            "Nacionalidad": self.nacionalidad,
            "Info Medica": self.infoMedica,
            "Num MaletasBodega": self.numMaletasBodega
        }

    # Método para obtener la información de los vuelos asignados al pasajero
    def getInformacion(self):
        return self.vuelo
