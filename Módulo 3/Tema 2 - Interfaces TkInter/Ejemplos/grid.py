import tkinter as tk

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master =  master
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		

root = tk.Tk()
app = Application(master=root)

#grid() crea una tabla. Usar en vez de pack()
#para ordenar los widgets

label = tk.Label(root,text="Nombre largo")
label.grid(row=0,column=0,sticky="w", padx=5,pady=5)

entry = tk.Entry(root)
entry.grid(row=0,column=1,padx=5,pady=5)

label2 = tk.Label(root,text="Apellido")
label2.grid(row=1,column=0,sticky="w",padx=5,pady=5)

entry2=tk.Entry(root)
entry2.grid(row=1,column=1,padx=5,pady=5)

root.mainloop()