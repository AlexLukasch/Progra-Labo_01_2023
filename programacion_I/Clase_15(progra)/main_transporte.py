from Class_transporte import Transporte

un_transporte = Transporte(5, 20) #Llamo al constructor

un_transporte.avanzar()

#un_transporte.mostrar_velocidadmax_cantpasajeros()
print(f"Velocidad máxima:{un_transporte._velocidad_maxima} - Cantidad de pasajeros: {un_transporte._cantidad_pasajeros}")


un_transporte.frenar()
