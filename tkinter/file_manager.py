# importing tkinter and tkinter.ttk
# and all their functions and classes
import datetime
import os
import tkinter as tk
from tkinter import Tk
from tkinter.ttk import Treeview

# importing askopenfile function
# from class filedialog
from tkinter.filedialog import askopenfile, askdirectory

root = Tk()
root.geometry('900x650')

def open_dir():
	file = askdirectory()
	print(file)

tree = Treeview(root, height=600)
tree.pack(fill=tk.BOTH)

tree["columns"]=("date","filetype","size")
tree.column("#0", width=270, minwidth=270, stretch=tk.NO)
tree.column("date", width=150, minwidth=150, stretch=tk.NO)
tree.column("filetype", width=400, minwidth=200)
tree.column("size", width=80, minwidth=50, stretch=tk.NO)

tree.heading("#0",text="Name",anchor=tk.W)
tree.heading("date", text="Date modified",anchor=tk.W)
tree.heading("filetype", text="Type",anchor=tk.W)
tree.heading("size", text="Size",anchor=tk.W)


def insert_dir(tree, tree_parent, folder):
	for elem in os.listdir(folder):
		elem_path = os.path.join(folder, elem)
		stat = os.stat(elem_path)
		date = datetime.datetime.fromtimestamp(stat.st_mtime)
		if os.path.isdir(elem_path):
			tree_elem = tree.insert(tree_parent, "end", text=elem, values=(date.strftime("%d.%m.%y %H:%M:%S"),"dir",stat.st_size))
			insert_dir(tree, tree_elem, elem_path)
		if os.path.isfile(elem_path):
			tree.insert(tree_parent, "end", text=elem, values=(date.strftime("%d.%m.%y %H:%M:%S"), os.path.splitext(elem_path)[1], stat.st_size))



folder = os.path.join(os.path.curdir, "..")
print(folder)
insert_dir(tree, "", folder)

root.mainloop()
