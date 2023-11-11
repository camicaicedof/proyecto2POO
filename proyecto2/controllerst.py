from aeropuerto import Aeropuerto
from vuelos import Vuelos
from avion import Avion
from jet import JetPrivado
from helicoptero import Helicoptero
from tripulante import Tripulante
from pasajero import Pasajero
from view import AeropuertoView
import streamlit as st

class AeropuertoController:
    def __init__(self,aeropuerto):
        self.aeropuerto=aeropuerto
        self.aeropuerto_view = AeropuertoView()
    
    def ejecutar(self):
        num=0
        flag=True
        #Vista(?)
        rad=st.sidebar.radio("Opciones",["Inicio","Modificar Vuelos","Agregar Naves","Simular","Reservar vuelo","Consultar información"])
        #fin
        if rad=="Inicio":
            st.title("Aeropuerto Alfonso Bonilla")
            st.header("Bienvenido")
        if rad=="Modificar Vuelos":
            self.agregar_vuelos()
        elif rad=="Agregar Naves":
            self.agregar_naves()
        elif rad=="Simular":
            self.aeropuerto.asignarVuelo()
            l=self.aeropuerto.torreControl.simulacion()
            st.header("Simulación")
            if len(l)==0:
                st.text("No hay vuelos disponibles para simulación")
            else:
                for i in range(0,len(l),1):
                    for j in range (0,len(l[i])):
                        st.text(l[i][j])
        elif rad=="Reservar vuelo":
            if self.aeropuerto.disponibilidadVuelos():
                self.reserva()
            else:
                st.text("No hay vuelos")

        elif rad=="Consultar información":
            selec=st.selectbox("Opciones",["Vuelos","Puertas","Aeronaves"])
            if selec=="Vuelos":
                st.header("Destinos")
                x=self.aeropuerto.printDestinos()
                if len(x)==1:
                    st.text(x[0])
                else:
                    for i in range (0,len(x),1):
                        for j in range (0,len(x[i]),1):
                            st.text(x[i][j])
            elif selec=="Puertas":
                st.header("Puertas")
                y=self.aeropuerto.torreControl.mostrarPuertas()
                for i in range (0,len(y),1):
                    st.text(y[i])
            elif selec=="Aeronaves":
                st.header("Aviones")
                z=self.aeropuerto.torreControl.mostrarAviones()
                for i in range (0,len(z),1):
                    st.text(z[i])

    def agregar_vuelos (self):
        st.header("Agregue un vuelo")
        id=st.text_input("Ingrese la identificación del vuelo:",value="")
        fecha=st.text_input("Ingrese la fecha del vuelo (YYYY-MM-DD):",value="")
        ciudadDestino=st.text_input("Ingrese la ciudad de destino:",value="")
        hora = st.text_input("Ingrese la hora del vuelo (Hs:Ms):",value="")
        if st.button("Guardar"):
            tmp = Vuelos(id, fecha, ciudadDestino, hora)
            self.aeropuerto.agregarDestino(tmp)
            st.text("Vuelo agregado exitosamente")
            #TEMPORAL
            st.text(id)
            st.text(fecha)
            st.text(ciudadDestino)
            st.text(hora)

    def agregar_naves (self):
        #tmp
        st.text("AGREGAR NAVES")
    def reserva(self):
        #tmp
        st.text("RESERVA")
    




def main():
    aeropuerto= Aeropuerto()
    controller=AeropuertoController(aeropuerto)
    controller.ejecutar()

main()