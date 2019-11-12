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
from tkinter import Tk, Frame
root = Tk()
frame = Frame(root)

root.mainloop()
```

#### Geometry of Widgets
* pack - expand widgets as big as possible
* grid - align widgets to grid
* place - exact absolute position
TODO example + exercise

#### Button
```python
from tkinter import Button
button = Button(parent, text="Click me", command=clickButtonCb)
button.place(x=0, y=0)
```

#### Example
* colorButtons.py

#### Exercise 


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

#### Tk vs. ttk
TODO


#### Image
```python
load = Image.open("parrot.jpg")
render = ImageTk.PhotoImage(load)
```

TODO
https://pythonbasics.org/#Tkinter
https://www.tutorialspoint.com/python/tk_frame.htm
https://www.root.cz/clanky/graficke-uzivatelske-rozhrani-v-pythonu-knihovna-tkinter/


#### Exercise
https://projekty.pyladies.cz/session?course=pyladies-2019-ostrava-podzim&session=loops


#### QT
https://pythonbasics.org/

## threading + asyncio
https://realpython.com/intro-to-python-threading/
https://realpython.com/quizzes/python-threading/
https://realpython.com/async-io-python/

* todo: dva tasky, jeden spustí call_later v náhodném čase a druhý se bude ravidelně ptát kdy to bude spuštěné


## Database support


DB API
ODBC
Native Python databases
* mysqlclient


## Web server
flask + celery + db
- flask: registrovat nový task, prohlížení všech tasků (běžící + hotové)
- db: table task (id, name, time_taken, status)
- dlouhé tasky spouštět v celery


## Online resources
Books
Tutorials
IDEs
