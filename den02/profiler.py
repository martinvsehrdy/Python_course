import cProfile

from den01.fruit_list import fruits


def function1(n):
    a = []
    for i in range(1,n):
        a.append(45656 % i)
    return a

def function2(n):
    return [45656 % i for i in range(1, n)]

cProfile.run('function1(100000)')
cProfile.run('function2(100000)')

if __name__ == '__main__':
    print(function1(10))
    print(function2(10))
    print(fruits)