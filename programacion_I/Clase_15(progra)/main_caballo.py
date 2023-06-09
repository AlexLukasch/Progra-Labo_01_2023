from Class_caballo import Caballo
from Class_auto import Auto

caballo_1 = Caballo("Alpino", "Marron", 2, 50)
caballo_1.set_km_totales(100 )

caballo_2 = Caballo("Potro Salvaje", "Negro", 4, 50)
caballo_2.set_km_totales(500)

auto_1 = Auto(4, "Chevrolet", 6, 200)
auto_1.set_km_totales(700)

# caballo_1.avanzar()
# caballo_1.mostrar()
# caballo_1.frenar()

caballo_1.avanzar(120)
caballo_2.avanzar(25)
auto_1.avanzar(120)

lista_transportes = [caballo_1, auto_1, caballo_2] #Como son todos transportes, los pongo en una lista

for t in lista_transportes:
    t.mostrar()#Polimorfismo