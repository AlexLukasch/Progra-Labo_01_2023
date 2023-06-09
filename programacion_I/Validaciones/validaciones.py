def es_numerica(input:str)->bool:
    retorno = False
    if(input.isdigit() == True) or ((input.startswith('-') and input[1:].isdigit())):
        retorno = True
    return retorno

#SOLO VALIDA ENTEROS Y EXPONENTES#
def get_int(mensaje:str, mensaje_error:str)->int:
    entrada = input(mensaje)
    while es_numerica(entrada) == False:
        entrada = input(mensaje_error)
    return int(entrada)


