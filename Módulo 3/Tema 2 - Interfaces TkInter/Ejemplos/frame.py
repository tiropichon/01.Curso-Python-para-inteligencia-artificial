import tkinter as tk

root = tk.Tk()

#widget frame
frame = tk.Frame(root,width=300,height=200)

#side = top, bottom, right, left
#anchor= w-> west, e->east
#frame.pack(side="top",anchor="w")

#fill-> rellenar fill="x"->rellenar en x
#en fill="y", hay que añadir el argumento "expand"
#fill="both",expand=1 -> Expandir en x,y
#expand=1 -> True; expand= 0 -> False
#frame.pack(fill="x")
#frame.pack(fill="y",expand=1)
frame.pack(fill="both",expand=1)

#bd-> border relief->relieve
frame.config(cursor="cross",bg="beige",bd=8,relief="sunken")

root.config(cursor="heart",bg="lightgray",bd=10,relief="ridge")

root.mainloop()