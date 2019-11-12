

def generator(n):
    for i in range(n):
        print("in gen ", i)
        if i < 5:
            yield i
    yield 100


g = generator(10)
print(g)


for i in g:
    print("next", i)



