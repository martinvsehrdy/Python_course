# Python
![Python Logo](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

## Python Intro
* Python was created in 1991
* By developer **Guido Van Rossum**
* friendly and easy to learn
* described as an interpreted and dynamic programming language
* focus on code readability

todo https://pyladies.cz/praha/
### Versions
* Python 2.7
* Python 3.8
* [python.org](https://www.python.org/)


* [Python Virtual Environment](https://docs.python.org/3/tutorial/venv.html)
* [Python Anaconda](https://www.anaconda.com/)

### Instalation & Environment
Create python environment
```shell script
conda create -n py38 python=3.8
```

De/Activate environment
```shell script
conda activate py38
conda deactivate
```

All my environment
```shell script
conda env list
```

Install packages
```shell script
pip freeze
pip install <package name>
```
or
```shell script
pip3 install -r requirements.txt
```

## IDE
[PyCharm](https://www.jetbrains.com/pycharm/)

[Eclipse + PyDev](https://www.pydev.org/)

[Sublime Text](http://www.sublimetext.com)

[Atom](https://atom.io/)

[Vi / Vim](https://www.vim.org/)

[Visual Studio + PTVS](https://microsoft.github.io/PTVS/)

### JetBrain: PyCharm
![](https://d3nmt5vlzunoa1.cloudfront.net/pycharm/files/2019/05/EAP-1-Restyle.png)
* [Shortcuts in PDF](https://resources.jetbrains.com/storage/products/pycharm/docs/PyCharm_ReferenceCard.pdf)
* new project
* Settings

## Basic syntax
### Data types
#### Basic Types
```python
None
int
float
str
bool
```
* strings operations
```
s = "long text string"
len(s)
s.split(" ")
s.find("text")
s.join(["a", "b", "c"])
f""
```
* convert between them ( type, id )

#### Numbers
* math operation
* int <-> float
* plus, minus, div, mod
* const Math.PI

#### String
* split, join, find
* format
```python

```

## Flow control
#### Conditions
```python
gender = input("Gender? ")
if gender.lower() == "male":
    print("Your cat is male")
else:
    print("Your cat is female")

age = int(input("Age of your cat? "))
if age < 5:
    print("Your cat is young.")
else:
    print("Your cat is adult.")
```
#### For Loops
```python
city = ['Tokyo','New York','Toronto','Hong Kong']
print('Cities loop:')
for x in city:
    print('City: ' + x)

print('\n')  # newline

num = range(10)
print('x^2 loop:')
for x in num:
    y = x * x
    print(f"{x} * {x} = {y}")
```

#### While Loops
```python
x = 3                              
while x < 10:
    print(x)
    x = x + 1

while True:
    x = input("Put positive number (0 indicates end)")
    if x == 0:
        break
```

### Built-in Functions
https://docs.python.org/3/library/functions.html

#### Exercises - calculator
* Program that get 2 numbers and string `+`, `-`, `*` or `/` from and print result.
```shell script
First number: 12
Second number: 3
Operation: +
12 + 3 = 15
```
* Program that ask user for 5 numbers and print the smallest one.
* Program that is getting numbers sums them until user puts number 0

## Code structure
#### Functions
```python
def currentYear():
    print('2018')

currentYear()

def multiply(x,y):
    return x*y

result  = multiply(3,4)
print(result)
```
* lambda function


#### Container Types
array
```python
fruits = ["orange", "plum", "apple"]
fruits.append("pear")
fruits.append(5)
fruits.pop()
fruits[2]
fruits[-1]
fruits.sort()
```

dict
```python
d = {
    1: "one",
    2: "two",
    3: "three",
}
d["key"] = "value"
d["key"]
d.get("key")
d.items()
d.keys()
```

set
```python
s = {1, 2, 3}
s.add(6)
```

tuple
```python
t = (1, 2, "text", None)
t = (0, )
```

#### Exercises - fruits
Lets have list of fruits: "plum", "apple", "pear", "apricot", "grape", "banana"
* write function that returns fruits that has name shorter than 6
* write function that returns fruits beggining "a"
* write function that find out if given word is one of our fruit
  - return True or False
* write function that get 2 list of fruits and return
  - fruits that belongs to both list
  - fruits that belongs to first list but not to second
  - fruits that belongs to second list but not to first
* sort fruits in abc order, ignoring first letter


#### Exercise
Napiš funkci, která jako argument dostane řetězec a vrátí slovník, ve kterém budou jako klíče jednotlivé znaky ze zadaného řetězce a jako hodnoty počty výskytů těchto znaků v řetězci. A vypiš písmena podle počtu výskytů od největšího zastoupení v textu.

#### Exceptions
```python
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

try:
    result = x / y
except ZeroDivisionError:
    print("division by zero!")
else:
    print("result is", result) # when everything is OK
finally:
    print("executing finally clause") # everytime
```


#### Modules
* We have function, whatever in module `module.py`
```python
# module.py
def func():
    pass
```
* Lets import it from another file
```python
# program.py
import module

module.func()
```
OR
```python
from module import func

func()
```


#### Comprehensions
```python
print([i**2 for i in range(5)])     # list
print((i**2 for i in range(5)))     # generator
print({i: i**2 for i in range(5)})  # dict
print([i**2 for i in range(5) if i % 2 == 0])     # list
```

#### Benchmarking
```python
import cProfile

def function1(n):
    pass # variant 1

def function2(n):
    pass # variant 2

cProfile.run('function1(10000)')
```
* see more at https://docs.python.org/3.8/library/profile.html


#### Generators
* read large files
* infinite sequence
* is palindrom
* throw, close, send

```python
def large_file_reader(file_name):
    for row in open(file_name, "r"):
        yield row

a = range(5)

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
```
 #### Exercise - palindroms
 * palindrom is number that is read letf to right some as right to left
 * create function `get_palindroms(begin_from, num_of_palindrons)`
 
#### Exercise - poem
* Write program that print poem with reverse order of lines
* Write program that reverses order of words in each line
* Write program that reverses order of stanzas (separated by empty line)
* Print words of poem in random order


## Classes and objects
#### Define a Class
```python
class Dog:
    pass
```

#### Instance Attributes
* all classes creates objects
* object contains charasteristic called attributes (properties)
```python
class Dog:
    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

#### Class Attributes
* class attribute is common for all object of given class
```python
class Dog:
    # class attribute
    species = 'mammal'
    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
```
* create instances
* print, compare, equal

#### Instance, Static and Class method
```python
# instance method
def description(self):
    return f"{self.name} is {self.age} years old"

# instance method
def run(self, minutes=10):
    print(f"{self.name} is running for {minutes} minutes")

# instance method
def eat(self, food):
    print(f"{self.name} eats {food}")

@classmethod
def older_than(cls, dog):
    return cls(dog.name, dog.age + 1)
```
#### Exercise - complex numbers
* create class ComplexNumber so that we can use operators
 `+`, `-`, `*`, `/`, `str`, `len`, `==` 

#### Instantiating Objects
* instances of several Dogs
* compare them each other
* type
* change attr, class attr
* default value

#### Exercise
* the oldest dog
* add attribute energy
  - energy is between 0 and 100%
  - a minute of running decreases energy by 1%
  - if dog eats 'meat' energy go up by 10%
* add method is_hungry()
  - return True if energy is less than 25%

---

#### Object Inheritance
```python
# Parent class
class Pet:
    def eats(self):
        print("eats")
# Child class (inherits from Pet class)
class Dog(Pet):
    def haf(self):
        print("haf")

# Child class (inherits from Pet class)
class Cat(Pet):
    def mnau(self):
        print("mnau")
```

#### Exercise - Pets
* number of dogs (#instances)
* number of cats (#instances)
* last created pet `Pet.lastPet()`


#### Ecercise - Shapes
* create class Shape with methods:
  - area - surface of shape
  - length - the biggest length in any direction
  - expand - expands shape but keep ratio
* create classes Circle, Rectangle and Line inherited from Shape
* create properties (getter and setter) center, size, left_top, right_bottom
----

## Decorators
### Functions
Lets have easy function
```python
def add_one(number):
    return number + 1
```

#### First-class object
* **functions can be passed around and used as arguments**
```python
def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")
```
`Say_hello` and `be_awesome` are regular functions. `greet_bob` takes function and call it with arg `"Bob"`

#### Inner function
```python
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()
```
* What happens when we call `parent` function?
* Try to call `first_child` function

#### Return function from function
```python
def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me John"

    if num == 1:
        return first_child
    else:
        return second_child
```
* store functions from `parent` and call them

#### Simple Decorator
```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")
```

#### Exercise - decorators
* create and apply decorator
  - that runs function twice (or n-times)
  - not to run durring night (or during odd minutes)
  - to measure and print time that function takes
  - debug decorator that print when function is called and its args
  - slow down function - time.sleep(1) before calling function
  - `register` that register functions and count how many times were called 


#### Exercise - snake game
* Napiš funkci, která dostane seznam souřadnic (párů čísel menších než 10, která určují sloupec a řádek) a vypíše je jako mapu: mřížku 10×10, kde na políčka která jsou v seznamu napíše X, jinde tečku. Například:
```shell script
nakresli_mapu([(0, 0), (1, 0), (2, 2), (4, 3), (8, 9), (8, 9)])
X X . . . . . . . .
. . . . . . . . . .
. . X . . . . . . .
. . . . X . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . X .
```

* Jak na to?
  - Udělej tabulku (seznam seznamů) se samými tečkami, něco jako: `[['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]`.
  - Na příslušných místech nahraď tečky X-ky.
  - Tabulku vypiš pomocí dvou cyklů for zanořených do sebe.


* Napiš funkci pohyb, která dostane seznam souřadnic a světovou stranu ("s", "j", "v" nebo "z") a přidá k seznamu poslední bod „posunutý“ v daném směru. Např.:
```python
souradnice = [(0, 0)]
pohyb(souradnice, 'v')
print(souradnice)         # → [(0, 0), (1, 0)]
pohyb(souradnice, 'v')
print(souradnice)         # → [(0, 0), (1, 0), (2, 0)]
pohyb(souradnice, 'j')
print(souradnice)         # → [(0, 0), (1, 0), (2, 0), (2, 1)]
pohyb(souradnice, 's')
print(souradnice)         # → [(0, 0), (1, 0), (2, 0), (2, 1), (2, 0)]
```
  - Funkce by neměla nic vracet. Jen mění už existující seznam.


* Napiš cyklus, který se bude ptát uživatele na světovou stranu, podle ní zavolá pohyb, a následně vykreslí seznam jako mapu. Pak se opět se zeptá na stranu atd.
  - Začínej se seznamem [(0, 0), (1, 0), (2, 0)].


* Doplň funkci pohyb tak, aby při pohybu umazala první bod ze seznamu souřadnic. Výsledný seznam tak bude mít stejnou délku, jako před voláním.


* Doplň funkci pohyb tak, aby zamezila:
  - pohybu ven z mapy,
  - pohybu na políčko, které už v seznamu je.
  - Vhodná výjimka pro tyto situace je ValueError('Game over').


* Přidej do hry hadí potravu.

* Seznam ovoce obsahuje na začátku jedno ovoce na políčku, na kterém není had (například: [(2, 3)] znamená jedno ovoce na pozici (2, 3)). Když had sežere ovoce, vyroste („nesmaže“ se mu ocas, tedy neprovede se to, cos přidala v projektu 13), a pokud na mapě zrovna není další ovoce, na náhodném místě (kde není had) vyroste ovoce nové.

* Každých 30 tahů vyroste nové ovoce samo od sebe.

* Na mapě se toto tajemné ovoce zobrazuje jako otazník (?).

* Hadí hřiště může mít libovolné rozměry větší než 4×1. Třeba 20×20 nebo 10×30.


## Working with files
### module os

* os.listdir - list
* os.scandir - generator
* os.stat() - file attributes
* os.path.join()
* os.path.isfile()
* os.path.isdir()

### module pathlib
* pathlib.Path


#### Listing all files and all subdirectories
```python
import os

basepath = 'my_directory/'
for entry in os.listdir(basepath):  # or os.scandir
    if os.path.isfile(os.path.join(basepath, entry)):
        print("File: ", entry)
    if os.path.isdir(os.path.join(basepath, entry)):
        print("Directory: ", entry)
```

```python
from pathlib import Path

entries = Path('my_directory/')
for entry in entries.iterdir():
    if entry.is_file():
        print("File: ", entry.name)
    if entry.is_dir():
        print("Directory: ", entry.name)
```


#### Making Directories
```python
import os
os.mkdir()
os.makedirs('2019/11/11', mode=0o770)
```

```python
from pathlib import Path

p = Path('example_directory/')
p.mkdir()
```

#### Exercise
* create `ls -la` in Python
* create `tree` in Python

#### Filename Pattern Matching
* `endswith()` and `startswith()` string methods
```python
import os
for filename in os.listdir('some_directory'):
    if filename.endswith('.txt'):
        print(filename)
```

* `fnmatch.fnmatch()`
```python
import os
import fnmatch
for filename in os.listdir('some_directory'):
    if fnmatch.fnmatch(filename, '*.txt'):
        print(filename)
```

* `glob.glob()`
```python
import glob
glob.glob('**/*.py', recursive=True)
```

* `pathlib.Path.glob()`
```python
from pathlib import Path
p = Path('.')
for name in p.glob('*.p*'):
    print(name)
```

#### Achiving
```python
import zipfile

with zipfile.ZipFile('data.zip', 'r') as zipobj:
    bar_info = zipobj.getinfo('sub_dir/bar.py')
    bar_info.file_size
    # append file to ZIP
    for name in ["file1.txt", "file2.txt"]:
        zipobj.write(name)
```

#### Exercise
* create program like `find` with args
  - `-type` - distinguish file and dirs
  - `-name` - finds exact name
  - `-regex` - according to regular expression, module `re`
  - `-zip` - achive results to file `.zip`


# GUI frameworks
#### Tkinter
http://tkinter.py.cz/python_tkinter.html
  - the most popular programming package for graphical user interface
  - diverse widgets: labels, buttons, text boxes...

![Tkinter](https://www.tutorialsteacher.com/Content/images/python/window3.png)


#### QT
https://www.qt.io/qt-for-python
  - one of the most powerful and popular Python interfaces
  - combination of the Qt (owned by Nokia) library and Python
  - create visual dialogs by coding or using Qt Designer

![QT Designer](https://i.imgur.com/SgDylzb.png)


#### Kivy
https://kivy.org/#home
  - free and is an open source Python library
  - OpenGL ES 2 accelerated framework
  - cross platform

![Kivy](https://res.cloudinary.com/practicaldev/image/fetch/s--ipVf1ZK1--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://external-content.duckduckgo.com/iu/%3Fu%3Dhttps%253A%252F%252Fi.stack.imgur.com%252Fy6Hmq.png%26f%3D1%26nofb%3D1)


#### WxPython
https://www.wxpython.org/
  - traditional applications for Windows, Unix and Mac OS

![WxPython](https://res.cloudinary.com/practicaldev/image/fetch/s--0jSQuTij--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://external-content.duckduckgo.com/iu/%3Fu%3Dhttp%253A%252F%252Fwxglade.sourceforge.net%252Fimg%252Fwxglade_session.png%26f%3D1%26nofb%3D1)


## Tkinter
#### Tk
* widgets: frame, label, button...

```python
import tkinter 
m = tkinter.Tk() 
''' 
widgets are added here 
'''
m.mainloop() 
```
#### Geometry of Widgets
* **pack** expand widgets as big as possible
* **grid** align widgets to grid
* **place** exact absolute position

#### Button
* **activebackground** to set the background color when button is under the cursor.
* **activeforeground** to set the foreground color when button is under the cursor.
* **bg** to set he normal background color.
* **command** to call a function.
* **font** to set the font on the button label.
* **image** to set the image on the button.
* **width** to set the width of the button.
* **height** to set the height of the button.
![Button](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-68-300x67.png)

```python
import tkinter as tk 
r = tk.Tk() 
r.title('Counting Seconds') 
button = tk.Button(r, text='Stop', width=25, command=r.destroy) 
button.pack() 
r.mainloop() 
```

#### Canvas
* **bd** to set the border width in pixels.
* **bg** to set the normal background color.
* **cursor** to set the cursor used in the canvas.
* **highlightcolor** to set the color shown in the focus highlight.
* **width** to set the width of the widget.
* **height** to set the height of the widget.

![Canvas](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-68-1.png)
```python
from tkinter import *
master = Tk() 
w = Canvas(master, width=40, height=60) 
w.pack() 
canvas_height=20
canvas_width=200
y = int(canvas_height / 2) 
w.create_line(0, y, canvas_width, y ) 
mainloop() 
```

#### CheckButton
* **Title** To set the title of the widget.
* **activebackground** to set the background color when widget is under the cursor.
* **activeforeground** to set the foreground color when widget is under the cursor.
* **bg** to set he normal background color.
* **command** to call a function.
* **font** to set the font on the button label.
* **image** to set the image on the widget.

```python
from tkinter import *
master = Tk() 
var1 = IntVar() 
Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W) 
var2 = IntVar() 
Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W) 
mainloop() 
```
![CheckButton](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-68-2.png)

#### Entry
* **bd** to set the border width in pixels.
* **bg** to set the normal background color.
* **cursor** to set the cursor used.
* **command** to call a function.
* **highlightcolor** to set the color shown in the focus highlight.
* **width** to set the width of the button.
* **height** to set the height of the button.

```python
from tkinter import *
master = Tk() 
Label(master, text='First Name').grid(row=0) 
Label(master, text='Last Name').grid(row=1) 
e1 = Entry(master) 
e2 = Entry(master) 
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1) 
mainloop() 
```
![Entry](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-68-3.png)

#### Frame
* **highlightcolor** To set the color of the focus highlight when widget has to be focused.
* **bd** to set the border width in pixels.
* **bg** to set the normal background color.
* **cursor** to set the cursor used.
* **width** to set the width of the widget.
* **height** to set the height of the widget.
```python
from tkinter import *

root = Tk() 
frame = Frame(root) 
frame.pack() 
bottomframe = Frame(root) 
bottomframe.pack( side = BOTTOM ) 
redbutton = Button(frame, text = 'Red', fg ='red') 
redbutton.pack( side = LEFT) 
greenbutton = Button(frame, text = 'Brown', fg='brown') 
greenbutton.pack( side = LEFT ) 
bluebutton = Button(frame, text ='Blue', fg ='blue') 
bluebutton.pack( side = LEFT ) 
blackbutton = Button(bottomframe, text ='Black', fg ='black') 
blackbutton.pack( side = BOTTOM) 
root.mainloop() 
```
![Frame](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-68-4.png)


#### Label
* **bg** to set he normal background color.
* **bg** to set he normal background color.
* **command** to call a function.
* **font** to set the font on the button label.
* **image** to set the image on the button.
* **width** to set the width of the button.
* **height** to set the height of the button.
```python
from tkinter import *
root = Tk() 
w = Label(root, text='Python is the best !', font=("Helvetica", 18)) 
w.pack() 
root.mainloop()
```
![Label]()

#### ListBox
* **highlightcolor** To set the color of the focus highlight when widget has to be focused.
* **bg** to set he normal background color.
* **bd** to set the border width in pixels.
* **font** to set the font on the button label.
* **image** to set the image on the widget.
* **width** to set the width of the widget.
* **height** to set the height of the widget.
```python
from tkinter import *

top = Tk() 
Lb = Listbox(top) 
Lb.insert(1, 'Python') 
Lb.insert(2, 'Java') 
Lb.insert(3, 'C++') 
Lb.insert(4, 'Any other') 
Lb.pack() 
top.mainloop()
```
![ListBox](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-68-6.png)

#### MenuButton
* **activebackground** To set the background when mouse is over the widget.
* **activeforeground** To set the foreground when mouse is over the widget.
* **bg** to set he normal background color.
* **bd** to set the size of border around the indicator.
* **cursor** To appear the cursor when the mouse over the menubutton.
* **image** to set the image on the widget.
* **width** to set the width of the widget.
* **height** to set the height of the widget.
* **highlightcolor** To set the color of the focus highlight when widget has to be focused.
```python
from tkinter import *

top = Tk() 
mb = Menubutton ( top, text = &quot;GfG&quot;) 
mb.grid() 
mb.menu = Menu ( mb, tearoff = 0 ) 
mb[&quot;menu&quot;] = mb.menu 
cVar = IntVar() 
aVar = IntVar() 
mb.menu.add_checkbutton ( label ='Contact', variable = cVar ) 
mb.menu.add_checkbutton ( label = 'About', variable = aVar ) 
mb.pack() 
top.mainloop()
```

![MenuButton](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-68-8.png)

#### Menu
* **title** To set the title of the widget.
* **activebackground** to set the background color when widget is under the cursor.
* **activeforeground** to set the foreground color when widget is under the cursor.
* **bg** to set he normal background color.
* **command** to call a function.
* **font** to set the font on the button label.
* **image** to set the image on the widget.
```python
from tkinter import *
	
root = Tk() 
menu = Menu(root) 
root.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='New') 
filemenu.add_command(label='Open...') 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=root.quit) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About') 
mainloop()
```
![Menu](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-68-9.png)

### Message
* **bd** to set the border around the indicator.
* **bg** to set he normal background color.
* **font** to set the font on the button label.
* **image** to set the image on the widget.
* **width** to set the width of the widget.
* **height** to set the height of the widget.
```python
from tkinter import *
main = Tk() 
ourMessage ='This is our Message'
messageVar = Message(main, text = ourMessage) 
messageVar.config(bg='lightgreen') 
messageVar.pack( ) 
main.mainloop( ) 
```
![Message](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-68-10.png)

### RadioButton
* **activebackground** to set the background color when widget is under the cursor.
* **activeforeground** to set the foreground color when widget is under the cursor.
* **bg** to set he normal background color.
* **command** to call a function.
* **font** to set the font on the button label.
* **image** to set the image on the widget.
* **width** to set the width of the label in characters.
* **height** to set the height of the label in characters.
```python
from tkinter import *
root = Tk() 
v = IntVar() 
Radiobutton(root, text='GfG', variable=v, value=1).pack(anchor=W) 
Radiobutton(root, text='MIT', variable=v, value=2).pack(anchor=W) 
mainloop()
```
![RadioButton](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-68-11.png)

### Scale
* **cursor** To change the cursor pattern when the mouse is over the widget.
* **activebackground** To set the background of the widget when mouse is over the widget.
* **bg** to set he normal background color.
* **orient** Set it to HORIZONTAL or VERTICAL according to the requirement.
* **from**: To set the value of one end of the scale range.
* **to** To set the value of the other end of the scale range.
* **image** to set the image on the widget.
* **width** to set the width of the widget.
```python
from tkinter import *
master = Tk() 
w = Scale(master, from_=0, to=42) 
w.pack() 
w = Scale(master, from_=0, to=200, orient=HORIZONTAL) 
w.pack() 
mainloop()
```
![Scale](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-68-12.png)

### ScrollBar
* **width** to set the width of the widget.
* **activebackground** To set the background when mouse is over the widget.
* **bg** to set he normal background color.
* **bd** to set the size of border around the indicator.
* **cursor** To appear the cursor when the mouse over the menubutton.
```python
from tkinter import *
root = Tk() 
scrollbar = Scrollbar(root) 
scrollbar.pack( side = RIGHT, fill = Y ) 
mylist = Listbox(root, yscrollcommand = scrollbar.set ) 
for line in range(100): 
    mylist.insert(END, 'This is line number' + str(line)) 
mylist.pack( side = LEFT, fill = BOTH ) 
scrollbar.config( command = mylist.yview ) 
mainloop()
```
![ScrollBar](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-68-13.png)

### Text
* **highlightcolor** To set the color of the focus highlight when widget has to be focused.
* **insertbackground** To set the background of the widget.
* **bg** to set he normal background color.
* **font** to set the font on the button label.
* **image** to set the image on the widget.
* **width** to set the width of the widget.
* **height** to set the height of the widget.
```python
from tkinter import *
root = Tk() 
T = Text(root, height=2, width=30) 
T.pack() 
T.insert(END, "First line\nSecond line") 
mainloop()
```
![Text]()

### TopLevel
* **bg** to set he normal background color.
* **bd** to set the size of border around the indicator.
* **cursor** To appear the cursor when the mouse over the menubutton.
* **width** to set the width of the widget.
* **height** to set the height of the widget.
```python
from tkinter import *
root = Tk() 
root.title('GfG') 
top = Toplevel() 
top.title('Python') 
top.mainloop()
```
![TopLevel](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-68-15.png)

### SpinBox
* **bg** to set he normal background color.
* **bd** to set the size of border around the indicator.
* **cursor** To appear the cursor when the mouse over the menubutton.
* **command** To call a function.
* **width** to set the width of the widget.
* **activebackground** To set the background when mouse is over the widget.
* **disabledbackground** To disable the background when mouse is over the widget.
* **from**: To set the value of one end of the range.
* **to** To set the value of the other end of the range.
```python
from tkinter import *
master = Tk() 
w = Spinbox(master, from_ = 0, to = 10) 
w.pack() 
mainloop()
```
![SpinBox](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-68-16.png)

### PannedWindow
* **bg** to set he normal background color.
* **bd** to set the size of border around the indicator.
* **cursor** To appear the cursor when the mouse over the menubutton.
* **width** to set the width of the widget.
* **height** to set the height of the widget.
```python
from tkinter import *
m1 = PanedWindow() 
m1.pack(fill = BOTH, expand = 1) 
left = Entry(m1, bd = 5) 
m1.add(left) 
m2 = PanedWindow(m1, orient = VERTICAL) 
m1.add(m2) 
top = Scale( m2, orient = HORIZONTAL) 
m2.add(top) 
mainloop()
```
![PannedWindow](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-68-17.png)



#### Menu
```python
from tkinter import Menu
menu = Menu(parent)
fileMenu = Menu(menu)
fileMenu.add_command(label="Item")
fileMenu.add_command(label="Exit", command=exit)
menu.add_cascade(label="File", menu=fileMenu)
```

#### Label
```python
from tkinter import Label
label = Label(parent, text="Tkinter", fg="red", font=("Helvetica", 18))
```

#### Example
* clock like 10:40:27, changing each second
* in menu, change time format
* clock.py

### Events and Binding
http://tkinter.programujte.com/tkinter-events-and-bindings.htm
