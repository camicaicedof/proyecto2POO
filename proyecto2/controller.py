from aeropuerto import Aeropuerto
from vuelos import Vuelos
from avion import Avion
from jet import JetPrivado
from helicoptero import Helicoptero
from tripulante import Tripulante
from pasajero import Pasajero
from view import AeropuertoView

class AeropuertoController:
    def __init__(self, aeropuerto):
        self.aeropuerto = aeropuerto
        self.aeropuerto_view = AeropuertoView()

    def ejecutar(self):
        num = 0
        flag = True
        self.aeropuerto_view.mostrar_linea()

        while flag:
            self.aeropuerto_view.mostrar_menu_principal()
            cases = self.aeropuerto_view.input_entero("Seleccione una opción: ")
            self.aeropuerto_view.mostrar_linea()

            if cases == 1:
                flag2 = True
                self.agregar_vuelos()
            elif cases == 2:
                self.agregar_naves()
            elif cases == 3:
                self.aeropuerto.asignarVuelo()
                self.aeropuerto.torreControl.simulacion()
                print("Deseas continuar?\n1. Si\n")
                npas = input()
            elif cases == 4:
                if self.aeropuerto.disponibilidadVuelos():
                    self.reserva()
                else:
                    print("No hay vuelos")
            elif cases == 5:
                self.aeropuerto_view.mostrar_linea()
                flag2 = True
                while flag2:
                    num = self.aeropuerto_view.input_entero("1. Consultar Vuelos\n2. Consultar Puertas\n3. Consultar Aeronaves\n4. Salir: ")
                    if num == 1:
                        print("Destinos:")
                        self.aeropuerto.printDestinos()
                    elif num == 2:
                        print("Puertas:")
                        self.aeropuerto.torreControl.mostrarPuertas()
                    elif num == 3:
                        print("Aviones:")
                        self.aeropuerto.torreControl.mostrarAviones()
                    else:
                        flag2 = False
                    self.aeropuerto_view.mostrar_linea()
            elif cases == 6:
                flag = False
            self.aeropuerto_view.mostrar_linea()

    def agregar_vuelos(self):
        print("Agregue vuelos")
        id = self.aeropuerto_view.input_entero("Ingrese la identificación del vuelo: ")
        fecha = self.aeropuerto_view.input_texto("Ingrese la fecha del vuelo (YYYY-MM-DD): ")
        ciudadDestino = self.aeropuerto_view.input_texto("Ingrese la ciudad de destino: ")
        hora = self.aeropuerto_view.input_texto("Ingrese la hora del vuelo (HH:MM): ")

        tmp = Vuelos(id, fecha, ciudadDestino, hora)
        self.aeropuerto.agregarDestino(tmp)
        salir = self.aeropuerto_view.input_entero("Salir?\n1. Si\n2. No: ")
        if salir == 1:
            flag2 = False

    def agregar_naves(self):
        flag2 = True
        while flag2:
            self.aeropuerto_view.mostrar_agregar_nave_menu()
            cases = self.aeropuerto_view.input_entero("Seleccione una opción: ")

            if cases == 4:
                print("Saliendo")
                break

            marca = self.aeropuerto_view.input_texto("Ingrese la marca de la aeronave: ")
            capacidad = self.aeropuerto_view.input_entero("Ingrese la capacidad de la aeronave: ")

            if cases == 1:
                avion = Avion(marca, capacidad, self.aeropuerto.torreControl)
                avion.obtenerDatos()
                self.aeropuerto.agregarAeronave(avion)
            elif cases == 2:
                jet = JetPrivado(marca, capacidad, self.aeropuerto.torreControl)
                jet.obtenerDatos()
                self.aeropuerto.agregarAeronave(jet)
            elif cases == 3:
                helicoptero = Helicoptero(
                    marca, capacidad, self.aeropuerto.torreControl)
                helicoptero.obtenerDatos()
                self.aeropuerto.agregarAeronave(helicoptero)
            else:
                print("Selección errónea, seleccione una opción válida...")

            num = self.aeropuerto_view.input_entero("Quieres añadir un tripulante?\n1. Si\n2. No: ")
            tripulantes = []

            while num == 1:
                tripulante = Tripulante(
                    "", "", 0, "", "", "", "", "", "", "", 0, 0)
                tripulante.crearTripulante()
                tripulantes.append(tripulante)
                num = self.aeropuerto_view.input_entero("Quieres añadir otro tripulante?\n1. Si\n2. No: ")

        self.aeropuerto.torreControl.mostrarAviones()

    def reserva(self):
        p = Pasajero("", "", 0, "", "", "", "", "", "", "", 0)
        pasajero = p.obtenerDatosPasajero()

        flag = True
        while flag:
            pasajero.getInformacion()
            s = self.aeropuerto_view.input_entero("Los datos son correctos?\n1. Si\n2. No: ")
            if s == 2:
                pasajero.obtenerDatosPasajero()
            else:
                flag = False

        print("Seleccione su vuelo")
        self.aeropuerto.printDestinos()
        selec = self.aeropuerto_view.input_entero("Ingrese el número del vuelo deseado: ")
        selec -= 1
        vuelo = self.aeropuerto.obtenerVuelo(selec)
        pasajero.asignarVuelo(vuelo)
        selec = self.aeropuerto_view.input_entero("El vuelo ha sido reservado, desea consultar?\n1. Si\n2. No: ")

        if selec == 1:
            vuelo.printVuelo()