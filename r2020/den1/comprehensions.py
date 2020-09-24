
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


gen1 = infinite_sequence()

next(gen1)

gen3 = (i**2 for i in range(5))

for g in gen3:
    print(g)
