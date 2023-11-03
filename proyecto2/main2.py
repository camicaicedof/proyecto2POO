from controller import AeropuertoController
from aeropuerto import Aeropuerto
def main():
    aeropuerto= Aeropuerto()
    controller=AeropuertoController(aeropuerto)
    controller.ejecutar()

main()
