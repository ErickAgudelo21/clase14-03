from .nodo import Nodo
from .vehiculo import Vehiculo
from .automovil import Automovil
from .motocicleta import Motocicleta


class ColasVehiculo:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar_vehiculo(self, marca: str, modelo: str, anio: int, tipo: str):
        vehiculo = None
        if tipo == "Motocicleta":
            vehiculo = Motocicleta(marca, modelo, anio)
        elif tipo == "Automovil":
            vehiculo = Automovil(marca, modelo, anio)

        if vehiculo:
            nodo = Nodo(vehiculo)
            if self.cabeza is None:
                self.cabeza = nodo
                self.cola = nodo
            else:
                self.cola.siguiente = nodo
                self.cola = nodo

    def despachar_vehiculo(self):
        if self.cabeza is None:
            return None
        
        vehiculo = self.cabeza.datos
        self.cabeza = self.cabeza.siguiente
        
        if self.cabeza is None:
            self.cola = None
        
        return vehiculo

    def mostrar_vehiculos(self):
        vehiculos_info = []
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            vehiculos_info.append(nodo_actual.datos.mostrar_informacion())
            nodo_actual = nodo_actual.siguiente
        return vehiculos_info
