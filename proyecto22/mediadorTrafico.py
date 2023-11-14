from abc import ABC, abstractmethod

class MediadorTrafico(ABC):
    # La clase MediadorTrafico es una clase abstracta (ABC) que define una interfaz para los mediadores de tráfico.

    @abstractmethod
    def registrarAeronave(self, aeronave):
        # Método abstracto para registrar una aeronave en el mediador de tráfico.
        pass

    @abstractmethod
    def enviarMensaje(self, mensaje, emisor):
        # Método abstracto para enviar un mensaje a través del mediador de tráfico desde un emisor.
        pass

    @abstractmethod
    def asignarPuertaDeEmbarque(self, aeronave, puerta, cod, hora):
        # Método abstracto para asignar una puerta de embarque a una aeronave para un vuelo específico.
        pass
