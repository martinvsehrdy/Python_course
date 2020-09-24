a = int(input("First number: "))
b = int(input("Second number:"))
op = input("Operation:")

if op in ("+", "-", "*", "/"):
    if op == "+":
        res = a + b
    elif op == "-":
        res = a - b
    elif op == "*":
        res = a * b
    elif op == "/":
        res = a / b
    print(f"{a} {op} {b} = {res}")
else:
    print("Unknown operation")



calc = f"{a} {op} {b}"
print(f"{calc} = {eval(calc)}")
