import time


def debug(func):
    def wrapper(*args, **kwargs):
        print(f"calling '{func.__name__}'({args}, {kwargs}")
        func(*args, **kwargs)
    return wrapper


def slow_down_delay(delay):
    def slow_down(func):
        def wrapper():
            time.sleep(delay)
            func()
        return wrapper
    return slow_down


@debug
def say_whee(a, b, option=None):
    print("Whee!")


say_whee(3, 4, option=10)
############


l = [1, 2, 3, 4, 5]
a, b, *c = l

print(a, b, c)

