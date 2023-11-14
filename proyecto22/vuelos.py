class Vuelos:
    def __init__(self, id, fecha, ciudad_destino, hora, aerolinea):
        # Atributos de la clase Vuelos
        self.identificacion = id
        self.capacidad = 10  # Puedes establecer la capacidad deseada
        self.num_pasajeros = 0
        self.fecha = fecha
        self.ciudad_origen = "Cali"
        self.ciudad_destino = ciudad_destino
        self.hora = hora
        self.tripulantes = []
        self.tr = []
        self.estado = True
        self.aerolinea = aerolinea

    def agregarPasajero(self):
        # Método para agregar un pasajero al vuelo si hay capacidad disponible
        if self.num_pasajeros < self.capacidad:
            self.num_pasajeros += 1
        else:
            self.estado = False

    def agregarTripulante(self, tripulantes, tr):
        # Método para agregar tripulantes al vuelo
        self.tripulantes = tripulantes
        self.tr = tr

    def printVuelo(self):
        # Método para imprimir la información del vuelo
        data = {
            "Aerolinea": self.aerolinea,
            "Ciudad de origen": self.ciudad_origen,
            "Ciudad de destino": self.ciudad_destino,
            "Fecha": self.fecha,
            "Hora": self.hora
        }
        if self.estado:
            data["Disponibilidad"] = "Disponible"
        else:
            data["Disponibilidad"] = "Vuelo lleno"
        return data

    def printTripulantes(self):
        # Método para imprimir la información de los tripulantes
        return self.tr

    def disponible(self):
        # Método para verificar la disponibilidad del vuelo
        return self.estado
