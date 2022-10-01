def sumar():
	result.set(float(num1.get()) + float(num2.get()))

import tkinter as tk 

root = tk.Tk()

num1 = tk.StringVar()
num2 = tk.StringVar()
result = tk.StringVar()

tk.Entry(root,justify="center",textvariable=num1).pack()
tk.Entry(root,justify="center",textvariable=num2).pack()
tk.Entry(root,justify="center",textvariable=result).pack()

tk.Button(root,text="Sumar",command=sumar).pack()

root.mainloop()