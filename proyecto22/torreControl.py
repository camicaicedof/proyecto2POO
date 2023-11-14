# Importación de módulos y clases necesarios
from mediadorTrafico import MediadorTrafico
from puertaEmbarque import PuertaEmbarque
from aeronave import Aeronave
from vuelos import Vuelos
import streamlit as st

# Definición de la clase TorreControl que hereda de MediadorTrafico
class TorreControl(MediadorTrafico):
    # Constructor de la clase TorreControl
    def __init__(self):
        # Inicialización de atributos: aeronaves, aviones, puertas y contador
        self.aeronaves = []
        self.aviones = []
        self.puertas = [PuertaEmbarque(i) for i in range(1, 7)]
        self.cont = 0

    # Método para registrar una aeronave en la torre de control
    def registrarAeronave(self, aeronave: Aeronave):
        self.aeronaves.append(aeronave)

    # Método para registrar un avión en la torre de control
    def registrarAvion(self, aeronave: Aeronave):
        self.aviones.append(aeronave)

    # Método para enviar mensajes a otras aeronaves
    def enviarMensaje(self, mensaje, emisor: Aeronave):
        s = ""
        for aeronave in self.aeronaves:
            if aeronave != emisor:
                s += aeronave.recibirMensaje(mensaje) + ","
        print(s)
        return s

    # Método para asignar puerta de embarque a una aeronave
    def asignarPuertaDeEmbarque(self, aeronave: Aeronave, puerta, cod, hora):
        aeronave.asignarPuertaDeEmbarque(puerta, cod, hora)
        self.puertas[puerta - 1].disponibilidad = False

    # Método para verificar la disponibilidad de naves en la torre de control
    def disponibilidadNaves(self):
        return bool(self.aeronaves)

    # Método para mostrar la información de las aeronaves
    def mostrarAeronaves(self):
        x = []
        for i in range(len(self.aeronaves)):
            x.append(self.aeronaves[i].printInfo())
        return x

    # Método para seleccionar una aeronave para un vuelo
    def seleccionarAeronave(self, vuelo: Vuelos):
        if self.cont == len(self.aeronaves):
            self.cont = 0
        for j in range(self.cont, len(self.aeronaves)):
            if self.aeronaves[j].estado:
                self.aeronaves[j].agregarVuelo(vuelo)
                flag = True
                for i in range(len(self.puertas)):
                    if self.puertas[i].disponibilidad:
                        self.asignarPuertaDeEmbarque(self.aeronaves[j], self.puertas[i].ident, vuelo.identificacion,
                                                    vuelo.hora)
                        flag = False
                        break
                break
        self.cont += 1

    # Método para realizar una simulación de vuelos
    def simulacion(self):
        def generarNumeroAleatorio():
            import random
            return random.randint(10000, 100000)

        lista2 = []

        for aeronave in self.aeronaves:
            if aeronave.tieneVuelos():
                for i in range(len(aeronave.vuelos)):
                    x = aeronave.despegar()
                    pos1 = generarNumeroAleatorio()
                    pos2 = generarNumeroAleatorio()
                    n = "Lat: " + str(pos1) + " Lon: " + str(pos2)
                    y = aeronave.actualizarPosicion(n)
                    z = aeronave.aterrizar()
                    lista = [x, y, z]
                    lista2.append(lista)

                for i in range(len(aeronave.vuelos)):
                    aeronave.eliminarVuelo()

        for puerta in self.puertas:
            puerta.disponibilidad = True
        return lista2

    # Método para mostrar la información de las puertas de embarque
    def mostrarPuertas(self):
        l = []
        for puerta in self.puertas:
            estado = "disponible" if puerta.disponibilidad else "no disponible"
            x = (f"Puerta #{puerta.identificacion} {estado}")
            l.append(x)
        return l

    # Método para obtener la información de las puertas de embarque en formato de lista de diccionarios
    def listPuertas(self):
        l = []
        for i in range(len(self.puertas)):
            l.append(self.puertas[i].to_dictPE())
        return l
