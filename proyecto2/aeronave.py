""" from mediadorTrafico import MediadorTrafico
from vuelos import Vuelos
from tripulante import Tripulante
 """


class Aeronave:
    def __init__(self, marca, capacidad, mediator):
        self.mediador = mediator
        self.puerta_de_embarque = ""
        self.marca = marca
        self.modelo = "2019"
        self.capacidad = capacidad
        self.vuelos = []
        self.estado = True
        self.sillasDispo = 0
        self.tripulantes = []

    def enviarMensaje(self, mensaje):
        self.mediador.enviarMensaje(mensaje, self)

    def despegar(self):
        x=(f"{self.marca}: Despegando.")
        self.enviarMensaje(f"Despegando {self.marca}")
        return x

    def aterrizar(self):
        y=(f"{self.marca}: Aterrizando.")
        self.enviarMensaje(f"Aterrizando {self.marca}")
        return y
    
    def actualizarPosicion(self, mensaje):
        z=(f"{self.marca}: Actualizando posición a {mensaje}")
        self.enviarMensaje(f"Nueva posición: {self.marca} {mensaje}")
        return z
    
    def recibirMensaje(self, mensaje):
        w=(f"{self.marca} recibió mensaje: {mensaje}")
        return w
    
    def asignarPuertaDeEmbarque(self, puerta, cod, hora):
        print(f"{self.marca} se dirige a la puerta de embarque: {puerta} para el vuelo #{cod} Hora: {hora}")

    def agregarVuelo(self, v):
        flag = self.estado
        for vuelo in self.vuelos:
            if v.identificacion == vuelo.identificacion:
                flag = False
        if len(self.vuelos) < 3 and flag:
            self.vuelos.append(v)
        else:
            self.estado = False
        if len(self.vuelos) == 3:
            self.estado = False

    def agregarTripulante(self, t):
        self.tripulantes.append(t)

    def printInfo(self):
        x=(f"Marca: {self.marca}")
        y=(f"Capacidad: {self.capacidad}")
        return [x,y]

    def eliminarVuelo(self):
        self.vuelos.pop()

    def tieneVuelos(self):
        return len(self.vuelos) > 0

    def getCapacidad(self):
        return self.capacidad

    def setModelo(self, s):
        self.modelo = s

    def setNombre(self, s):
        self.nombre = s

    def setAutonomia(self, i):
        self.autonom
