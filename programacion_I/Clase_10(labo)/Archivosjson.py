import json
import re
# JSON #
# data = {} #creo un diccionario, y hardcodeo datos
# data["alumnos"] = []
# data["alumnos"].append({"nombre":"Juan", "edad":20})
# data["alumnos"].append({"nombre":"Luis", "edad":25})
# data["alumnos"].append({"nombre":"Maria", "edad":31})

# with open("D:\Programacion-Python\Progra-Labo_01_2023\programacion_I\Clase_10(labo)\agenda.json", "w") as mi_archivo:
#     json.dump(data, mi_archivo, indent = 4)

# with open("D:\Programacion-Python\Progra-Labo_01_2023\programacion_I\Clase_10(labo)\agenda.json", "r") as mi_archivo:
#     data = json.load(mi_archivo)
# print(data)

# PARSERS #


def parser_csv(path:str)->list:
    lista = []
    #contador = 0
    archivo = open(path, "r", encoding = "utf-8")
    for linea in archivo:
        #contador = contador + 1
        #print(f"ES LA ITERACIÓN: {contador}\n")
        lectura = re.split(",|\n", linea)
        tema = {}
        tema["title"] = lectura[0]
        tema["views"] = lectura[1]
        tema["length"] = lectura[2]
        tema["img_url"] = lectura[3]
        tema["url"] = lectura[4]
        tema["date"] = lectura[5]
        lista.append(tema)
    archivo.close()
    return lista

def parser2_csv(path:str)->list:
    lista = []

    archivo = open(path, "r", encoding = "utf-8")
    for line in archivo:
        lectura = re.split(",|\n", line)
        print(lectura)
    archivo.close()
    return lista

def generar_csv(path:str, lista:list):
    archivo = open(path,"w",encoding="utf-8")
    for tema in lista:
        registro = "{0},{1},{2},{3},{4},{5}\n"
        registro = registro.format(tema["title"],
                                   tema["views"],
                                   tema["length"],
                                   tema["img_url"],
                                   tema["url"],
                                   tema["date"])
        archivo.write(registro)
    archivo.close()


#lista = parser_csv("D:\Programacion-Python\Progra-Labo_01_2023\programacion_I\Clase_10(labo)\data.csv")
lista = parser2_csv("D:\Programacion-Python\Progra-Labo_01_2023\programacion_I\Clase_10(labo)\data.csv")

#generar_csv("D:\Programacion-Python\Progra-Labo_01_2023\programacion_I\Clase_10(labo)\lista_modificada.csv",lista)

print(lista)