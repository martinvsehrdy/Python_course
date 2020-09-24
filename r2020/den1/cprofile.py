import cProfile

def func():
    pass


def function1(n):
    l = []
    for i in range(n):
        l.append(i ** 2)
    return l

def function2(n):
    return [i**2 for i in range(n)]


cProfile.run('function2(100)')
