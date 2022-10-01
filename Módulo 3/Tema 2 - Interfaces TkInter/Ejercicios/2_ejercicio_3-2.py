# 2 EJERCICIO TEMA 14 TKINTER

# Crea una ventana interfaz de usuario que sirva para generar una lista con productos para ir a la compra
# Para ello, utiliza tkinter, creando la raiz, etiquetas y campo de texto
# Almacena los nombres de cinco productos como elementos de una lista, a medida que se introduzcan.
# Finalmente, muestra los elementos de la lista
def compra():
	resulprod1.set("Producto 1: " + prod1.get())
	resulprod2.set("Producto 2: " + prod2.get())
	resulprod3.set("Producto 3: " + prod3.get())
	resulprod4.set("Producto 4: " + prod4.get())
	resulprod5.set("Producto 5: " + prod5.get())
	return resulprod1, resulprod2, resulprod3, resulprod4, resulprod5

import tkinter as tk


root=tk.Tk()
root.title("Lista de la compra")
root.iconbitmap("carrito.ico")

prod1 = tk.StringVar()
prod2 = tk.StringVar()
prod3 = tk.StringVar()
prod4 = tk.StringVar()
prod5 = tk.StringVar()
resulprod1 = tk.StringVar()
resulprod2 = tk.StringVar()
resulprod3 = tk.StringVar()
resulprod4 = tk.StringVar()
resulprod5 = tk.StringVar()

label = tk.Label(root,text="Productos lista de la compra",justify="center", relief="ridge", borderwidth=2).grid(row=0,columnspan=2)
label1 = tk.Label(root,text="Producto nº 1").grid(row=1,column=0,sticky="w")
label2 = tk.Label(root,text="Producto nº 2").grid(row=2,column=0,sticky="w")
label3 = tk.Label(root,text="Producto nº 3").grid(row=3,column=0,sticky="w")
label4 = tk.Label(root,text="Producto nº 4").grid(row=4,column=0,sticky="w")
label5 = tk.Label(root,text="Producto nº 5").grid(row=5,column=0,sticky="w")
labelprod1 = tk.Label(root, textvariable=resulprod1).grid(row=7,columnspan=2,sticky="w")
labelprod2 = tk.Label(root, textvariable=resulprod2).grid(row=8,columnspan=2,sticky="w")
labelprod3 = tk.Label(root, textvariable=resulprod3).grid(row=9,columnspan=2,sticky="w")
labelprod4 = tk.Label(root, textvariable=resulprod4).grid(row=10,columnspan=2,sticky="w")
labelprod5 = tk.Label(root, textvariable=resulprod5).grid(row=11,columnspan=2,sticky="w")


entry1 = tk.Entry(root,textvariable=prod1, justify="left").grid(row=1,column=1) 
entry2 = tk.Entry(root,textvariable=prod2, justify="left").grid(row=2,column=1)
entry3 = tk.Entry(root,textvariable=prod3, justify="left").grid(row=3,column=1)
entry4 = tk.Entry(root,textvariable=prod4, justify="left").grid(row=4,column=1)
entry5 = tk.Entry(root,textvariable=prod5, justify="left").grid(row=5,column=1)

boton = tk.Button(root,text="Mostrar lista de la compra", command=compra).grid(row=6,columnspan=2)

root.mainloop()
