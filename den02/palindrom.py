

def is_palindrom(n):
    s = str(n)
    return s == s[::-1]


def infinite_sequence(num):
    while True:
        yield num
        num += 1

def get_palindroms(begin_from, num_of_palindroms):
    g = infinite_sequence(begin_from)
    palindroms = []
    while len(palindroms) < num_of_palindroms:
        number = next(g)
        if is_palindrom(number):
            palindroms.append(number)
    return palindroms


print(get_palindroms(1001, 30))

