class Transporte:
    def __init__(self, cantidad, velocidad):
        self._cantidad_pasajeros = cantidad
        self._velocidad_maxima = velocidad
        self._km_totales = 0
        self._distancia_recorrida = 0

    def avanzar(self, velocidad):
        if velocidad <= self._velocidad_maxima:
            print("Esta avanzando")
            self._distancia_recorrida += velocidad
        else:
            print("//////////////////////////////////////")
            print("Atencion. Limite de velocidad superado")
            print("//////////////////////////////////////")

    def frenar(self):
        print("Esta frenando")

    def mostrar_velocidadmax_cantpasajeros(self):
        print(f"*****{type(self)}*****")
        print(f"Velocidad máxima:{self._velocidad_maxima} - Cantidad de pasajeros: {self._cantidad_pasajeros}\n"
              f"Destino: {self._km_totales} - Restan: {self.get_distancia()}")

    def set_km_totales(self, valor): #Faltan las validaciones
        self._km_totales = valor

    def get_distancia(self):
        return self._km_totales - self._distancia_recorrida