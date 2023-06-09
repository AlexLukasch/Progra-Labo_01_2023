import re
# CSV #
# nombres = ["Thiago","Gio","Marian"]
# apellidos = ["Mejias","Lucchetta","Fernandez"]
# edades = [21,23,24]
# TAM = 3
# with open("D:\Programacion-Python\Progra-Labo_01_2023\programacion_I\Clase_10(labo)\agenda.csv","w") as archivo:
#     for i in range(TAM):
#         registro = "{0},{1},{2}\n".format(nombres[i],apellidos[i],edades[i])
#         archivo.write(registro)

with open("D:\Programacion-Python\Progra-Labo_01_2023\programacion_I\Clase_10(labo)\agenda.csv","r") as archivo: #El with cierra el archivo solo#
    for line in archivo:
        #registro = line.split(",")
        registro = re.split(r",|\n",line)
        print(f"{registro[0]} - {registro[1]} - {registro[2]}")    

