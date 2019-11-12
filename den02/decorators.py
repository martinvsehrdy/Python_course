import time
import datetime

time.time()

now = datetime.datetime.now()
now.hour
now.minute
now.second

def not_during_night(func):
    def wrapper(*args, **kwargs):
        now = datetime.datetime.now()
        if now.hour < 22 and now.hour >= 8:
            return func(*args, **kwargs)
    return wrapper


def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        ret = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return ret
    return wrapper

def debug(func):
    def wrapper(*args, **kwargs):
        arguments = ', '.join(args)
        kw_arguments = ", ".join([f"{k}={v}" for k,v in kwargs.items()])
        print(f">>> {func.__name__}({arguments}, {kw_arguments})")
        ret = func(*args, **kwargs)
        print(ret)
        return ret
    return wrapper


@debug
def say_hello(*args, **kwargs):
    return f"Hello {args[0]}, Hi {kwargs['name']}"


s = say_hello("Alex", "John", name="Bob", jmeno="Petr")
print(s)

