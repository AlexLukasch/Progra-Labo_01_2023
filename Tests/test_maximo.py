from data_stark import lista_personajes

flag_altura =True
altura_maxima = 0

for heroe in lista_personajes:
    altura_parseada = float (heroe['altura']) 

    if flag_altura == True or altura_parseada > altura_maxima:
        altura_maxima = altura_parseada
        flag_altura = False
    
        for hero in lista_personajes:
            if altura_parseada == altura_maxima:
                print(hero['nombre'])

