import tkinter as tk

root = tk.Tk()



def lista():

    tk.Label(root,text=f"Tengo que comprar {p1.get()} y ademas {p2.get()} y por último {p3.get()}").grid(row=6, column=1)





root.title("Productos")

root.geometry('300x200')



#icono = root.iconbitmap('python.ico')



p1 = ""

p2 = ""

p3 = ""



label_p1 = tk.Label(root, text="Producto_1")

label_p1.grid(row=0, column=0, sticky="e", padx=5, pady=5)



p1 = tk.Entry(root)

p1.grid(row=0, column=1)

p1.config(justify="center")



label_p2 = tk.Label(root, text="Producto_2")

label_p2.grid(row=2, column=0, sticky="e", padx=5, pady=5)



p2 = tk.Entry(root)

p2.grid(row=2, column=1)

p2.config(justify="center")



label_p3 = tk.Label(root, text="Producto_3")

label_p3.grid(row=3, column=0, sticky="e", padx=5, pady=5)



p3 = tk.Entry(root)

p3.grid(row=3, column=1)

p3.config(justify="center")



button = tk.Button(root, text="Lista", width=20, command=lista)

button.grid(row=5, column=1)



root.mainloop()