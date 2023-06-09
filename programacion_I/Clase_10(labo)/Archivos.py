# TEXTO #
# encoding="utf-8" argumento extra para caracteres especiales
#mi_archivo = open("D:\Programacion-Python\Progra-Labo_01_2023\programacion_I\Clase_10(labo)\nombre.txt", "w") #Sino pongo el modo, se abre en modo lectura por defecto#
#mi_archivo = open("D:\Programacion-Python\Progra-Labo_01_2023\programacion_I\Clase_10(labo)\hola.txt", "w")
mi_archivo = open("D:\Programacion-Python\Progra-Labo_01_2023\programacion_I\Clase_10(labo)\hola.txt", "r")
#mi_archivo = open("D:\Programacion-Python\Progra-Labo_01_2023\programacion_I\Clase_10(labo)\nombre.txt")#Lo abre en read por defecto#
#mi_archivo.write("Este es un agregado de prueba")
registro = mi_archivo.readline()
print(registro)
mi_archivo.close()
