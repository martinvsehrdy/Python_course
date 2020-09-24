import tkinter as tk
from tkinter import Tk, Frame, Button

window = Tk()
frame = Frame(window, background="azure")
frame.pack(fill=tk.X, side=tk.TOP)

bottomframe = Frame(window, background="yellow")
bottomframe.pack(fill=tk.Y, side=tk.BOTTOM)

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack(side=tk.LEFT)

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack(side=tk.LEFT)

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack(side=tk.LEFT)

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack(side=tk.BOTTOM)

window.geometry("600x400")
window.mainloop()

