import tkinter as tk

root = tk.Tk()

#grid() crea una tabla. Usar en vez de pack()
#para ordenar los widgets

label = tk.Label(root,text="Usuario")
label.grid(row=0,column=0,sticky="w", padx=5,pady=5)

entry = tk.Entry(root)
entry.grid(row=0,column=1,padx=5,pady=5)
entry.config(justify="center")

label2 = tk.Label(root,text="Contraseña")
label2.grid(row=1,column=0,sticky="w",padx=5,pady=5)

entry2=tk.Entry(root)
entry2.grid(row=1,column=1,padx=5,pady=5)
entry2.config(justify="center",show="*")

root.mainloop()