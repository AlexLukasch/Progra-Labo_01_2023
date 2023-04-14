color = "gold"
#Esta forma es correcta pero a veces es mejor usar el elif#
if color == "azul":
    print("Es azul")
else:
    if color == "verde":
        print("Es verde")
    else:
        if color == "amarillo":
            print("Es amarillo")
        else:
            if color == "rojo":
                print("Es rojo")
            else:
                print("Es otro color")
#Usando el elif optimizo mejor el código y no tengo tanto anidamiento#
if color == "azul":
    print("Es azul")
elif color == "verde":
    print("Es verde")
elif color == "amarillo":
    print("Es amarillo")
elif color == "rojo":
    print("Es rojo")
else:
    print("Es otro color")
