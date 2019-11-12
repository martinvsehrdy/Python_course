
ops = {
    "+": (lambda a, b: a + b),
    "-": (lambda a, b: a - b),
}
ops = {"+": (lambda a, b: a + b), "-": (lambda a, b: a - b)}
a = float(input("Zadej cislo: "))
b = float(input("Zadej cislo: "))
op = input("Operator: ")

def add(a, b):
    return a + b

ops[op](a, b)


if op == "+":
    print(f"{a} + {b} = {a + b}")
elif op == "-":
    print(f"{a} - {b} = {a-b}")
elif op == "*":
    print(f"{a} * {b} = {a * b}")
elif op == "/":
    print(f"{a} / {b} = {a / b}")
else:
    print("neznamy operator")

