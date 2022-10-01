# 3 EJERCICIO TEMA 14 TKINTER

# Crea una ventana con etiquetas y botones para un proyecto de interfaz online para tests médicos
# La ventana debe tener un tamaño de 480x320px y un color de fondo gris claro. El estilo de borde debe ser "groove"
# La ventana debe tener como título "Test auditivo"
# Debe aparecer una etiqueta, en la parte superior, de fondo gris oscuro y letra en blanco, con el texto:
# 	"Pulse todos los botones que correspondan a cada sonido"
# La ventana debe tener cuatro botones: 
# 	- Botón 1 situado en el centro, arriba. Tamaño 12x5. Fondo de color azul y letra en blanco. Texto: Sonido agudo
#	- Botón 2 situado en el centro, abajo. Tamaño 12x5. Fondo de color naranja y letra en blanco. Texto: Sonido grave
#	- Botón 3 situado a la izquierda, en altura media. Tamaño 12x8. Fondo negro y letra en blanco. Texto: Oído izq
#	- Botón 4 situado a la derecha, en altura media. Tamaño 12x8. Fondo blanco y letra en negro. Texto: Oído derch

from tkinter import *

class Application(Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master

		# título de la ventana principal "Test auditivo"
		self.master.title("Test Auditivo")
		# La ventana debe tener un tamaño de 480x320px y un color de fondo gris claro. El estilo de borde debe ser "groove"
		self.master.config(width=480, height=320, bg="lightgrey", bd=10, relief="groove")

		#Ventana no redimensionable
		self.master.resizable(0,0)

		#Función que genera los widgets
		self.create_widgets()

	def create_widgets(self):

		self.frame = Frame(self,bg="lightgrey").pack(padx=5,pady=5)

		#Etiqueta en la parte superior, fondo gris oscuro, y letra en blanco
		self.label = Label(self.frame,text="Pulse todos los botones que correspondan a cada sonido",bg="darkgrey", fg="white").pack(side="top")

		# botón 1 en el centro, arriba. Color azul y letra en blanco. Texto: Sonido agudo
		self.boton1 = Button(self.frame, width=12, height=5, bg="blue", fg="white", text="Sonido agudo").pack(side="top")

		# botón 2 en el centro, abajo. Color naranja y letra en blanco. Texto: Sonido grave
		self.boton2 = Button(self.frame, width=12, height=5, bg="orange", fg="white", text="Sonido grave").pack(side="bottom")

		# botón 3 en altura media, a la izquierda. Fondo negro y letra en blanco. Texto: Oído izquierdo
		self.boton3 = Button(self.frame, width=12, height=5, bg="black", fg="white", text="Oído izquierdo").pack(side="left")

		# botón 4 en altura media, a la derecha. Fondo blanco y letra en negro. Texto: Oído derecho
		self.boton4 = Button(self.frame, width=12, height=5, bg="white", fg="black", text="Oído derecho").pack(side="right")



root = Tk()
app = Application(master=root)
root.mainloop()