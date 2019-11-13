import random
import tkinter as tk
from tkinter import Tk, Frame, Button


class Window(Frame):
    def __init__(self, master, num_buttons=1):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=tk.BOTH, expand=1)
        self.buttons = []
        self.moves = []
        for i in range(num_buttons):
            but = Button(master, text=f"Catch me {i}")
            but.place(x=random.randrange(300), y=random.randrange(300))
            self.buttons.append(but)

            def move(event=None):
                if event:
                    event.widget.place_configure(x=random.randrange(300), y=random.randrange(300))

            but.bind("<Enter>", move)
            print(but)

        #self.button = Button(master, text="Catch me", command=self.moveButton)
        #self.moveButton()

    def moveButton(self):
        print(self.button.size)
        self.button.place_configure(x=random.randrange(300), y=random.randrange(300))



root = Tk()
app = Window(root, 3)
root.wm_title("Tkinter window")
root.geometry("720x568")
root.mainloop()