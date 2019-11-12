

d = {
    1: "one",
    2: "two",
    3: "three",
}

c = {
'Tokyo': (16000000, "Mc Donald"),
'New York': 20000000,
}

print(c['Tokyo'][1])


cities = ['Tokyo','New York','Toronto','Hong Kong']

def fce(*args, **kwargs):
    print(args)
    print(kwargs)


fce("LL", 3, prom=2)




print({*cities})



print(*cities)

print(cities[0], cities[1])