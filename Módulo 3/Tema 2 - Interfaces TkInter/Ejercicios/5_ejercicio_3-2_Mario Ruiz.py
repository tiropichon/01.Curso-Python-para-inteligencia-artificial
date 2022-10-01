# 5º EJERCICIO TEMA 12 - TKINTER
# Crea la interfaz para una rockola (máquina de música) virtual

from tkinter import *

class Application(Frame):
	def __init__(self,master=None):
		super().__init__(master)
		self.master = master
		self.master.title("Rockola")

		#Ventana con borde "ridge"
		self.master.config(relief="ridge",bd=5, bg="lightblue")

		#Tamaño fijo
		self.master.resizable(0,0)
		self.create_widgets()

	def create_widgets(self):

		# En la ventana debe aparecer un título a tamaño 24
		Label(self.master, text="ROCKOLA", font=("Verdana",24), bd=5, relief="sunken", width=43, bg="lightblue", fg="blue").grid(row=0,column=0, columnspan=2, padx=5, pady=5)

		# Añade un subtítulo explicativo a tamaño 18
		Label(self.master, text="App que simula una Rockola", font=("Tahoma",18), bd=5, relief="groove", width=35, bg="lightblue", fg="yellow").grid(row=1,column=0, columnspan=2, padx=5,pady=5)

		# En una distribución de dos columnas, debe haber 10 botones
		# En cada botón debe aparecer el título de una canción
		# Configura colores, fuente del texto, dimensiones de los botones
        # Programa un tipo de cursor diferente para las canciones según el estilo
		Button(self.master, text="Blues - B.B. King", width=50, height=5, fg="black", bg="yellow", cursor="clock").grid(row=2,column=0, padx=5, pady=5)
		Button(self.master, text="Jazz - Louis Armstrong", width=50, height=5, fg="yellow", bg="black", cursor="cross").grid(row=2,column=1, padx=5, pady=5)
		Button(self.master, text="Rythm & Blues - Usher", width=50, height=5, fg="blue", bg="orange", cursor="dotbox").grid(row=3,column=0, padx=5, pady=5)
		Button(self.master, text="Rock & Roll - Elvis Presley", width=50, height=5, fg="orange", bg="blue", cursor="exchange").grid(row=3,column=1, padx=5, pady=5)	
		Button(self.master, text="Soul - James Brown", width=50, height=5, fg="green", bg="red", cursor="heart").grid(row=4,column=0, padx=5, pady=5)
		Button(self.master, text="Soul - Sam Cooke", width=50, height=5, fg="red", bg="green", cursor="heart").grid(row=4,column=1, padx=5, pady=5)	
		Button(self.master, text="Rock & Roll - Chuck Berry", width=50, height=5, fg="red", bg="lightgreen", cursor="exchange").grid(row=5,column=0, padx=5, pady=5)
		Button(self.master, text="Rythm & Blues - Beyoncé", width=50, height=5, fg="lightgreen", bg="pink", cursor="dotbox").grid(row=5,column=1, padx=5, pady=5)	
		Button(self.master, text="Jazz - Ray Charles", width=50, height=5, fg="black", bg="white", cursor="cross").grid(row=6,column=0, padx=5, pady=5)
		Button(self.master, text="Blues - Eric Clapton", width=50, height=5, fg="white", bg="black", cursor="clock").grid(row=6,column=1, padx=5, pady=5)		

root = Tk()
app = Application(master=root)
app.mainloop()