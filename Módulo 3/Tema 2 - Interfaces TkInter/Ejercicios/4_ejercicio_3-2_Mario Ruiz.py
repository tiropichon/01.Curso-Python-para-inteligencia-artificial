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
    # Si todos los campos se han rellenado, muestro por pantalla los datos introducidos
	if (len(app.nombre.get()) > 0 and len(app.apellidos.get()) > 0 and len(app.usuario.get()) > 0 and len(app.password.get()) > 0):
		texto = "Datos usuario registrado\nNombre: {}\nApellidos: {}\nUsuario: {}\nContraseña: {}".format(app.nombre.get(),app.apellidos.get(),app.usuario.get(),app.password.get())		
	else:
		#Si hay alguno que no se ha rellenado, le paso esta cadena a la variale texto
		texto="Debe rellenar los siguientes datos:\n"
    
    #Si el campo Nombre esta vacío, cambia el color de fondo a rojo y concateno el nombre de campo a la variable texto.
	if (len(app.nombre.get()) == 0):
		app.eNombre.configure(bg="red")
		texto += "Nombre\n"
	else:
		#Si no está vacío, cambia el color de fondo a blanco.
		app.eNombre.configure(bg="white")
    
    #Si el campo Apellidos esta vacío, cambia el color de fondo a rojo y concateno el nombre de campo a la variable texto.
	if (len(app.apellidos.get()) == 0):
		app.eApellidos.configure(bg="red")
		texto += "Apellidos\n"
	else:
		#Si no está vacío, cambia el color de fondo a blanco.
		app.eApellidos.configure(bg="white")
    
    ##Si el campo Usuario esta vacío, cambia el color de fondo a rojo y concateno el nombre de campo a la variable texto.
	if (len(app.usuario.get()) == 0):
		app.eUsuario.configure(bg="red")
		texto += "Usuario\n"
	else:
		#Si no está vacío, cambia el color de fondo a blanco.
		app.eUsuario.configure(bg="white")
    
    ##Si el campo Password esta vacío, cambia el color de fondo a rojo y concateno el nombre de campo a la variable texto.
	if (len(app.password.get()) == 0):
		app.ePassword.configure(bg="red")
		texto += "Password\n"
	else:
		#Si no está vacío, cambia el color de fondo a blanco.
		app.ePassword.configure(bg="white")

    #Muestro un messagebox que muestra el texto que se ha recopilado en los pasos anteriores
	messagebox.showinfo(message=texto,title="Datos del usuario")

class Application(Frame):

	#Constructor de la clase Application
	def __init__(self, master=None):
		#Constructor de la clase padre
		super().__init__(master)

		#Asigno al atributo master, el argumento master
		self.master =  master

		#establezco el título de la ventana
		self.master.title("Registro de usuario")

		#Pongo un borde de 15, color gris claro
		self.config(bd=15, bg="lightgrey")

		#La pantalla no se puede redimensionar
		self.master.resizable(0,0)
		self.pack()

		#Llamo a la función que genera los widgets
		self.create_widgets()

	def create_widgets(self):

		#Creo las StringVar que almacenarán los datos de los entry del formulario
		self.nombre = StringVar()
		self.apellidos = StringVar()
		self.usuario = StringVar()
		self.password = StringVar()
        
        #Creo el primer frame. Fondo azul claro, borde sunken y tamaño de borde 10
		self.frame1 = Frame(self, bg="lightblue", bd=10, relief="sunken")
		self.frame1.pack(padx=5, pady=5)

		#Creo una etiqueta vacía como separador entre los dos frames
		Label(self ,text="", bg="lightgrey", padx=10, pady=10)

		#Creo el segundo frame. Fondo verde claro, borde ridge y tamaño de borde 10
		self.frame2 = Frame(self, bg="lightgreen", bd=10, relief="ridge")
		self.frame2.pack(padx=5, pady=5)

		#----------------------------------

		#Etiqueta para Nombre del primer frame
		self.lNombre = Label(self.frame1, text="Nombre", bg="lightblue").pack(side="left")
		
		#Entry para recoger el campo Nombre del primer frame
		self.eNombre = Entry(self.frame1, textvariable=self.nombre)
		self.eNombre.pack(side="left")
		
		#Etiqueta para Apellidos del primer frame
		self.lApellidos = Label(self.frame1, text="Apellidos", bg="lightblue").pack(side="left")
		
		#Entry para recoger el campo Apellidos del primer frame
		self.eApellidos = Entry(self.frame1, textvariable=self.apellidos)
		self.eApellidos.pack(side="left")

        #-----------------------------------

		#Etiqueta Usuario del segundo frame
		self.lUsuario = Label(self.frame2, text="Usuario", bg="lightgreen").pack(side="left")
		
		#Entry para recoger el campo Usuario del segundo frame
		self.eUsuario = Entry(self.frame2, textvariable=self.usuario)
		self.eUsuario.pack(side="left")
		
		#Etiqueta password del segundo frame
		self.lPassword = Label(self.frame2, text="Password", bg="lightgreen").pack(side="left")
		
		#Entry para recoger el campo Password del segundo frame
		self.ePassword = Entry(self.frame2, textvariable=self.password,show="*")
		self.ePassword.pack(side="left")

		#----------------------------------

		#Botón con texto Registrarse, que llama a la función registrarse()
		self.bRegisto = Button(self, text="Registrarse", command=registrarse).pack(side="right", padx=5, pady=5)

#creamos la ventana raíz
root = Tk()
app = Application(master=root)
root.mainloop()



