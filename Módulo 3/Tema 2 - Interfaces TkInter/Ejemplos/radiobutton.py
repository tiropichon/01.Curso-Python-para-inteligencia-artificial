import tkinter as tk

def seleccion():
	opcion_sel.config(text="{}".format(opcion.get()))

def reset():
	opcion.set(None)
	opcion_sel.config(text="")

root = tk.Tk()

opcion = tk.IntVar()

tk.Radiobutton(root,text="Opción 1", variable=opcion, value=1, command=seleccion).pack()
tk.Radiobutton(root,text="Opción 2", variable=opcion, value=2, command=seleccion).pack()
tk.Radiobutton(root,text="Opción 3", variable=opcion, value=3, command=seleccion).pack()

opcion_sel = tk.Label(root)
opcion_sel.pack()

tk.Button(root,text="Reiniciar", command=reset).pack()

root.mainloop()