# acumulador = 0
# seguir = "si"
# while seguir == "si":
#     numero = int(input("Ingrese un numero: "))
#     acumulador += numero

#     seguir = input("¿Desea continuar?\n")

# print(f"Valor acumulado: ", {acumulador})

#Esto simula un do while#
acumulador = 0

while True:
    numero = int(input("Ingrese un numero: "))
    acumulador += numero

    seguir = input("¿Desea continuar?\n")
    if seguir != "si":
        break

print(f"Valor acumulado: ", {acumulador})
#print("Valor acumulado: ", acumulador)#