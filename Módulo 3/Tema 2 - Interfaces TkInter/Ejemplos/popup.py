# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox

def popup():
	messagebox.showinfo(title="Título del popup",message="Info que queremos mostrar")
	messagebox.showwarning(title="Advertencia!!!",message="Esta acción no se ha podido realizar")
	respuesta = messagebox.askquestion(title="Título del popup",message="¿Guardar cambios antes de salir?")
	if respuesta == "no":
		root.destroy()

	respuesta2 = messagebox.askokcancel(title="ok o cancel", message="Desea cerrar?")
	if respuesta2 == True:
		root.destroy()

root = tk.Tk()

tk.Button(root,text="Haz click", command=popup).pack()

root.mainloop()