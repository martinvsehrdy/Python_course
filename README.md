![Python Logo](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

# Python Course

[//]: # (nenahrávejte online přenos)
[//]: # (kontakt na mě)
[//]: # (představení studentů, něco o sobě, jaké má zkušenosti)

[//]: # (todo
webserver: update timestamp in DB
webserver: update read_count 
pandas:change data between people <-> movies 
)

### Download tools we are using
* download [anaconda](https://www.anaconda.com/products/individual#Downloads)
* download [pycharm](https://www.jetbrains.com/pycharm/download) - Community edition is enough

### Agenda
| Chapter             | Duration          |
| ------------------- | ----------------- |
| Python Intro        | (40 min)          |
| Basic syntax        | (1 h)             |
| Built-in Functions  | (1 h)             |
| Code structure      | (2,5 - 3 h)       |
| Classes and objects | (3 h)             |
| Decorators          | (1 - 2 h)         |
| Working with files  | (1 h + 1 h)       |
| Tkinter             | (40 min + 1:20 h) |
| Database            | (30 min + 30 min) |
| Webserver Flask     | (1,5 h + 1,5 h)   |
| NumPy               | (1 h + 2 h)       |
| Pandas              | (1 h + 2 h)       |


## Python Intro
(40 min)
* Python was created in 1991
* By developer **Guido Van Rossum**
* friendly and easy to learn
* described as an interpreted and dynamic programming language
* focus on code readability

### Versions
* Python 2.7
* Python 3.8
* official website [python.org](https://www.python.org/)
* official documentation [docs.python.org](https://docs.python.org/3/)


* [Python Virtual Environment](https://docs.python.org/3/tutorial/venv.html)
* [Python Anaconda](https://www.anaconda.com/)

### Instalation & Environment
Create python environment
```shell script
conda create -n course python=3.8
```

De/Activate environment
```shell script
conda activate course
conda deactivate
```

All my environments
```shell script
conda env list
```

Install package
```shell script
pip freeze
pip install <package name>
```
or
```shell script
pip3 install -r requirements.txt
```

### IDE
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
(1 h)
### Data types
#### Basic Types
```python
None
int
float
str
bool
bytes
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

### Flow control
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
cities = ['Tokyo','New York','Toronto','Hong Kong']
print('Cities loop:')
for city in cities:
    print('City: ' + city)

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

## Built-in Functions
(1 h)
https://docs.python.org/3/library/functions.html
* input output: `print`, `input`, `open`
* basic types convertion: `str`, `int`, `float`, `bool`, `bytes`
* types and classes: `type`, `isinstance`, `issubclass`, `id`
* data structures: `list`, `set`, `dict`, `tuple`, `len`, `range`, `sorted`, `reversed`
  - usage with containers [bellow](####container-types)
* modification: `zip`, `enumerate`, `map`, `filter`
* agregation: `min`, `max`, `sum`, `all`, `any` 
* python execution: `exec`, `eval`


#### Exercises - calculator
(30 min)
* Program that get 2 numbers and string `+`, `-`, `*` or `/` and print result.
```shell script
First number: 12
Second number: 3
Operation: +
12 + 3 = 15
```
* Program that ask user for 5 numbers and print the smallest one.
* Program that is getting numbers until user puts number 0 and print sum of them

## Code structure
(2,5 - 3 h)
#### Functions
```python
def printCurrentYear():
    print('2018')

printCurrentYear()

def multiply(x,y):
    return x*y

result  = multiply(3,4)
print(result)
```
* lambda function
```python
identity_func = lambda x: x

identity_func(10)
map(lambda x: x + 1, [3, 7, 2]) # map object that contains [4, 8, 3]
```


#### Container Types
* list
```python
fruits = ["orange", "plum", "apple"]
fruits.append("pear")
fruits.append(5)
fruits.pop()
fruits[2]
fruits[-1]
"banana" in fruits  # find out if "banana" is in fruits 
fruits.sort()
# or using built-in sorted
sorted(fruits)
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
d.update({5: "five", 6: "six"})
d.items()
d.keys()
```

set
```python
s = {1, 2, 3}
s.intersection({1, 6})  # {1}
s.difference({1, 6})    # {2, 3}
s.add(6)
```

tuple
```python
t = (1, 2, "text", None)
t = (0, )
```

**indexing**
* pass begin, end and step `[begin:end]`, `[begin:end:step]`
* don't pass anything `[:end:step]`, `[begin::step]`, `[:]`, `[::]`
```python
l = [1, 2, 3, 4, 5, 6, 7]
l[1:5]    # [2, 3, 4, 5]
l[:4]     # [1, 2, 3, 4]
l[4:]     # [5, 6, 7]
l[::2]    # [1, 3, 5, 7]
```

**unpacking**
* unpack list/tuple
```python
l = [1, 2, 3]
a, b, c = l # a = 1, b = 2, c = 3
a, *b = l   # a = 1, b = [2, 3]
function(*l)    # function(1, 2, 3)
```

* unpack dict
```python
old = {"a": 1, "b": 2}
new = {**old, "c": 10}  # {"a": 1, "b": 2, "c": 10}
```

* unpack arguments and keyword arguments
```python
def function(*args, **kwargs):
    pass
# args -   list of arguments
# kwargs - dict of keyword arguments
```

#### Exercises - fruits
Lets have list of fruits: "plum", "apple", "pear", "apricot", "grape", "banana"
* write function that returns fruits that has name shorter than 6
* write function that returns fruits beginning "a"
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

#### Generators
* read large files
```python
def large_file_reader(file_name):
    for row in open(file_name, "r"):
        yield row
```
* infinite sequence
```python
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
```
* for-loop
```python
gen = iter(range(3))    # create generator(iterator) from range(3)
for _ in gen:
    pass
```
* next & StopIteration
```python
gen = iter(range(3))    # create generator(iterator) from range(3)
next(gen)   # 0
next(gen)   # 1
next(gen)   # 2
next(gen)   # StopIteration
```

#### Comprehensions
```python
print([i**2 for i in range(5)])     # list
print((i**2 for i in range(5)))     # generator
print({i: i**2 for i in range(5)})  # dict
print([i**2 for i in range(5) if i % 2 == 0])     # list
```

#### Benchmarking
**timeit**
```python
from timeit import timeit
mysetup = "from math import sqrt"

timeit("map(sqrt, range(100))", setup=mysetup, number=1000)
timeit("list(map(sqrt, range(100)))", setup=mysetup, number=1000)
timeit("[sqrt(a) for a in range(100)]", setup=mysetup, number=1000)
```
**cProfile**
* see more at https://docs.python.org/3.8/library/profile.html

#### Exercise - timeit
* lets have list of numbers, write a function that return list of square of them
  - use `map`
  - use comprehensions
  - use for loop 
* what lasts the longest?

#### Exercise - palindroms
 * palindrom is number that is read left to right some as right to left
 * create function `get_palindroms(begin_from, num_of_palindroms)`
 
#### Exercise - poem
* Write program that print poem with reverse order of lines
* Write program that reverses order of words in each line
* Write program that reverses order of stanzas (separated by empty line)
* Print words of poem in random order


## Classes and objects
(3 h)
#### Define a Class
```python
class Dog:
    pass
```

#### Instance Attributes
* all classes creates objects
* object contains characteristic called attributes (properties)
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
def create_older_than(cls, dog):
    return cls(dog.name, dog.age + 1)
```
#### Exercise - complex numbers
* create class ComplexNumber so that we can use operators
 `+`, `-`, `*`, `/`, `str`, `len`, `==` 

#### Create Instances of Objects
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

#### Abstract Base Class
* abstract class and abstractmethod
```python
from abc import ABC, abstractmethod

class AbstractClass(ABC):   # defines interface
    @abstractmethod
    def fce(self):
        pass

class DerivedClass(AbstractClass):
    def fce(self):      # must be defined
        super().fce()   # call method of parent class

AbstractClass()     # TypeError: Can't instantiate abstract class AbstractClass with abstract methods fce
DerivedClass()      # ok
```

* type or isinstance
```python
class BaseClass:
    pass

class DerivedClass(BaseClass):
    pass

derived = DerivedClass()

type(derived) == DerivedClass       # True
type(derived) == BaseClass          # False
isinstance(derived, DerivedClass)   # True
isinstance(derived, BaseClass)      # True
```

#### Built-in type, isinstance, issubclass

#### Exercise - Pets
* number of dogs (#instances)
* number of cats (#instances)
* last created pet `Pet.lastPet()`


#### Exercise - Shapes
* create class Shape with methods:
  - area - surface of shape
  - length - the biggest length in any direction
  - expand - expands shape but keep ratio
* create classes Circle, Rectangle and Line inherited from Shape
* create properties (getter and setter) center, size, left_top, right_bottom

## Decorators
(1 - 2 h)
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
  - not to run during night (or during odd minutes)
  - to measure and print time that function takes
  - debug decorator that print when function is called and its args
  - slow down function - time.sleep(1) before calling function
  - `register` that register functions and count how many times were called 

## Working with files
(1 h + 1 h)
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
os.makedirs('r2019/11/11', mode=0o770)
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
(30 min)
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
(40 min + 1:20 h)
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
mb = Menubutton (top, text="GfG") 
mb.grid() 
mb.menu = Menu (mb, tearoff=0) 
mb["menu"] = mb.menu 
cVar = IntVar() 
aVar = IntVar() 
mb.menu.add_checkbutton(label='Contact', variable=cVar) 
mb.menu.add_checkbutton(label='About', variable=aVar) 
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

### TreeView
```python
import tkinter as tk
from tkinter import ttk
master = tk.Tk()
tree=ttk.Treeview(master)

tree["columns"]=("one","two","three")
tree.column("#0", width=270, minwidth=270, stretch=tk.NO)
tree.column("one", width=150, minwidth=150, stretch=tk.NO)
tree.column("two", width=400, minwidth=200)
tree.column("three", width=80, minwidth=50, stretch=tk.NO)

tree.heading("#0",text="Name",anchor=tk.W)
tree.heading("one", text="Date modified",anchor=tk.W)
tree.heading("two", text="Type",anchor=tk.W)
tree.heading("three", text="Size",anchor=tk.W)

# Level 1
folder1=tree.insert("", 1, text="Folder 1", values=("23-Jun-17 11:05","File folder",""))
tree.insert("", 2, text="text_file.txt", values=("23-Jun-17 11:25","TXT file","1 KB"))
# Level 2
tree.insert(folder1, "end", text="photo1.png", values=("23-Jun-17 11:28","PNG file","2.6 KB"))
tree.insert(folder1, "end", text="photo2.png", values=("23-Jun-17 11:29","PNG file","3.2 KB"))
tree.insert(folder1, "end", text="photo3.png", values=("23-Jun-17 11:30","PNG file","3.1 KB"))
```
![TreeView](https://i.stack.imgur.com/2Mzp2.png)

### Delay Event
```python
def event():
    pass

widget.after(1000, event)
```
### Binding events
```python
def move(event):
    pass

widget.bind("<Enter>", move)
```

### Events and Binding
http://tkinter.programujte.com/tkinter-events-and-bindings.htm

#### Exercises
* clock
  - clock in format 10:40:27
  - changing each second
  - change time format in menu
* file manager
  - choose directory at the beginning
  - read files and dirs and display it in treeview
* catch the button
  - create button (or label, image)
  - bind event 'Enter' to button
  - create more of them


## Database
(30 min + 30 min)

### Database clients
**MySQL**

https://pypi.org/project/mysqlclient/

**PostgreSQL**

https://pypi.org/project/psycopg/


**MS SQL Server**

http://www.pymssql.org/en/stable/

**SQLite**

https://pypi.org/project/pysqlite3/

### Install SQLite
```bash
pip install pysqlite3
```
### Connecting to database
* connect to DB in file, or create it
* create DB in memory when `db_file == ":memory:"`
* `conn` is object `Connection`
```python
import sqlite3
db_file = "database.db"
conn = sqlite3.connect(db_file)
conn.close()
```

### Create table and insert
* create connection using `connect()`
* create cursor by `cursor()`
* execute query `cursor.execute()`
* save data to file `conn.commit()`

```python
query = "INSERT INTO table () VALUES (...)"
cursor = conn.cursor()
cursor.execute(query)
conn.commit()
conn.close()
```

#### Prepared statement
```python
data = ('title', '2015-01-01')
datas = [data, ]
query = "INSERT INTO table (title, date) VALUES (?, ?)"
cursor.execute(query, data)
cursor.executemany(query, datas)
```

### Querying database
* create connection using `connect()`
* create cursor by `cursor()`
* pass query by `execute()`
* get result by `fetchone` or `fetchall`

```python
query = "SELECT * FROM table ..."
cursor = conn.cursor()
cursor.execute(query)
cursor.fetchone()   # return tuple (according to row)
cursor.fetchall()   # return list of tuple
```

#### Exercises
* download database.db
* select all authors
* select all articles of one of them
* append yourself as author to DB

```bash
sqlite> .tables
author  article
```

|cid | name  | type     | notnull | dflt_value | pk   |
|----|-------|----------|---------|------------|------|
| 0  | id    | integer  | 0       |            |  1   |
| 1  | name  | CHAR(50) | 0       |            |  0   |

| cid | name       | type      | notnull | dflt_value | pk |
|-----|------------|-----------|---------|------------|----|
| 0   | id         | integer   | 0       |            | 1  |
| 1   | title      | CHAR(100) | 0       |            | 0  |
| 2   | text       | text      | 0       |            | 0  |
| 3   | author_id  | integer   | 0       |            | 0  |
| 4   | timestamp  | TIMESTAMP | 0       | CURRENT_TI | 0  |
| 5   | read_count | integer   | 0       | 0          | 0  |


## Webserver Flask
(1,5 h + 1,5 h)
* Flask is webserver that is easy to be used.

https://flask-doc.readthedocs.io/en/latest/

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Huray, there is first web page !'

if __name__ == '__main__':
    app.run()
```

We registered the view `index` with route '/'. On URL '/' will be content that is returned by function `index`.

#### Kinds of executions
* debug/deploy mode
* host + port
```python
app.run(host="0.0.0.0", port=8000, debug=True)
```

#### Dynamic Routes
**part of route is variable**
```python
@app.route('/user/<username>/')
def profile(username):
    return f"User {username}"
```

**exact type of route variable**
```python
@app.route('/post/<int:post_id>/')
def view(): pass
```

**Even more routes**
```python
@app.route('/hello/')
@app.route('/hello/<name>/')
def hello(name='world'):
    return f"Hello, {name}!"
```

#### Getting URLs
* opposite way to routes
```python
from flask import url_for
# ...
@app.route('/url/')
def show_url():
    return url_for("profile", username="martin_cerny")
```

#### Templates
We can use html pages like
```python
@app.route('/')
def hello():
    return '<html><head><title>...'
```
..but there will be lot of html codes. Better way is to separate html to separate files (templates).

```python
from flask import render_template

@app.route('/hello/<name>/')
def hello(name=None):
    return render_template('hello.html', name=name)
```


* Templates are in [Jinja2](https://jinja.palletsprojects.com/en/2.10.x/templates/) language and includes:
  - html code
  - variables `{{ variable }}`
  - for loop `{% for %}` and `{% endfor %}`
  - conditions `{% if %}`, `{% else %}` and `{% endif %}`
```jinja2
<!doctype html>
<html>
    <head>
        <title>Hello from Flask</title>
    </head>
    <body>
        {% if name %}
            <h1>Hello {{ name }}!</h1>
            <a href="{{ url_for('hello') }}">Go back home</a>
        {% else %}
            <h1>Hello, World!</h1>
        {% endif %}
    </body>
</html>
```

#### Filters
Filters are functions that converts any type of data to str to print to html template.
```python
from datetime import datetime
from flask import render_template

@app.template_filter('time')
def convert_time(dt):
    return dt.strftime('%c')

@app.route('/date_example')
def date_example():
    return render_template(
        'date_example.html',
        created_at=datetime.now(),
    )
```
and in template, it is used like:
```jinja2
{{ created_at|time }}
```

# Data Analysis
## NumPy
(1 h + 2 h)
* NumPy is a python library used for working with
  - arrays, linear algebra, fourier transform and matrices
* NumPy stands for **Num**erical **Py**thon
* written in C/C++
* numpy array `ndarray` is up to 50x faster than regular `list` 


#### Installation and import
```bash
pip install numpy
```
```python
import numpy as np

print(np.__version__)   # check version

arr = np.array([1, 2, 3, 4, 5])
print(type(arr), arr)
```

#### N-dimensions array
* 0-D array - scalar
```python
np.array(42)
```
* 1-D array
```python
np.array([1, 2, 3, 4])
np.arange(4)    # array([0, 1, 2, 3])
```
* 2-D array - matrice
```python
np.array([[1, 2, 3], [4, 5, 6]])
```
* 3-D array
```python
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
```
* dimension of array
```python
arr = np.array([1, 2, 3, 4], ndmin=5)
# array([[[[[1, 2, 3, 4]]]]])
print(arr.ndim)
```

#### Array indexing
```python
import numpy as np

arr = np.array([1, 2, 3, 4])

arr[0]  # 1
arr[1]  # 2
arr[2] + arr[3] # 7
```

```python
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2]) # return 6 - why?
```
* negative indexing
```python
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
arr[1, -1]  # Last element from 2nd dim
```

#### Slicing Array
* pass begin, end and step `[begin:end]`, `[begin:end:step]`
* don't pass anything `[:end:step]`, `[begin::step]`, `[:]`
```python
arr = np.array([1, 2, 3, 4, 5, 6, 7])
arr[1:5]    # array([2, 3, 4, 5])
arr[:4]     # array([1, 2, 3, 4])
arr[4:]     # array([5, 6, 7])
arr[::2]    # array([1, 3, 5, 7])

arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
arr2[1, 1:4]    # array([7, 8, 9])
```

#### Data types
* NumPy has daty types
  - `i` integer
  - `b` boolean
  - `u` unsigned integer
  - `f` float
  - `c` complex float
  - `m` timedelta
  - `M` datetime
  - `O` object
  - `S` string
  - `U` unicode string
  - `V` void - fixed chunk of memory for other type

```python
import numpy as np

np.array([1, 2, 3, 4]).dtype    # dtype('int64')
np.array(['apple', 'banana', 'cherry']).dtype   # dtype('<U6')
np.array([1, 2, 3, 4], dtype='S').dtype # dtype('S1')

arr = np.array([1.1, 2.1, 3.1])
arr.astype('i').dtype     # dtype('int32')
arr.astype(int).dtype     # dtype('int64')
```

#### Copy vs. View
```python
import numpy as np

arr = np.array([1, 2, 3, 4])
arr_copy = arr.copy()
arr_view = arr.view()
arr[0] = 42
arr         # array([42,  2,  3,  4])
arr_copy    # array([ 1,  2,  3,  4])
arr_view    # array([42,  2,  3,  4])
```

#### Shape & reshape
```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8], ndmin=3)   # array([[[[[1, 2, 3, 4]]]]])
arr.shape   # (1, 1, 8)

arr.reshape(2, 4)  # array([[1, 2, 3, 4], [5, 6, 7, 8]])
arr.reshape(4, 2)  # array([[1, 2], [3, 4], [5, 6], [7, 8]])
```

#### Joining array
* concatenate 1d array
```python
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

np.concatenate((arr1, arr2))    # array([1, 2, 3, 4, 5, 6])
```
* concatenate and stack 2d array
```python
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

np.concatenate((arr1, arr2), axis=0)    # array([[1, 2], [3, 4], [5, 6], [7, 8]])
np.concatenate((arr1, arr2), axis=1)    # array([[1, 2, 5, 6], [3, 4, 7, 8]])

np.stack((arr1, arr2), axis=0)    # array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
np.stack((arr1, arr2), axis=1)    # array([[[1, 2], [5, 6]], [[3, 4], [7, 8]]])
np.stack((arr1, arr2), axis=2)    # array([[[1, 5], [2, 6]], [[3, 7], [4, 8]]])
```

#### Search
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

indexes_of_4 = np.where(arr == 4)   # (array([3, 5, 6],)
arr[indexes_of_4]  # array([4, 4, 4])
```

#### Specific arrays
* ones - array where every value is equal to 1
* zeros - array where every value is equal to 0
* identity - array where diagonal value is equal to and others 0
* random - array with random values
* choice - array that consists of the values from given array
```python
import numpy as np
np.ones((2, 3))
np.zeros((2, 3))
np.eye(3)
np.random.randint(100, size=(3, 5))
np.random.choice([3, 5, 7, 9], size=(3, 5))
```

### Exercise
[//]: # (https://www.w3resource.com/python-exercises/numpy/index.php)
* create an array of 10 zeros,10 ones, 10 fives
* create a vector with values ranging from 15 to 55 and print all values except the first and last
* create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15
* multiply the values of two given vectors
* create a 10x10 matrix, in which the elements on the borders will be equal to 1, and inside 0
* compute sum of all elements, sum of each column and sum of each row of a given array
* save two given arrays into a single file in compressed format (.npz format) and load it
* convert a given array into bytes, and load it as array
* sort a given array of shape 2 along the first axis, last axis and on flattened array
  - original array: [[10 40], [30 20]]
  - sorted along the first axis: [[10 20], [30 40]]
  - sorted the array along the last axis: [[10 40], [20 30]]
  - sorted the flattened array: [10 20 30 40]


## Pandas
(1 h + 2 h)
 * the most important tool of Data Scientists
 * clean, transform and analyze data
 * calculate statistics and answer questions about the data
 * the name pandas is derived from **pan**el **da**ta
 * built on top of numpy

#### Instalation and import
```bash
pip install pandas
# OR
conda install pandas
```
```python
import pandas as pd
```

#### Core components of pandas
* Series - essentially a column
* DataFrame - multi-dimensional table, collection of Series

#### DataFrame from scratch
* key-value item corresponds to a column in DataFrame
```python
data = {
    'apples': [3, 2, 0, 1], 
    'oranges': [0, 3, 7, 2]
}
pd.DataFrame(data)
```
```bash
   apples  oranges
0       3        0
1       2        3
2       0        7
3       1        2
```
* let's have customer names as our index
```python
df = pd.DataFrame(data, index=['Jane', 'Robert', 'Lily', 'David'])
```
```bash
        apples  oranges
Jane         3        0
Robert       2        3
Lily         0        7
David        1        2
```
* locate a customer's order by using their name (index)
```python
df.loc['Jane']
```
```bash
apples     3
oranges    0
Name: June, dtype: int64
```

#### How to read in data
* from/to CSVs
```python
df = pd.read_csv('purchases.csv')
# ... working with DataFrame
df.to_csv('new_purchases.csv')
```
* from/to JSON
```python
df = pd.read_json('purchases.json')
# ... working with DataFrame
df.to_json('new_purchases.json')
```

* from/to database
```python
import sqlite3, pandas as pd

conn = sqlite3.connect("database.db")
df = pd.read_sql_query("SELECT * FROM purchases", conn)
# ... working with DataFrame
df.to_sql('new_purchases', conn)
```

#### Observing DataFrame
* load the IMDB movies dataset
```python
movies_df = pd.read_csv("pandas/IMDB-Movie-Data.csv", index_col="Title")
```

* view your data - few first/last rows
```python
movies_df.head()
movies_df.head(10)  # first 10 rows
movies_df.last()
movies_df.shape     # get shape - the some as numpy
```
* getting info about DataFrame
```python
movies_df.info()
```

#### Duplicates
* duplicate all rows
```python
temp_df = movies_df.append(movies_df)

temp_df.shape   # (2000, 11)
```
* remove duplicates
```
temp_df = temp_df.drop_duplicates() # return the results
temp_df.shape   # (1000, 11)

temp_df.drop_duplicates(inplace=True)   # remove it in place
```

#### Column cleanup
* getting columns
```
movies_df.columns
```
* rename columns
```
movies_df.rename(columns={'Runtime (Minutes)': 'Runtime', 'Revenue (Millions)': 'Revenue_millions'}, inplace=True)
movies_df.columns

movies_df.columns = ['rank', 'genre', 'description', 'director', 'actors', 'year', 'runtime', 'rating', 'votes', 'revenue_millions', 'metascore']
# OR
movies_df.columns = [col.lower() for col in movies_df]
movies_df.columns
```

#### Missing values
* `isnull()` returns a DataFrame where each cell is either True or False
```
movies_df.isnull()
```
* count the number of nulls
```
movies_df.isnull().sum()
```

* removing null values
```
movies_df.dropna()
movies_df.dropna(axis=1)
```

* Imputation - replace null values by mean, median..
```
revenue = movies_df['revenue_millions']
revenue_mean = revenue.mean()
revenue.fillna(revenue_mean, inplace=True)
```

* some statistics
```
movies_df.describe()    # print count, mean, min, max..
movies_df['genre'].describe()   # it tells us there are 50 genres
movies_df['genre'].value_counts().head(10)  # 10 top genres
```

#### DataFrame slicing, selecting, extracting
* by column
```
genre_col = movies_df['genre']
type(genre_col)     # pandas.core.series.Series

genre_col = movies_df[['genre']]
type(genre_col)     # pandas.core.frame.DataFrame
```
* by row `.loc`, `.iloc`
```
prom = movies_df.loc["Prometheus"]
prom    # info about Prometheus movie
# OR
prom = movies_df.iloc[1]
movie_subset = movies_df.iloc[1:4]
```
* by condition
```
condition = (movies_df['director'] == "Ridley Scott")
condition.head()    # list of True or Flase

movies_df[movies_df['director'] == "Ridley Scott"]  # movies of "Ridley Scott"
```
  - OR `|`, AND `&`
  - is in `movies_df.isin()`
  - quantile `movies_df.quantile(0.25)`

#### Applying functions
```
movies_df["squared_rating"] = movies_df["rating"].apply(lambda x: x**2)
```

#### Brief Plotting
* install `pip install matplotlib`

```
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)}) # set font and plot size to be larger
```
* plotting DataFrame
```
movies_df.plot(kind='scatter', x='rating', y='revenue (millions)', title='Revenue (millions) vs Rating')
movies_df['rating'].plot(kind='hist', title='Rating')
movies_df['rating'].describe()  # these data are plotted
```


### Exercise - dataframe
[//]: # (https://www.w3resource.com/python-exercises/pandas/index.php)
* download json file `pandas/dataframe_people.json`
* create DataFrame from file which has the index labels
* append a new row 'k' to data frame with given values for each column than delete the new row and return the original DataFrame.
  - name : "Suresh", score: 15.5, attempts: 1, qualify: "yes", label: "k"
* sort the DataFrame first by 'name' in descending order, then by 'score' in ascending order.
* replace the 'qualify' column contains the values 'yes' and 'no' with True and False
* change the name 'James' to 'Suresh' in name column of the DataFrame.
* delete the 'attempts' column and insert a new column 'color' in DataFrame
* count the NaN values in one or more columns in DataFrame
* replace all the NaN values with Zero's in a column of a dataframe
* shuffle a given DataFrame rows
* get the datatypes of columns of a DataFrame
* convert the datatype of a given column (floats to ints)


## Other Links
* Official Python website (https://www.python.org/)
* [Pyvo](https://pyvo.cz/)
  - Czech Python community
* [PyLadies](https://pyladies.cz/praha/)
  - Python courses for beginners (:girl:)
* [PyCon](https://pycon.org/) - Python Conference
  - [PyCon 2017 on youtube](https://www.youtube.com/channel/UCrJhliKNQ8g0qoE_zvL8eVg)
  - [PyCon 2018 on youtube](https://www.youtube.com/channel/UCsX05-2sVSH7Nx3zuk3NYuQ)
  - [PyCon 2019 on youtube](https://www.youtube.com/channel/UCxs2IIVXaEHHA4BtTiWZ2mQ)
* [PyData](https://pydata.org/)
  - [PyData on youtube](https://www.youtube.com/user/PyDataTV)
