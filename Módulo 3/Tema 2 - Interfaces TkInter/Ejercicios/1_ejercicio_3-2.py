# 1 EJERCICIO TEMA 14 TKINTER

# Escribe el código necesario para crear una ventana utilizando tkinter
# Debe mostrar un texto de presentación o una advertencia
#root.title("")
#root.iconbitmap('icono.ico')

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Mensaje de bienvenida")
root.iconbitmap("icono.ico")
root.config(bg="beige",width=320,height=240,padx=8,pady=8)

label = tk.Label(root,text="Bienvenidos a tkinter!",bg="lightblue",fg="red",borderwidth=2,relief="groove")
label.grid(row=0,column=0)
messagebox.showinfo(message="Mensaje de bienvenida a tkinter!!",title="Bienvenida")

root.mainloop()