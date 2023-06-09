# mi_archivo = open("D:\Programacion-Python\Progra-Labo_01_2023\programacion_I\Clase_10(labo)\archivo.txt", "a", encoding="utf-8")
# mi_archivo.write("lukasch\n")
# mi_archivo.close()

# mi_archivo = open("D:\Programacion-Python\Progra-Labo_01_2023\programacion_I\Clase_10(labo)\archivo.txt", "r", encoding="utf-8")
# registro = mi_archivo.read()
# print(registro)
# mi_archivo.close()

# lista = ["Thiago", "Gio", "Marian", "Mario"]
# with open("D:\Programacion-Python\Progra-Labo_01_2023\programacion_I\Clase_10(labo)\lista_nombres.txt", "w", encoding="utf-8") as mi_archivo:
#     for nombre in lista:
#         mi_archivo.write(f"{nombre}\n")

# mi_archivo = open("D:\Programacion-Python\Progra-Labo_01_2023\programacion_I\Clase_10(labo)\lista_nombres.txt","r")
# lista = mi_archivo.read()
# lista = mi_archivo.readlines()
# print(lista)
# for line in lista:
#     print(line, end="")
    
with open("lista_nombres.txt", "r", encoding="utf-8") as mi_archivo:
    for line in mi_archivo:
        print(line, end="")
mi_archivo.close()