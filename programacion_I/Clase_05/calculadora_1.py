def sumar_numeros(primer_numero:int, segundo_numero:int)->int:
    suma = primer_numero + segundo_numero
    return suma
    
def restar_numeros(primer_numero:int, segundo_numero:int)->int:
    resta = primer_numero - segundo_numero
    return resta

def multiplicar_numeros(primer_numero:int, segundo_numero:int)->int:
    multiplicacion = primer_numero * segundo_numero
    return multiplicacion

def dividir_numeros(primer_numero:int, segundo_numero:int):
    division = None
    if segundo_numero != 0:
        division = primer_numero / segundo_numero
    return division

while True:
    opcion = int(input("1. Ingresar numeros\n"
                       "2. Sumar\n"
                       "3. Restar\n"
                       "4. Multiplicar\n"
                       "5. Dividir\n"
                       "6. Salir\n"))
    match opcion:
        case 1:
            x = int(input("Ingrese el primer numero: "))
            y = int(input("Ingrese el segundo numero: "))         
        case 2:
            suma = sumar_numeros(x,y)
            print(f"La suma es: {suma}")
        case 3:
            resta = restar_numeros(x,y)
            print(f"La resta es: {resta}")
        case 4:
            multiplicacion = multiplicar_numeros(x,y)
            print(f"La multiplicación es: {multiplicacion}")
        case 5:
            division = dividir_numeros(x,y)
            print(f"La división es: {division}")
        case 6:
            print("Saliendo del programa...\n")
            break