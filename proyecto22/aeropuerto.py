# Importa las clases necesarias
from torreControl import TorreControl
import streamlit as st
from vuelos import Vuelos 

class Aeropuerto:
    # Variable de clase para almacenar la única instancia del aeropuerto
    instancia = None

    def __init__(self):
        # Inicializa el estado del aeropuerto
        if 'vuelos' not in st.session_state:
            st.session_state['vuelos'] = {}
            self.vuelos = {}
        else:
            self.vuelos = st.session_state['vuelos']
            
        if 'torreDeControl' not in st.session_state:
            self.torreControl = TorreControl()
            st.session_state['torreDeControl'] = self.torreControl 
        else:
            self.torreControl = st.session_state['torreDeControl']

        if "aerolinea" not in st.session_state:
            st.session_state["aerolinea"]={}
            self.aerolinea={}
        else:
            self.aerolinea=st.session_state["aerolinea"]
        
        if "pasajeros" not in st.session_state:
            st.session_state["pasajeros"]={}
            self.pasajeros={}
        else:
            self.pasajeros=st.session_state["pasajeros"]
        
    @classmethod
    def obtenerInstancia(cls):
        # Método de clase para obtener la única instancia del aeropuerto
        if cls.instancia is None:
            cls.instancia = cls()
        return cls.instancia

    def agregarDestino(self, id, vuelo : Vuelos):
        # Método para agregar un destino (vuelo) al aeropuerto
        self.vuelos[id] = vuelo
        st.session_state['vuelos'] = self.vuelos

    def printDestinos(self):
        # Método para obtener la información de todos los destinos (vuelos) disponibles
        l = []
        for i in self.vuelos:
            l.append(self.vuelos[i].printVuelo())
        return l
    
    def printDestinosReserva(self):
        # Método para obtener la información de los destinos (vuelos) disponibles para reserva
        l = []
        for i in self.vuelos:
            if(self.vuelos[i].disponible()):
                l.append(self.vuelos[i].printVuelo())
        return l
    
    def printAerolineasVuelos(self):
        # Método para obtener la información de los vuelos de todas las aerolíneas
        d = {}
        for key in self.aerolinea:
            l = []
            for i in range(len(self.aerolinea[key].vuelos)):
                l.append(self.aerolinea[key].vuelos[i].printVuelo())
            d[key] = l
        return d
    
    def printPasajeros(self):
        # Método para obtener la información de todos los pasajeros
        l = []
        for i in self.pasajeros:
            l.append(self.pasajeros[i].to_dict())
        return l

    def disponibilidadVuelos(self):
        # Método para verificar la disponibilidad de vuelos
        return bool(self.vuelos)

    def disponibilidadAeronaves(self):
        # Método para verificar la disponibilidad de aeronaves en la torre de control
        return self.torreControl.disponibilidadNaves()
    
    def disponibilidadAerolineas(self):
        # Método para verificar la disponibilidad de aerolíneas
        return bool(self.aerolinea)

    def asignarVuelo(self):
        # Método para asignar vuelos a las aeronaves en la torre de control
        for vuelo in self.vuelos:
            self.torreControl.seleccionarAeronave(self.vuelos[vuelo])

    def obtenerVuelo(self, pos):
        # Método para obtener un vuelo específico
        return self.vuelos[pos]

    def agregarAeronave(self, id, nave):
        # Método para agregar una aeronave a la torre de control
        self.torreControl.aeronaves.append(nave)
        st.session_state["torreDeControl"] = self.torreControl

    def agregarAerolinea(self, nombre, aerolinea):
        # Método para agregar una aerolínea al aeropuerto
        self.aerolinea[nombre] = aerolinea
        st.session_state["aerolinea"] = self.aerolinea

    def agregarPasajero(self, pasajero, nombre):
        # Método para agregar un pasajero al aeropuerto
        self.pasajeros[nombre] = pasajero
        st.session_state["pasajeros"] = self.pasajeros

    def asignVueloAerolinea(self, nombre, vuelo):
        # Método para asignar un vuelo a una aerolínea específica
        self.aerolinea[nombre].agregarVuelo(vuelo)
