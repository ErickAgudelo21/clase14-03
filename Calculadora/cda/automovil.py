class ColasVehiculo: 
    
    def agregar_vehiculo(self, marca: str, modelo: str, anio: int, tipo: str):
        vehiculo = None
        if tipo == "Motocicleta":
            vehiculo = Motocicleta(marca, modelo, anio)
        elif tipo == "Automovil":
            vehiculo = Automovil(marca, modelo, anio)

        # poner su logica maravillosa

    def despachar_vehiculo(self):
        # poner su logica maravillosa
        pass

    def mostrar_vehiculos(self):
        # poner su logica maravillosa
        pass



  