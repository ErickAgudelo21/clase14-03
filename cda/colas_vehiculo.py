class ColasVehiculo:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, marca, modelo, anio, tipo):
        vehiculo = {
            "marca": marca,
            "modelo": modelo,
            "anio": anio,
            "tipo": tipo
        }
        self.vehiculos.append(vehiculo)