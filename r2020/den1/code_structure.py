

def multiply(x,y=1):
    return x*y


multiply(3, 4)
multiply(5)

def printCurrentYear():
    print('2018')

res = printCurrentYear()
print(res)

identity_func = lambda x: x

identity_func(10)
map(lambda x: x + 1, [3, 7, 2]) # map object that contains [4, 8, 3]


sum_fce = lambda a, b: a + b
