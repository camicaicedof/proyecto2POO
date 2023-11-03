from abc import ABC, abstractmethod


class MediadorTrafico():

    def registrar_aeronave(self, aeronave):
        pass

    def enviar_mensaje(self, mensaje, emisor):
        pass

    def asignar_puerta_de_embarque(self, aeronave, puerta, cod, hora):
        pass
