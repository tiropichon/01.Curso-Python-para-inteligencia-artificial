#Instrucción command en los botones
#se define primero las funciones y después el tema
#del GUI.

#para q aparezca en la consola
#def premio():
#    print("has ganado 100 puntos")

#para q aparezca en la interfaz


def crear_label():
    Label(root,text="¡Sorpresa!").pack()

from tkinter import *

root = Tk()

Button(root,text="Pincha aquí",command=crear_label).pack()

root.mainloop()