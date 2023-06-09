from Class_transporte import Transporte

class Auto (Transporte):
    def __init__(self, ruedas, marca, cantidad, velocidad):
        super().__init__(cantidad, velocidad)
        self._ruedas = ruedas
        self._marca = marca

    def avanzar(self, velocidad):
        print("El auto")
        super().avanzar(velocidad)

    def frenar(self):
        print("Esta frenando")
        super().frenar()

    def mostrar(self):
        print(f"Cantidad de ruedas: {self._ruedas} - Marca: {self._marca}")
        super().mostrar_velocidadmax_cantpasajeros()

