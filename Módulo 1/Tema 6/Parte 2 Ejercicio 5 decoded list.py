# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 18:50:28 2021

@author: mario
"""
def ecode(cadena):
    if len(cadena) == 0:
        return []
    
    indice = 1
    while indice < len(cadena) and cadena[indice] == cadena[indice - 1]:
            indice += 1
    
    ecoded_data = [cadena[0],indice]
    
    return ecoded_data + ecode(cadena[indice:len(cadena)])

s="AAAABBBBABBBBAAA"
print(ecode(s))

