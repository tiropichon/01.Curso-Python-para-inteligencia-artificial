# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
import datetime

def edad(anio_nac):
    """
    Esta función calcula los años que cumples en el año actual
    """
    hoy = datetime.datetime.today()
    return hoy.year - anio_nac
    
mi_edad = edad(1980)    

# mostramos el resultado en pantalla 
print("Este año cumples", mi_edad, "años")
