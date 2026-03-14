class Vehiculo:
    def __init__(self, marca: str, modelo: str, anio: int):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def mostrar_informacion(self) -> str:  
        return f"{self.marca} {self.modelo} ({self.anio})"   
