# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 09:35:49 2021

@author: mario
"""

#defino la función, con los argumentos no opcionales primero, y el opcional al final.
def dev_datos(nomPila,primApellido,segApellido,seg_nombre=""):
    #Muestro en pantalla los datos que se han introducido.
    if len(seg_nombre) > 0:
        print(f"Su nombre completo es:{nomPila.title()} {seg_nombre.title()} {primApellido.title()} {segApellido.title()}")
    else:
        print(f"Su nombre completo es:{nomPila.title()} {primApellido.title()} {segApellido.title()}")
    return

#Empezamos a almacenar en variables, los datos introducidos por el usuario 
print("Introduzca los datos")
print("--------------------")
nom_pila = input("Nombre de pila:")
seg_nombre = input("Segundo nombre, si posee:")
prim_apellido = input("Primer apellido:")
seg_apellido = input("Segundo apellido:")

#comprobamos si se ha introducido un segundo nombre.
#si no se introduce segundo nombre, la longitud de la variable es 0
#llamamos a la función con 3 argumentos
if len(seg_nombre) == 0:
    dev_datos(nom_pila,prim_apellido,seg_apellido)
else:
    #Si la longitud es mayor que 0, quiere decir que se ha introducido algo
    #por lo que llamamos a la función con los 4 argumentos.
    dev_datos(nom_pila,prim_apellido,seg_apellido,seg_nombre)
