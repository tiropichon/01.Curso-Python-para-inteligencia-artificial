# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 18:50:28 2021

@author: mario
"""



indice = 0
decoded_list = []

def decode(lista):
    if indice == len(lista):
        return decoded_list

    for i in range(lista[indice+1]):
        decoded_list.append(lista[indice])
    return decode(lista[indice+2:len(lista)])

encoded_list = ["A",8,"B",4,"A",1,"B",3]
print(encoded_list)
print(decode(encoded_list))