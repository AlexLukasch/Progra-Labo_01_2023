'''
[] Conjunto de caracteres
\
.
flecha arriba Empieza con 
$ Termina con
*
+ Una o más ocurrencias
?
{}
| Una o la otra
()
'''
import re # regular expresions

# SPLIT #
#print(re.split(" ", "Hola mundo 1B"))
#print(re.split("[a-z]+", "Hola mundo 1B"))
#print(re.split("[a-z]+", "Hola mundo 1B"))
#print(re.split("Hola|chau", "Hola mundo 1B"))
#print(re.split("[a-z]|[0-9 ]", "Hola mundo @@ 1234 chau"))

# SEARCH #
#print(re.search(" ", "hola como estan?").span()) #Devuelve none sino encuentra la expresión
#print(re.search(" ", "hola como estan?").start())
#print(re.search(" ", "hola como estan?").end())
#print(re.search("[0-9]", "texto con numeros: 123 y letras: aaa"))
#print(re.search("[0-9]+", "texto con numeros: 123 y letras: aaa").group())

# FINDALL #
#texto = "Uno 1 Dos 2 Tres 3 Cuatro 44"
#print(re.findall(" ", texto))
#print(re.findall("[0-9]+", texto))
#print(re.findall("[a-zA-Z]{6}", texto))
#print(re.findall("[a-zA-Z]{3,6}", texto))

# SUB # para reemplazar con un rango ejemplo a-z
#texto = "abc ABC ccc ddd  abc aaa"
#result = re.sub("abc", "reemplazo", texto)
#print(result)
#print(texto)
#result = re.sub("\\s+", " ", texto) #si uso r no uso \
#result = re.sub(r"\s\s", "**", texto)
#print(result)

###################### BIZARRAP ######################

#texto = "QUEVEDO || BZRP Music Sessions #52"

#print(re.findall("[A-Za-z]+", texto))
#print(re.split(" \|{2} ", texto)) #Uso el \|{2} para tomar solo 2 barras con un espacio delante y detras
#print(re.split("[\|#]+", texto))

fecha = "2022-02-03 19:20:33"

#fechahora = print(re.findall("[0-9]{4}-[0-9]{2}-[0-9]{2}", fecha))
#fecha = print(re.findall("[0-9]{2}:[0-9]{2}:[0-9]{2}", fecha))
#print(re.findall("[0-9]{4}", fecha))
#print(re.findall("-([0-9]{2})-", fecha))
#print(re.findall("-([0-9]{2}) ", fecha))
print(re.split("-",re.findall("[0-9]{2,4}-[0-9]{1,2}-[0-9]{1,2}",fecha)[0]))

#año = "([0-9]{2,4})"
#mes = "([0-9]{1,2})"
#dia = "([0-9]{1,2})"
#print(re.findall(f"{año}-{mes}-{dia}", fecha))

