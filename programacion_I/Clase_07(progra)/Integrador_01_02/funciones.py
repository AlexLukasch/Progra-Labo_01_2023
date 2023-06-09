def confirmar_continuar():
    input("Presione enter para continuar...\n")

def convertir_strings_numeros(lista:list):
    for heroe in lista:
        heroe['altura'] = float(heroe['altura'])
        heroe['peso'] = float(heroe['peso'])
        heroe['fuerza'] = int(heroe['fuerza'])

def mostrar_una_key(lista:list, key:str, mensaje_key_1:str):
    if(type(lista) == list and len(lista)>0):
        for heroe in lista:
            print(f"{mensaje_key_1}{heroe[key]}")

def mostrar_dos_keys(lista:list, key_1:str, key_2:str, mensaje_key_1:str, mensaje_key_2:str):
    if(type(lista) == list and len(lista)>0):
        for heroe in lista:
            print(f"{mensaje_key_1}{heroe[key_1]}")
            print(f"{mensaje_key_2}{heroe[key_2]}\n")

def buscar_maximo(lista:list, clave:str)->dict:
    if(type(lista) == list and len(lista)>0):
        flag_maximo = 0
        for heroe in lista:
            if(flag_maximo == 0 or heroe[clave] > max_altura):
                max_altura = heroe[clave]  
                flag_maximo = 1 
                mas_alto = heroe
        return mas_alto

def buscar_minimo(lista:list, clave:str)->dict:
    if(type(lista) == list and len(lista)>0):
        flag_minimo = 0
        for heroe in lista:
            if(flag_minimo == 0 or heroe[clave] < min_altura):
                min_altura = heroe[clave]
                flag_minimo = 1
                mas_bajo = heroe
        return mas_bajo

def mostrar_un_dato(diccionario:dict, clave:str, mensaje_clave:str):
    if(type(diccionario) == dict):
        dato = diccionario[clave]
        print(f"{mensaje_clave} {dato}")

def mostrar_dos_datos(diccionario:dict, clave_1:str, clave_2:str, mensaje_clave_1:str, mensaje_clave_2:str):
    if(type(diccionario) == dict):
        dato_1 = diccionario[clave_1]
        dato_2 = diccionario[clave_2]
        print(f"{mensaje_clave_1} {dato_1}")
        print(f"{mensaje_clave_2} {dato_2}\n")

def calcular_promemdio(lista:list, clave:str)->float:
    if(type(lista) == list and len(lista)>0):
        acumulador = 0
        contador = 0
        for i in range(len(lista)):
            acumulador = acumulador + lista[i][clave]
            contador = contador + 1
            
        promedio = acumulador / contador
        promedio = "{:.2f}".format(promedio)
        return promedio
#HASTA ACA LAS FUNCIONES DEL Integrador_01_00#

'''
Brief: Filtra una lista por un criterio
Parameters:
    lista -> lista sobre la que voy a hacer la busqueda
    key_criterio -> clave donde esta guardado el dato a comparar
    criterio -> criterio según el cual filtrar la lista
return: la lista filtrada por el criterio
'''
def filtrar_un_criterio(lista:list, key_criterio:str, criterio:str)->list:
    if(type(lista) == list and len(lista)>0):
        lista_filtrada = []
        for heroe in lista:
            if(heroe[key_criterio] == criterio):
                lista_filtrada.append(heroe)
    else:
        print("ERROR. La lista es inválida o esta vacía.\n")
    return lista_filtrada

def normalizar_letras_capitales(lista:list, clave:str):
    if(type(lista) == list and len(lista)>0):
        for elemento in lista:
            elemento[clave] = str.capitalize(elemento[clave])

def normalizar_claves_vacias(lista:list, clave:str, nueva_clave:str):
    if(type(lista) == list and len(lista)>0):
        for elemento in lista:
            if(elemento[clave] == ""):
                elemento[clave] = nueva_clave

def contar_elementos_por_clave(lista:list, clave: str)->dict:
    diccionario_elementos = {}
    for elemento in lista:
        if elemento[clave]  in diccionario_elementos:
            diccionario_elementos[elemento[clave]] += 1
        else:
            diccionario_elementos[elemento[clave]] = 1
    return diccionario_elementos

def guardar_elementos_por_clave(lista:list, clave: str)->dict:
    diccionario_elementos = {}
    for elemento in lista:
        if elemento[clave]  in diccionario_elementos:
            diccionario_elementos[elemento[clave]] += ", " + elemento["nombre"]
        else:
            diccionario_elementos[elemento[clave]] = elemento["nombre"]
    return diccionario_elementos

def mostrar_un_diccionario(diccionario:dict):
    if(type(diccionario) == dict):
        for elemento in diccionario:
            print(f"{elemento}: {diccionario[elemento]}")
#HASTA ACA LAS FUNCIONES DEL Integrador_01_01#

def stark_normalizar_datos(lista:list):
    if(type(lista) == list and len(lista)>0):
        bandera_cambios = 0
        for elemento in lista:
            if(type(elemento['altura']) != float):
                elemento['altura'] = float(elemento['altura'])
                bandera_cambios = 1
            if(type(elemento['peso']) != float):
                elemento['peso'] = float(elemento['peso'])  
                bandera_cambios = 1     
            if(type(elemento['fuerza']) != int):
                elemento['fuerza'] = int(elemento['fuerza'])
                bandera_cambios = 1
        if(bandera_cambios == 1):
            print("Datos normalizados.\n")
    else:
        print("Error: Lista de héroes vacía.\n")

def obtener_nombre(diccionario:dict)->str: #devuelve nombre formateado#
    pass
