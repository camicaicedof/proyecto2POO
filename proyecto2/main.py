from aeropuerto import Aeropuerto
from vuelos import Vuelos
from avion import Avion
from jet import JetPrivado
from helicoptero import Helicoptero
from tripulante import Tripulante
from pasajero import Pasajero


def agregarNaves(aeropuerto: Aeropuerto):

    flag2 = True
    while flag2:
        tr = True
        print("Agregar:\n1. Avion\n2. Jet\n3. Helicoptero\n4. Salir")
        cases = int(input())

        if cases == 4:
            print("Saliendo")
            break

        print("Ingrese la marca de la aeronave:")
        marca = input()
        print("Ingrese la capacidad de la aeronave:")
        capacidad = int(input())

        if cases == 1:
            avion = Avion(marca, capacidad, aeropuerto.torreControl)
            avion.obtenerDatos()
            aeropuerto.agregarAeronave(avion)
        elif cases == 2:
            jet = JetPrivado(marca, capacidad, aeropuerto.torreControl)
            jet.obtenerDatos()
            aeropuerto.agregarAeronave(jet)
        elif cases == 3:
            helicoptero = Helicoptero(
                marca, capacidad, aeropuerto.torreControl)
            helicoptero.obtenerDatos()
            aeropuerto.agregarAeronave(helicoptero)

        else:
            print("Selección errónea, seleccione una opción válida...")

        print("Quieres añadir un tripulante?\n1. Si\n2. No")
        num = int(input())
        tripulantes = []

        while tr and num == 1:
            tripulante = Tripulante(
                "", "", 0, "", "", "", "", "", "", "", 0, 0)
            tripulante.crearTripulante()
            tripulantes.append(tripulante)
            print("Quieres añadir otro tripulante?\n1. Si\n2. No")
            num = int(input())
            if num != 1:
                tr = False

        """ for nave in naves:
            for tripulante in tripulantes:
                nave.agregarTripulante(tripulante) """

        aeropuerto.torreControl.mostrarAviones()

        printLinea()


def reserva(aeropuerto: Aeropuerto):
    p = Pasajero("", "", 0, "", "", "", "", "", "", "", 0)
    pasajero = p.obtenerDatosPasajero()

    flag = True
    while flag:
        pasajero.getInformacion()
        print("Los datos son correctos?\n1. Si\n2. No")
        s = int(input())
        if s == 2:
            pasajero.obtenerDatosPasajero()
        else:
            flag = False

    print("Seleccione su vuelo")
    aeropuerto.printDestinos()
    selec = int(input())
    selec -= 1
    vuelo = aeropuerto.obtenerVuelo(selec)
    pasajero.asignarVuelo(vuelo)
    print("El vuelo ha sido reservado, desea consultar?\n1. Si\n2. No")
    selec = int(input())

    if selec == 1:
        vuelo.printVuelo()


def printLinea():
    print("===========================================================================================\n\n")


if __name__ == "__main__":
    aeropuerto = Aeropuerto()
    num = 0
    flag = True
    printLinea()

    while flag:
        print("Bienvenido\n1. Modificar vuelos\n2. Agregar naves\n3. Simular\n4. Reservar vuelo\n5. Consultar info\n6. Salir")
        cases = int(input())
        print()

        if cases == 1:
            flag2 = True
            while flag2:
                print("Agregue vuelos")
                id = 0
                fecha = ""
                ciudadOrigen = "Ciudad de Origen"
                ciudadDestino = ""
                hora = ""
                ej = ""

                try:
                    print("Ingrese la identificación del vuelo:")
                    ej = input()
                    id = int(ej)
                except ValueError as e:
                    print("Error: Argumento inválido,",
                          e, "Ingrese un número entero")
                    id = int(input())

                print("Ingrese la fecha del vuelo (YYYY-MM-DD):")
                fecha = input()

                print("Ingrese la ciudad de destino:")
                ciudadDestino = input()

                print("Ingrese la hora del vuelo (HH:MM):")
                hora = input()

                tmp = Vuelos(id, fecha, ciudadDestino, hora)
                aeropuerto.agregarDestino(tmp)
                print("Salir?\n1. Si\n2. No")
                num = int(input())

                if num == 1:
                    flag2 = False
        elif cases == 2:
            agregarNaves(aeropuerto)
        elif cases == 3:
            aeropuerto.asignarVuelo()
            aeropuerto.torreControl.simulacion()
            print("Deseas continuar?\n1. Si\n")
            npas = input()
        elif cases == 4:
            if aeropuerto.disponibilidadVuelos():
                reserva(aeropuerto)
            else:
                print("No hay vuelos")
        elif cases == 5:
            printLinea()
            flag2 = True
            while flag2:
                print(
                    "1. Consultar Vuelos\n2. Consultar Puertas\n3. Consultar Aeronaves\n4. Salir")
                num = int(input())
                if num == 1:
                    print("Destinos:")
                    aeropuerto.printDestinos()
                elif num == 2:
                    print("Puertas:")
                    aeropuerto.torreControl.mostrarPuertas()
                elif num == 3:
                    print("Aviones:")
                    aeropuerto.torreControl.mostrarAviones()
                else:
                    flag2 = False
                printLinea()
        else:
            flag = False
        printLinea()
