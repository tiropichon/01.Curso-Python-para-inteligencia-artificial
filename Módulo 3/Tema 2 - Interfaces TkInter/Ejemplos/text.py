import tkinter as tk

#Creamos la ventana
root = tk.Tk()

#widget text
texto = tk.Text(root)

#Empaquetamos el widget text dentro de la
#ventana "root"
texto.pack()

#Dimensiones concretas. Unidades, no en 
#pixels

texto.config(width=80,height=20,font=("Consolas",12),padx=10,pady=5)

#Envento mainloop para q muestre la ventana
root.mainloop()