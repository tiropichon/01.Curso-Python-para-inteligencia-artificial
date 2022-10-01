# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def factorial(x):
    resultado=1
    if x==0:
        resultado*=1
        return resultado
    else:
        for num in range(1,x+1):
            resultado *= num
        return resultado
            
numero=5
print("El factorial de",numero,"es",factorial(numero))