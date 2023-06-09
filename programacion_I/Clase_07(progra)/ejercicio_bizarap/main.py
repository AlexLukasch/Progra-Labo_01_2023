from data import lista_bzrp
from os import system

# {
#     'title': 'QUEVEDO || BZRP Music Sessions #52',
#     'views': 227192970,
#     'length': 204,
#     'img_url': 'https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg',
#     'url': 'https://youtube.com/watch?v=A_g3lMcWVy0',
#     'date': '2022-07-06 00:00:00'
# }

# 'QUEVEDO || BZRP Music Sessions #52'

def prueba():
    titulo = 'QUEVEDO || BZRP Music Sessions #52'
    cadena = titulo.split("||")
    artista = cadena[0].strip()
    cadena2 = cadena[1].split("#")
    tipo = cadena2[0].strip()
    numero = cadena2[1].strip()
    print(f"{artista} - {tipo} - {numero}")

def prueba2(titulo:str):
    cadena = titulo.split("||")
    artista = cadena[0].strip()
    cadena2 = cadena[1].split("#")
    tipo = cadena2[0].strip()
    numero = cadena2[1].strip()
    print(f"{artista} - {tipo} - {numero}")

def prueba3(titulo:str):
    cadena = titulo.split("||")
    if(len(cadena)>1):
        artista = cadena[0].strip()
        cadena2 = cadena[1].split("#")
        if(len(cadena2)>1):
            tipo = cadena2[0].strip()
            numero = cadena2[1].strip()
            print(f"{artista} - {tipo} - {numero}")

# 'QUEVEDO || BZRP Music Sessions #52'
def prueba4(titulo:str):
    tipo = "BZRP Music Sessions"
    parte1 = titulo.split(tipo)
    if(len(parte1)==2):
        artista = parte1[0].replace("||","").strip()
        numero = parte1[1].replace("#","").strip()
        print(f"{artista} - {tipo} - {numero}")

# 'https://youtube.com/watch?v=A_g3lMcWVy0'
def url(tema:dict):
    # cadena = tema["url"].split("=")
    # print(cadena[1])
    #////OTRA FORMA DE HACERLO////#
    # codigo = tema["url"].replace("https://youtube.com/watch?v=","")
    # print(codigo)
    #////OTRA FORMA DE HACERLO////#
    # l = len("https://youtube.com/watch?v=")
    # url = tema["url"]
    # codigo = url[l:]
    # print(codigo)
    #////OTRA FORMA DE HACERLO////#
    url = tema["url"]
    indice = url.index("=")
    codigo = url[indice+1:]
    print(codigo)

# date': '2022-07-06 00:00:00
def formatear_fecha(fecha_cadena:str)->int:
    fecha_split = fecha_cadena.split(" ")
    fecha = fecha_split[0].split("-")
    año = fecha[0]
    mes = fecha[1]
    dia = fecha[2]
    separador = "/"
    fecha_formato = separador.join([dia,mes,año])
    return fecha_formato

def test(lista:list):
    for tema in lista:
        #prueba4(tema["title"])
        #url(tema)
        fecha = formatear_fecha(tema["date"])
        print(fecha)

'''
Brief: Calcula el maximo valor numerico en base a una clave
Parameters:
    lista -> lista sobre la que voy a hacer la busqueda
    clave -> la clave con la cual realizo la busqueda en la lista
return: un entero que representa el valor maximo de la clave
'''
def calcular_maximo(lista:list, clave:str)->int:
    flag_primero = True
    maximo = 0
    if(type(lista) == list and len(lista)>0 and type(clave) == str and len(clave) > 0):

        for tema in lista:
            if flag_primero == True or tema [clave] > maximo:
                maximo = tema[clave]
                flag_primero = False

    return maximo 

test(lista_bzrp)