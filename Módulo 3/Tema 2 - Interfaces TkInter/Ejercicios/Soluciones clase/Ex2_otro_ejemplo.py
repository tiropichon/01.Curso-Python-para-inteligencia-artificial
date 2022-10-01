import tkinter as tk


def print_function():
    print('Comprar:')
    print(element1.get(), element2.get(), element3.get(), element4.get(), element5.get())
    element1.delete(0, tk.END)
    element2.delete(0, tk.END)
    element3.delete(0, tk.END)
    element4.delete(0, tk.END)
    element5.delete(0, tk.END)


my_window = tk.Tk()
my_window.geometry('400x400')
my_window.title('My Shopping App')

my_text = tk.Label(text='Lista de la compra:', bg='#ffccff')
my_text.config(font=('Arial', 20))
my_text.pack(fill=tk.X)

blank = tk.Label()
blank.pack()

element1 = tk.Entry(font=('Arial', 18))
element1.pack()

blank = tk.Label()
blank.pack()

element2 = tk.Entry(font=('Arial', 18))
element2.pack()

blank = tk.Label()
blank.pack()

element3 = tk.Entry(font=('Arial', 18))
element3.pack()

blank = tk.Label()
blank.pack()

element4 = tk.Entry(font=('Arial', 18))
element4.pack()

blank = tk.Label()
blank.pack()

element5 = tk.Entry(font=('Arial', 18))
element5.pack()

blank = tk.Label()
blank.pack()

button = tk.Button(my_window, text='Print', command=print_function)
button.pack()

my_window.mainloop()