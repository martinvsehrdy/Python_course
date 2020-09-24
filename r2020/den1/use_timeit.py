from timeit import timeit


mysetup = "from math import sqrt"

print(timeit("map(sqrt, range(100))", setup=mysetup, number=1000))
print(timeit("list(map(sqrt, range(100)))", setup=mysetup, number=1000))
print(timeit("[sqrt(a) for a in range(100)]", setup=mysetup, number=1000))



