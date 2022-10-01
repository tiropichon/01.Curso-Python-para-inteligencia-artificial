# -*- coding: utf-8 -*-

import tkinter as tk

def coste():
	cost = 15
	if jarron.get():
		cost += 5 

	if regalo.get():
		cost += 2

	cost_label.config(text=f"El coste es {cost} €")

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

#toscana = tk.PhotoImage(file="toscana.gif")
toscana = tk.PhotoImage(file="toscana.gif")
jarron = tk.IntVar()
regalo = tk.IntVar()

tk.Label(frame, image=toscana).pack(side="left")
tk.Label(frame, text="Elige extras para tu ramo de flores").pack()

tk.Checkbutton(frame, text="Jarrón Rústico", variable=jarron, onvalue=1, offvalue=0, command=coste).pack(side="top", anchor="w")
tk.Checkbutton(frame, text="Prepara para regalo", variable=regalo, onvalue=1, offvalue=0, command=coste).pack(side="top", anchor="w")

cost_label = tk.Label(root,text="El coste es 15 €")
cost_label.pack()

root.mainloop()