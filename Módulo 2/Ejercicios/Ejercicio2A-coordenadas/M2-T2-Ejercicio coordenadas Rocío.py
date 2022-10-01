# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 22:32:25 2021

@author: Rocío
"""


class Punto():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
    
    def Cuadrante(self):
        if self.y == 0 and self.x != 0:
            print(f"El punto {self} se encuentra sobre el eje Y.")
        elif self.y != 0 and self.x == 0:
            print(f"El punto {self} se encuentra sobre el eje X.")
        elif self.y > 0:
            if self.x > 0:
                print(f"El punto {self} pertenece al cuadrante I.")
            if self.x < 0:
                print(f"El punto {self} pertenece al cuadrante II.")
        elif self.y < 0:
            if self.x > 0:
                print(f"El punto {self} pertenece al cuadrante VI.")
            if self.x < 0:
                print(f"El punto {self} pertenece al cuadrante III.")
        else:
            print(f"El punto {self} se encuentra en el origen de coordenadas.")
        
    def Vector(self, other):
        return '(' + str(other.x - self.x) + ',' + str(other.y - self.y) + ')'
    
    def Distancia(self,other):
        from math import sqrt
        d = sqrt((other.x - self.x)**2+(other.y - self.y)**2)
        return round(d,3)

class Rectangulo():
    def __init__(self, p_inicial=Punto(0,0), p_final=Punto(0,0)):
        self.p_inicial = p_inicial
        self.p_final = p_final
                
    def DosPuntos(self):
        print("El rectángulo se va a formar a partir de los siguientes puntos:")
        print(self.p_inicial)
        print(self.p_final)

    def Base(self):
        self.base = abs(self.p_inicial.x - self.p_final.x)
        print('La base del rectángulo es', self.base)

    def Altura(self):
        self.altura = abs(self.p_inicial.y - self.p_final.y)
        print('La altura del rectángulo es', self.altura)

    def Area(self):
        print('El área del rectángulo es', self.base * self.altura)
    
    
# Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.
A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3, -1)
D = Punto(0,0)
F = Punto(0,1)
# A
print(f"A{A}")
print(f"B{B}")
print(f"C{C}")
print(f"D{D}")

# Consulta a que cuadrante pertenecen el punto A, C y D.
A.Cuadrante()
C.Cuadrante()
D.Cuadrante()
F.Cuadrante()

# Consulta los vectores AB y BA.
print(A.Vector(B))
print(B.Vector(A))

# Consulta la distancia entre los puntos 'A y B' y 'B y A'.
print(A.Distancia(B))
print(B.Distancia(A))

# Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0).
distancia_origen = {'A': A.Distancia(D), 'B': B.Distancia(D), 'C': C.Distancia(D)}
mayor_distancia =max(distancia_origen.values())
punto_mas_lejos = max(distancia_origen, key=lambda key: distancia_origen[key])
print(f'El punto más alejado del origen es {punto_mas_lejos}, que está a {mayor_distancia}.')


# Crea un rectángulo utilizando los puntos A y B.
rect = Rectangulo(A, B)
rect.DosPuntos()

# Consulta la base, altura y área del rectángulo.
rect.Base()
rect.Altura()
rect.Area()

rect2 = Rectangulo(B, C)
rect2.DosPuntos()
rect2.Base()
rect2.Altura()
rect2.Area()
