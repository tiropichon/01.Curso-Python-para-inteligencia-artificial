# -*- coding: utf-8 -*-

"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""

try:    
    archivo = open("resultado.txt", "w")
    print("Archivo resultado.txt abierto.")
    resultado = 15 * (3/0)
except IOError:
    # Instrucciones si ocurre la excepción IOError
    print("Error de entrada/salida.")    
except ZeroDivisionError:
    # Instrucciones si ocurre la excepción ZeroDivisionError
    print("Error división por cero.")
else:
    # Instrucciones si no ocurre ninguna excepción
    print("El resultado de la división es", resultado)
    archivo.write(resultado)    
finally:
    # Instrucciones si ocurren o no ocurren excepciones
    if not(archivo.closed):
        archivo.close()
        print("Archivo resultado.txt cerrado.")