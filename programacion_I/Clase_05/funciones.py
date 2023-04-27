def sumar_numeros()->None:#Implementacion de la funcion
    primer_numero = int(input("Ingrese el primer numero: "))
    segundo_numero = int(input("Ingrese el segundo numero: "))
    suma = primer_numero + segundo_numero
    print(f"La suma es: {suma}")

def restar_numeros()->int:#Lo adecuado es decir que va a retornar
    primer_numero = int(input("Ingrese el primer numero: "))
    segundo_numero = int(input("Ingrese el segundo numero: "))
    resta = primer_numero - segundo_numero

    return resta

def multiplicar_numeros(primer_numero:int, segundo_numero:int):#Parametros formales
    retorno = primer_numero * segundo_numero
    return retorno

#sumar_numeros()#Llamada a la funcion
resultado_resta = restar_numeros()
print(f"El resultado de la resta es: {resultado_resta}")
resultado_mult = multiplicar_numeros(5,6)#Parametros actuales
print(f"El resultado de la multiplicación es: {resultado_mult}")