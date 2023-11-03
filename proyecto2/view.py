class AeropuertoView:
    def mostrar_menu_principal(self):
        print("Bienvenido\n1. Modificar vuelos\n2. Agregar naves\n3. Simular\n4. Reservar vuelo\n5. Consultar info\n6. Salir")

    def mostrar_agregar_nave_menu(self):
        print("Agregar:\n1. Avion\n2. Jet\n3. Helicoptero\n4. Salir")

    def mostrar_linea(self):
        print("===========================================================================================\n\n")

    def input_entero(self, mensaje):
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada no válida. Introduce un número entero.")
            return self.input_entero(mensaje)

    def input_texto(self, mensaje):
        return input(mensaje)
