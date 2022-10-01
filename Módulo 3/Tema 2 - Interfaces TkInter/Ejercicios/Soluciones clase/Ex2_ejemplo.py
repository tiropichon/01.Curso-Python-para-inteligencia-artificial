# Crea una ventana interfaz de usuario que sirva para generar una lista con productos para ir a la compra
# Para ello, utiliza tkinter, creando la raiz, etiquetas y campo de texto
# Almacena los nombres de cinco productos como elementos de una lista, a medida que se introduzcan.
# Finalmente, muestra los elementos de la lista

import tkinter as tk


def load_item():
    saved_items.append(items_box.get())
    items_box.delete(0, "end")


def generate_shopping_list():
    text = ""
    for item in saved_items:
        text += item + "\n"

    shopping_list.insert(tk.INSERT, text)


# Variables
saved_items = list()

# Main window
window = tk.Tk()
window.title("Mi lista de la compra")
window.geometry("600x300")
window.configure(bg="whitesmoke")

# Window elements
header_msg = tk.Label(text="Introduce aquí cada artículo:")
header_msg.pack()
items_box = tk.Entry()
items_box.pack()
load_item_btn = tk.Button(text="Guardar", command=load_item)
load_item_btn.pack()
shopping_list_btn = tk.Button(text="Generar Lista", command=generate_shopping_list)
shopping_list_btn.pack()
shopping_list = tk.Text(bg="whitesmoke", bd=0)
shopping_list.pack()

window.mainloop()