# lista_bzrp=[
#     {
#         'title': 'QUEVEDO || BZRP Music Sessions #52',
#         'views': 227192970, 
#         'length': 204,
#         'img_url': 'https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg', 
#         'url': 'https://youtube.com/watch?v=A_g3lMcWVy0',
#         'date': '2022-07-06 00:00:00'
#     }, 
#     {   
#         'title': 'VILLANO ANTILLANO || BZRP Music Sessions #51', 
#         'views': 112947399, 
#         'length': 188, 
#         'img_url': 'https://i.ytimg.com/vi/wvz97-lNPH8/sddefault.jpg', 
#         'url': 'https://youtube.com/watch?v=wvz97-lNPH8', 
#         'date': '2022-06-08 00:00:00'
#     }]

from data import lista_bzrp

def mostrar_lista_temas():
    for i in range(len(lista_bzrp)):
        print(f"{lista_bzrp[i]['title']}")

# print(type(lista_bzrp))
# print(type(lista_bzrp[0]))
#B. Recorrer la lista imprimiendo por consola el título de cada video#
# for i in range(len(lista_bzrp)):
#     print(f"{lista_bzrp[i]['title']}")
    #print(f"{tema['title']}")#

#C. Recorrer la lista imprimiendo por consola el título de cada video junto a la
# cantidad de reproducciones del mismo
for tema in lista_bzrp:
    print(f"{tema['title']} - {tema['views']}")

#D. Recorrer la lista y determinar cuál es la cantidad máxima de reproducciones
# (MÁXIMO)#
flag_primero = True
# max_views = lista_bzrp[0]["views"]

for tema in lista_bzrp:
    if (flag_primero==True) or (tema['views'] > max_views):
        max_views = tema["views"]
        flag_primero = False
print(f"Cantidad máxima de reproducciones: {max_views}")
for tema in lista_bzrp:
    if(tema["views"] == max_views):
        print(f"{tema['title']}")

print(max_views)

#E. Recorrer la lista y determinar cuál es la cantidad mínima de reproducciones
#(MÍNIMO)
flag_primero = True
for tema in lista_bzrp:
    if (flag_primero==True) or (tema['views'] < min_views):
        min_views = tema["views"]
        flag_primero = False
print(f"Cantidad mínima de reproducciones: {min_views}")
for tema in lista_bzrp:
    if(tema["views"] == min_views):
        print(f"{tema['title']}")

#F#
acumulador_views = 0
for tema in lista_bzrp:
    acumulador_views += tema["views"]

print(f"El total de reproducciones del canal es: {acumulador_views}")

#G#
cont_temas = 0

for tema in lista_bzrp:
    cont_temas += 1

prom_views = acumulador_views / cont_temas

print(f"El promedio de vistas por video es: {prom_views}")

'''
PARA MOVER LINEAS DE CODIGO ENTERAS HACIA DERECHA E IZQUIERDA:
DERECHA: TAB
IZQUIERDA: SHIFT + TAB
ARRIBA: ALT + FLECHA ARRIBA
ABAJO: ALT + FLECHA ABAJO
'''
