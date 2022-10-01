# 4º EJERCICIO TEMA 12 - TKINTER
# Crea una interfaz de usuario con dos marcos
# En uno de los marcos, utiliza los widgets Label y Entry para que el usuario introduzca nombre y apellidos
# En el otro marco, utiliza también Label y Entry para introducir nombre de usuario y contraseña
# El campo de contraseña no debe permitir que se vean los caracteres reales
# En la parte inferior de la ventana, crea un botón con el texto "Registrarse"
# Da color, dimensiones y tipo de borde a los marcos, etiquetas, campos de texto y botón
from tkinter import *
from tkinter import messagebox

def registrarse():
	texto = ""

	if (len(app.nombre.get()) > 0 and len(app.apellidos.get()) > 0 and len(app.usuario.get()) > 0 and len(app.password.get()) > 0):
		texto = "Datos usuario registrado\nNombre: {}\nApellidos: {}\nUsuario: {}\nContraseña: {}".format(app.nombre.get(),app.apellidos.get(),app.usuario.get(),app.password.get())		
	else:
		texto="Debe rellenar los siguientes datos:\n"

	if (len(app.nombre.get()) == 0):
		app.eNombre.configure(bg="red")
		texto += "Nombre\n"
	else:
		app.eNombre.configure(bg="white")

	if (len(app.apellidos.get()) == 0):
		app.eApellidos.configure(bg="red")
		texto += "Apellidos\n"
	else:
		app.eApellidos.configure(bg="white")

	if (len(app.usuario.get()) == 0):
		app.eUsuario.configure(bg="red")
		texto += "Usuario\n"
	else:
		app.eUsuario.configure(bg="white")

	if (len(app.password.get()) == 0):
		app.ePassword.configure(bg="red")
		texto += "Password\n"
	else:
		app.ePassword.configure(bg="white")

	messagebox.showinfo(message=texto,title="Datos del usuario")

class Application(Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master =  master
		self.master.title("Registro de usuario")
		self.config(bd=15, bg="lightgrey")
		self.master.resizable(0,0)
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		self.nombre = StringVar()
		self.apellidos = StringVar()
		self.usuario = StringVar()
		self.password = StringVar()

		self.frame1 = Frame(self, bg="lightblue", bd=10, relief="sunken")
		self.frame1.pack(padx=5, pady=5)
		self.lNombre = Label(self.frame1, text="Nombre", bg="lightblue").pack(side="left")
		self.eNombre = Entry(self.frame1, textvariable=self.nombre)
		self.eNombre.pack(side="left")
		self.lApellidos = Label(self.frame1, text="Apellidos", bg="lightblue").pack(side="left")
		self.eApellidos = Entry(self.frame1, textvariable=self.apellidos)
		self.eApellidos.pack(side="left")

		Label(self ,text="", bg="lightgrey", padx=10, pady=10)

		self.frame2 = Frame(self, bg="lightgreen", bd=10, relief="ridge")
		self.frame2.pack(padx=5, pady=5)
		self.lUsuario = Label(self.frame2, text="Usuario", bg="lightgreen").pack(side="left")
		self.eUsuario = Entry(self.frame2, textvariable=self.usuario)
		self.eUsuario.pack(side="left")
		self.lPassword = Label(self.frame2, text="Password", bg="lightgreen").pack(side="left")
		self.ePassword = Entry(self.frame2, textvariable=self.password,show="*")
		self.ePassword.pack(side="left")

		self.bRegisto = Button(self, text="Registrarse", command=registrarse).pack(side="right", padx=5, pady=5)

#creamos la ventana raíz
root = Tk()
app = Application(master=root)
root.mainloop()



