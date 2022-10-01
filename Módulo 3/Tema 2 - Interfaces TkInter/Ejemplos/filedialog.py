from tkinter import *
from tkinter import filedialog

root = Tk()

def test():
	#ruta = filedialog.askopenfilename(title="Abrir fichero...")
	fichero = filedialog.asksaveasfile(title="Guardar fichero")
	print(fichero)

	if fichero is not None:
		fichero.write("Hemos creado este contenido dentro del fichero")
		fichero.close()

Label(root).pack()
Button(root,text="Guardar archivo", command=test).pack()
Label(root).pack()

root.mainloop()