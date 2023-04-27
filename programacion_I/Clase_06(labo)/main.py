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