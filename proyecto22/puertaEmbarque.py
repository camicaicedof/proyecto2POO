# Definición de la clase PuertaEmbarque
class PuertaEmbarque:
    # Constructor de la clase, que inicializa los atributos
    def __init__(self, nombre):
        # Inicialización de los atributos con los valores proporcionados
        self.ident = nombre
        self.disponibilidad = True
        self.historial_vuelos = []

    # Método para anunciar el embarque en una puerta específica
    def anunciarEmbarque(self, puerta):
        print(f"Anuncio de embarque en {self.ident} - Puerta {puerta}")

    # Método para obtener la información de la puerta de embarque en formato de diccionario
    def to_dictPE(self):
        data = {
            "nombre": "Puerta #" + str(self.ident),
        }
        if self.disponibilidad:
            data["disponibilidad"] = "Disponible"
        else:
            data["disponibilidad"] = "No disponible"
        return data
