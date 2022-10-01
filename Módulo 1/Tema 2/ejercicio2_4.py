# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 11:59:36 2021

@author: mario
"""
import math as m

numero=float(input("introduce N > 1000:"))
if(numero<1000):
    print("Introduce un número mayor de 1000")
else:
    Pi=numero * m.sin(m.radians(180)/numero)
    print("aprocimación de numero pi: ",round(Pi,4))