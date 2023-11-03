from mediadorTrafico import MediadorTrafico
from puertaEmbarque import PuertaEmbarque
from aeronave import Aeronave


class TorreControl(MediadorTrafico):
    def __init__(self):
        self.aeronaves = []
        self.aviones = []
        self.puertas = [PuertaEmbarque(i) for i in range(1, 7)]
        self.cont = 0

    def registrarAeronave(self, aeronave: Aeronave):
        self.aeronaves.append(aeronave)

    def registrarAvion(self, aeronave: Aeronave):
        self.aviones.append(aeronave)

    def enviarMensaje(self, mensaje, emisor: Aeronave):
        for aeronave in self.aeronaves:
            if aeronave != emisor:
                aeronave.recibirMensaje(mensaje)

    def asignarPuertaDeEmbarque(self, aeronave: Aeronave, puerta, cod, hora):
        aeronave.asignarPuertaDeEmbarque(puerta, cod, hora)
        self.puertas[puerta - 1].disponibilidad = False

    def disponibilidadNaves(self):
        return bool(self.aeronaves)

    def mostrarAviones(self):
        if not self.aeronaves:
            print("No hay aeronaves")
        for i, aeronave in enumerate(self.aeronaves, 1):
            print(f"{i}.")
            aeronave.printInfo()

    def seleccionarAeronave(self, vuelo):
        if self.cont == len(self.aeronaves):
            self.cont = 0
        for j in range(self.cont, len(self.aeronaves)):
            if self.aeronaves[j].estado:
                self.aeronaves[j].agregarVuelo(vuelo)
                flag = True
                for i in range(len(self.puertas)):
                    if self.puertas[i].disponibilidad:
                        self.asignarPuertaDeEmbarque(
                            self.aeronaves[j], self.puertas[i].identificacion, vuelo.identificacion, vuelo.hora)
                        flag = False
                        break
                break
        self.cont += 1

    def simulacion(self):
        def generarNumeroAleatorio():
            import random
            return random.randint(10000, 100000)

        for aeronave in self.aeronaves:
            if aeronave.tieneVuelos():
                for i in range(len(aeronave.vuelos)):
                    aeronave.despegar()
                    pos1 = generarNumeroAleatorio()
                    pos2 = generarNumeroAleatorio()
                    n = "Lat: " + str(pos1) + " Lon: " + str(pos2)
                    aeronave.actualizarPosicion(n)
                    aeronave.aterrizar()
                for i in range(len(aeronave.vuelos)):
                    aeronave.eliminarVuelo()

        for puerta in self.puertas:
            puerta.disponibilidad = True

    def mostrarPuertas(self):
        for puerta in self.puertas:
            estado = "disponible" if puerta.disponibilidad else "no disponible"
            print(f"Puerta #{puerta.identificacion} {estado}")
