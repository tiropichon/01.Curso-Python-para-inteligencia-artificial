import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

frame2 = tk.Frame(root)
frame2.pack()

label = tk.Label(frame,text="Nombre largo")
label.pack(side="left")

entry = tk.Entry(frame)
entry.pack(side="right")

label2 = tk.Label(frame2,text="Apellido")
label2.pack(side="left")

entry2=tk.Entry(frame2)
entry2.pack(side="right")

root.mainloop()