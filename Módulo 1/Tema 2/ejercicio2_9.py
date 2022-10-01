# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

texto = "Pero lo que más me gustaba de aquel museo era que todo "
texto += "estaba siempre en el mismo sitio. No cambiaba nada. "
texto += "Podías ir cien mil veces distintas y el esquimal seguía "
texto += "pescando, y los pájaros seguían volando hacia el sur, "
texto += "y los ciervos seguían bebiendo en las charcas con esas "
texto += "patas tan finas y tan bonitas que tenían, y la india del "
texto += "pecho al aire seguía tejiendo su manta."

print('La palabra seguía aparece',texto.count('seguía'),'veces en la cadena')

#indice va a almacenar la posición de la cadena 'seguía'
indice=texto.find('seguía')

#puntos va a almacenar la posición del char '.'
puntos=texto.find('.')

#comas va a almcacenar la posición del char ','
comas=texto.find(',')

print('Indice=',indice)
print('Indice punto=',puntos)
print('Indice coma=',comas)

#compruebo si la posición de la cadena 'seguía' se encuentra antes de un '.'
if(indice<puntos):
    '''si 'seguía' se encuentra antes de un punto, muestro el texto comprendido
    entre la posición desde donde se encuentra 'seguía' hasta ese punto'''
    print(texto[indice:puntos])
    
    '''Busco la posición dentro de la cadena, de la siguiente cadena 'seguía', 
    contanto desde la posición anterior.'''
    indice=texto.find('seguía',puntos)
    
    '''Busco la posición dentro de la cadena, del siguiente punto, contanto desde
    el punto que hemos utilizado ahora mismo.'''
    puntos=texto.find('.',puntos+1)
else:
    print(texto[indice:comas])
    indice=texto.find('seguía',comas)
    comas=texto.find(',',comas+1)
    
print('Indice=',indice)
print('Indice punto=',puntos)
print('Indice coma=',comas)
    
if(indice<puntos):
    '''si 'seguía' se encuentra antes de un punto, muestro el texto comprendido
    entre la posición desde donde se encuentra 'seguía' hasta ese punto'''
    print(texto[indice:puntos])
    
    '''Busco la posición dentro de la cadena, de la siguiente cadena 'seguía', 
    contanto desde la posición anterior.'''
    indice=texto.find('seguía',puntos)
    
    '''Busco la posición dentro de la cadena, del siguiente punto, contanto desde
    el punto que hemos utilizado ahora mismo.'''
    puntos=texto.find('.',puntos+1)
else:
    print(texto[indice:comas])
    indice=texto.find('seguía',comas)
    comas=texto.find(',',comas+1)
    
print('Indice=',indice)
print('Indice punto=',puntos)
print('Indice coma=',comas)
    
if(indice<puntos):
    '''si 'seguía' se encuentra antes de un punto, muestro el texto comprendido
    entre la posición desde donde se encuentra 'seguía' hasta ese punto'''
    print(texto[indice:puntos])
    
    '''Busco la posición dentro de la cadena, de la siguiente cadena 'seguía', 
    contanto desde la posición anterior.'''
    indice=texto.find('seguía',puntos)
    
    '''Busco la posición dentro de la cadena, del siguiente punto, contanto desde
    el punto que hemos utilizado ahora mismo.'''
    puntos=texto.find('.',puntos+1)
else:
    print(texto[indice:comas])
    indice=texto.find('seguía',comas)
    comas=texto.find(',',comas+1)
    
print('Indice=',indice)
print('Indice punto=',puntos)
print('Indice coma=',comas)
    
if(indice<puntos):
    '''si 'seguía' se encuentra antes de un punto, muestro el texto comprendido
    entre la posición desde donde se encuentra 'seguía' hasta ese punto'''
    print(texto[indice:puntos])
    
    '''Busco la posición dentro de la cadena, de la siguiente cadena 'seguía', 
    contanto desde la posición anterior.'''
    indice=texto.find('seguía',puntos)
    
    '''Busco la posición dentro de la cadena, del siguiente punto, contanto desde
    el punto que hemos utilizado ahora mismo.'''
    puntos=texto.find('.',puntos+1)
else:
    print(texto[indice:comas])
    indice=texto.find('seguía',comas)
    comas=texto.find(',',comas+1)
  