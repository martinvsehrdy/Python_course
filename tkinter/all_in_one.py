from tkinter import Tk, Label, Entry, IntVar, Canvas, Button
from tkinter.ttk import Combobox, Radiobutton


def button1_clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text=res)

def button2_clicked():
    button2.configure(fg=combo.get(), activeforeground=combo.get())

def button3_clicked():
    print(selected.get())
    label3.configure(text=selected.get())

window = Tk()
window.title("Welcome to First TKinter app")
window.geometry('350x200')
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
txt = Entry(window,width=10)
txt.grid(column=1, row=0)

button1 = Button(window, text="Click Me", command=button1_clicked)
button1.grid(column=2, row=0)

combo = Combobox(window)
combo['values'] = ("black", "red", "blue", "purple")
combo.current(1)  # set the selected item
combo.grid(column=0, row=1)

button2 = Button(window, text="Choose", command=button2_clicked)
button2.grid(column=1, row=1)

selected = IntVar()
rad1 = Radiobutton(window, text='First', value=1, variable=selected)
rad2 = Radiobutton(window, text='Second', value=2, variable=selected)
rad3 = Radiobutton(window, text='Third', value=3, variable=selected)
rad1.grid(column=0, row=2)
rad2.grid(column=1, row=2)
rad3.grid(column=2, row=2)
label3 = Label(window, text="")
label3.grid(column=0, row=3)
button3 = Button(window, text="What RadioButton", command=button3_clicked)
button3.grid(column=2, row=3)

canvas1 = Canvas(window, bg="yellow", width=100, height=70)
canvas1.grid(column=3, row=1)
print(canvas1.winfo_width())


window.mainloop()
