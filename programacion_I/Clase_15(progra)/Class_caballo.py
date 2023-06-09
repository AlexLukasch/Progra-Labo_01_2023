from Class_transporte import Transporte

class Caballo (Transporte):
    def __init__(self, raza, color, cantidad, velocidad):
        super().__init__(cantidad, velocidad)#Heredo los atributos de la clase base o Transporte
        self._raza = raza
        self._color = color

    def frenar(self): #Redefino el metodo frenar para la clase caballo
        print("El caballo")
        super().frenar()

    def avanzar(self, velocidad): #Redefino el metodo avanzar heredado de la clase transporte
        print("El caballo")
        super().avanzar(velocidad)

    def mostrar(self):
        print(f"Raza: {self._raza} - Color: {self._color}")
        super().mostrar_velocidadmax_cantpasajeros()
