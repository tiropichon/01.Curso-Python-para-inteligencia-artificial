from tkinter import *
root = Tk()


def listarProductos():

    lista = [entradaProducto1.get(),entradaProducto2.get(),entradaProducto3.get(),entradaProducto4.get()]
    
    for producto in lista:    

        Label(root, text=producto).grid()
        
#sticky alinea. y se utiliza dentro de grid(). Equivalente a anchor, pero este dentro de pack()
etiquetaProducto1 = Label(root,text="Producto 1")
etiquetaProducto1.grid(row=0, column=0, sticky=E, padx=5, pady=5)

entradaProducto1 = Entry(root)
entradaProducto1.grid(row=0, column=1, padx=5, pady=5)
entradaProducto1.config(justify=CENTER, )


etiquetaProducto2 = Label(root, text="Producto 2")
etiquetaProducto2.grid(row=1, column=0, sticky=E, padx=5, pady=5)


entradaProducto2 = Entry(root)
entradaProducto2.grid(row=1, column=1, padx=5, pady=5)
entradaProducto2.config(justify=CENTER)


etiquetaProducto3 = Label(root, text="Producto 3")
etiquetaProducto3.grid(row=2, column=0, sticky=E, padx=5, pady=5)

entradaProducto3 = Entry(root)
entradaProducto3.grid(row=2, column=1, padx=5, pady=5)
entradaProducto3.config(justify=CENTER)


etiquetaProducto4 = Label(root, text="Producto 4")
etiquetaProducto4.grid(row=3, column=0, sticky=E, padx=5, pady=5)

entradaProducto4 = Entry(root)
entradaProducto4.grid(row=3, column=1, padx=5, pady=5)
entradaProducto4.config(justify=CENTER)


#etiquetaLista = Label(root, text="lista")
#etiquetaLista.grid(row = 5, column=1)

Button(root, text="Mostrar productos", command=listarProductos).grid(row=7, column=1)



root.mainloop()
