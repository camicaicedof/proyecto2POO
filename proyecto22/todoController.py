
from todoView import TodoView
from aeropuerto import Aeropuerto
from jet import JetPrivado
from helicoptero import Helicoptero
from avion import Avion
from vuelos import Vuelos
from pasajero import Pasajero
from tripulante import Tripulante
from aerolinea import Aerolinea
import streamlit as st
import requests
import json


class TodoController:
    def __init__(self):
        self.aeropuerto = Aeropuerto()
        self.view = TodoView()
        if 'taskCount' not in st.session_state:
            st.session_state['taskCount'] = - 1
        if 'aeronavesC' not in st.session_state:
            st.session_state['aeronavesC'] = 0
        if 'pasajeroC' not in st.session_state:
            st.session_state['pasajeroC'] = 0
        if 'listaJets' not in st.session_state:
            st.session_state['listaJets'] = 0
        #if 'option' not in st.session_state:
        #    st.session_state['option'] = 'Ver todas las tareas'

    def showMenu(self):
        option = self.view.menu()
        st.session_state['option'] = option
        if option == "Modificar Vuelos":
            self.createNewVuelo()
        elif option == "Consultar información":
            self.showMenuConsulta()
        elif option == "Agregar Naves":
            self.showMenuAeronaves()
        elif option == "Simular":
            self.obtenerSimulacion()
        elif option == "Reservar vuelo":
            self.createNewPasajero()
        elif option == "Añadir aerolíneas":
            self.createNewAerolinea()
        elif option == "Consultar país":
            self.consultarPais()
        elif option == "Inicio":
            self.view.aeropuertoText()
        """elif option == 'Marcar una tarea como completada':
            self.checkTask()
        elif option == 'Eliminar una tarea':
            self.removeTask() """

    def showMenuConsulta(self):
        option =self.view.menuConsultar()
        st.session_state['opcionConsulta'] = option
        if option=="Vuelos":
            self.listAllVuelos()
        elif option=="Puertas de Embarque":
            self.listALlPuertas()
        elif option=="Aeronaves":
            self.listAllAeronaves()
        elif option == "Pasajeros":
            self.listAllPasajeros()
        elif option == "Reserva":
            self.listReserva()

    
    def showMenuAeronaves(self):
        option =self.view.menuNaves()
        st.session_state['opcionAvion'] = option
        if option=="Avión":
            self.createNewAvion()
        elif option=="Helicóptero":
            self.createNewHelicoptero()
        elif option=="Jet":
            self.createNewJet()
#-----------------------------------------------------------------------------------------------------#
    def increaseTaskCount(self):
        st.session_state['taskCount'] = st.session_state['taskCount'] + 1
        return st.session_state['taskCount']
    
    def increaseAeronavesCount(self):
        st.session_state['aeronavesC'] = st.session_state['aeronavesC'] + 1
        return st.session_state['aeronavesC']
    
    def increasePasajeroCount(self):
        st.session_state['pasajeroC'] = st.session_state['pasajeroC'] + 1
        return st.session_state['pasajeroC']

#-----------------------------------------------------------------------------------------------------#
    def createNewVuelo(self):
        flag=self.aeropuerto.disponibilidadAerolineas()

        data = self.view.addNewVuelo(flag,self.aeropuerto.aerolinea)
        if data:
            taskId = self.increaseTaskCount()
            newVuelo = Vuelos(data["id"], data["fecha"], data["ciudadDestino"], data["hora"], data["aerolinea"])
            l = data["tripulacion"]
            if len(l) > 0:
                tr = []
                for i in range(len(l)):
                    newTripulante = Tripulante(l[i]["Nombre"],l[i]["Apellido"],l[i]["Edad"],l[i]["Cedula"], l[i]["Fecha de Nacimiento"],l[i]["Genero"],l[i]["Direccion"],l[i]["Num Tel"],l[i]["Correo"],l[i]["Cargo"],l[i]["Experiencia"],l[i]["Horas diarias"])
                    tr.append(newTripulante)
                newVuelo.agregarTripulante(tr, l)
            self.aeropuerto.agregarDestino(taskId, newVuelo)
            if(data["aerolinea"]):
                self.aeropuerto.asignVueloAerolinea(data["aerolinea"], newVuelo)


    def createNewAvion(self):
        data = self.view.addNewAvion()
        if data:
            taskId = self.increaseAeronavesCount()
            newAvion = Avion(taskId, data["marca"], data["numPasajeros"], self.aeropuerto.torreControl, data["modelo"], data["velMax"], data["anoFab"], data["altitudMax"], data["numMotores"], data["categoria"] )
            self.aeropuerto.agregarAeronave(taskId, newAvion)

    def createNewJet(self):
        data = self.view.addNewJet()
        if data:
            taskId = self.increaseAeronavesCount()
            newJet = JetPrivado(taskId, data["marca"], data["numPasajeros"], self.aeropuerto.torreControl, data["modelo"], data["velMax"], data["anoFab"], data["propietario"], data["servicios"], data["destinos"] ) 
            self.aeropuerto.agregarAeronave(taskId, newJet)

    def createNewHelicoptero(self):
        data = self.view.addNewHelicoptero()
        if data:
            taskId = self.increaseAeronavesCount()
            newHelicoptero = Helicoptero(taskId, data["marca"], data["numPasajeros"], self.aeropuerto.torreControl, data["modelo"], data["velMax"], data["anoFab"], data["numRotores"], data["maxElevacion"], data["uso"] )
            self.aeropuerto.agregarAeronave(taskId, newHelicoptero)

    def createNewPasajero(self):
        dispo = self.aeropuerto.disponibilidadVuelos()
        allVuelos = self.aeropuerto.printDestinosReserva()
        d = self.view.addNewPasajero(dispo,allVuelos)
        if d:
            pasCount = self.increasePasajeroCount()
            newPasajero = Pasajero(d["nombre"], d["apellido"], d["edad"], d["cedula"], d["fechaNacimiento"], d["genero"], d["direccion"], d["numTel"], d["correo"], d["nacionalidad"], d["infoMedica"], d["numMaletasBodega"])
            newPasajero.asignarVuelo(self.aeropuerto.vuelos[int(d["selected_index"])])
            self.aeropuerto.agregarPasajero(newPasajero, d["nombre"])

    def createNewAerolinea(self):
        data=self.view.addNewAerolinea()
        if data:
            newAerolinea= Aerolinea(data["nombre"])
            self.aeropuerto.agregarAerolinea(data["nombre"],newAerolinea)
#-----------------------------------------------------------------------------------------------------#

    def listAllVuelosReserva(self):
        allVuelos = self.aeropuerto.printDestinosReserva()
        index = self.view.listAllVuelosReserva(allVuelos)
        return index

    def obtenerSimulacion(self):
        self.aeropuerto.asignarVuelo()
        l=self.aeropuerto.torreControl.simulacion()
        self.view.listAllSimulacion(l)

    def listAllVuelos(self):
        allVuelos = self.aeropuerto.printAerolineasVuelos()
        self.view.listAllVuelos(allVuelos)
    
    def listAllAeronaves(self):
        allNaves = self.aeropuerto.torreControl.mostrarAeronaves()
        self.view.listAllAeronave(allNaves)
    
    def listAllPasajeros(self):
        allPasajeros = self.aeropuerto.printPasajeros()
        self.view.listAllPasajero(allPasajeros)

    def listALlPuertas(self):
        allPuertas = self.aeropuerto.torreControl.listPuertas()
        self.view.listPuertas(allPuertas)

    def listReserva(self):
        nombre = self.view.askPasajero()
        if nombre:
            if nombre in self.aeropuerto.pasajeros:
                pasajero = self.aeropuerto.pasajeros[nombre]
                reserva = pasajero.getInformacion()
                self.view.listReserva(reserva)
            else:
                self.view.showErrorReserva()

    def getCountriesData(self,country : str):
        url = f"https://restcountries.com/v3.1/name/{country}"
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.text)
            return data
            #print(data[0]['name']['common'])
        else:
            return ("Error en la consulta de los datos")

    def getCountriesData2(self,data):
        d={}
        d["name"]=data[0]["name"]["official"]
        d["capital"]=data[0]["capital"]
        cur = ""
        i=0
        for key in data[0]["currencies"]:
            cur = key
            i+=1
            if i>=1:
                break
        d["currency"]=data[0]["currencies"][cur]["name"]
        d["region"]=data[0]["region"]
        d["population"]=data[0]["population"]
        d["flag"]=data[0]["flags"]["png"]
        return d
    
    def consultarPais(self):
        x=self.getCountriesData(self.view.askCountry())
        if x!="Error en la consulta de los datos":
            d=self.getCountriesData2(x)
            self.view.listCountries(d)
