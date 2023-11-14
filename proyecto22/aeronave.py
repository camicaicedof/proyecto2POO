# Importa las clases necesarias
from mediadorTrafico import MediadorTrafico
from vuelos import Vuelos
import streamlit as st

class Aeronave:
    def __init__(self, id, marca, capacidad, mediator: MediadorTrafico, modelo, velMax, anoFab):
        # Constructor de la clase Aeronave, inicializa las propiedades de la aeronave
        self.id = id
        self.mediador = mediator
        self.puerta_de_embarque = ""
        self.marca = marca
        self.modelo = modelo
        self.velMax = velMax
        self.capacidad = capacidad
        self.anoFab = anoFab
        self.vuelos = [] 
        self.estado = True
        self.sillasDispo = 0
        self.tripulantes = []

    def printInfo(self):
        # Método para obtener información sobre la aeronave
        data = {
            "marca": self.marca,
            "capacidad": self.capacidad,
        }
        if self.estado:
            data["estado"] = "En servicio"
        else:
            data["estado"] = "Totalmente asignada"
        return data

    def enviarMensaje(self, mensaje):
        # Método para enviar un mensaje a través del mediador
        s = self.mediador.enviarMensaje(mensaje, self)
        return s

    def despegar(self):
        # Método para realizar la acción de despegar
        x = str(self.marca) + ": Despegando.,"
        x += (self.enviarMensaje(" Despegando " + str(self.marca)))
        return x

    def aterrizar(self):
        # Método para realizar la acción de aterrizar
        y = (str(self.marca) + " Aterrizando.,")
        y += self.enviarMensaje(" Aterrizando " + str(self.marca))
        return y

    def actualizarPosicion(self, mensaje):
        # Método para actualizar la posición de la aeronave
        z = str(self.marca) + ": Actualizando posición a " + mensaje + ","
        z += self.enviarMensaje(" Nueva posición: " + str(self.marca) + " " + mensaje)
        return z

    def recibirMensaje(self, mensaje):
        # Método para recibir un mensaje
        w = (str(self.marca) + " recibió mensaje: " + mensaje + ",")
        return w

    def asignarPuertaDeEmbarque(self, puerta, cod, hora):
        # Método para asignar una puerta de embarque a la aeronave
        y = str(self.marca) + " se dirige a la puerta de embarque: " + str(puerta) + " para el vuelo #" + str(cod) + " Hora: " + str(hora)
        st.write(y)

    def agregarVuelo(self, v: Vuelos):
        # Método para agregar un vuelo a la lista de vuelos de la aeronave
        flag = self.estado
        
        if len(self.vuelos) < 3 and flag:
            self.vuelos.append(v)
        else:
            self.estado = False
        if len(self.vuelos) == 3:
            self.estado = False

    def agregarTripulante(self, t):
        # Método para agregar un tripulante a la lista de tripulantes
        self.tripulantes.append(t)

    def eliminarVuelo(self):
        # Método para eliminar el último vuelo de la lista
        self.vuelos.pop()

    def tieneVuelos(self):
        # Método para verificar si la aeronave tiene vuelos asignados
        return len(self.vuelos) > 0

    def getCapacidad(self):
        # Método para obtener la capacidad de la aeronave
        return self.capacidad

    def setModelo(self, s):
        # Método para establecer el modelo de la aeronave
        self.modelo = s

    def setNombre(self, s):
        # Método para establecer el nombre de la aeronave (nota: el atributo 'nombre' no está definido en la clase)
        self.nombre = s

    def setAutonomia(self, i):
        # Método para establecer la autonomía de la aeronave (nota: el atributo 'autonom' no está definido en la clase)
        self.autonom