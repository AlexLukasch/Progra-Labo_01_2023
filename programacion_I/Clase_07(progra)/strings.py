# cadena = "     Hola mundo mundo  "
# print(cadena)
# cadena = cadena.strip()
# cadena = cadena.upper()
# cadena = cadena.lower()
# cadena = cadena.capitalize()#parecido a title#
# cadena = cadena.replace("mundo", "zzz", 1)#Puedo pasarle un numero para que reemplaze x cantidad de veces#

# cadena = "Python, Java, JavaScript, C#"
# lista_split = cadena.split(",")# ","-> caracter delimitador, lo que separa las cadenas
# print(lista_split)
# for lenguaje in lista_split:
#     print(lenguaje.strip())

separador = "/"
dia = "10"
mes = "9"
año = "2005"
fecha = separador.join([dia,mes,año])
print(fecha)

# print(fecha)

# cadena ="123"
# cadena = cadena.zfill(25)
# print(cadena)

# cadena = "hola1mundo"#isalphaNo toma caracteres especiales como alfabeticos#
# print(cadena.isalnum())

# cadena = "hola mundo"
# print(len(cadena))

# mi_cadena = "holalala"
# print(mi_cadena.count("la"))#Tambien funciona con numeros#

cadena = "holamundo"
print(cadena[:5])#DESDE:HASTA donde tomar una cadena#