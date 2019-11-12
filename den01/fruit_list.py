



def shorter_than(fruit_list, shorter):
    ret = []
    for fruit in fruit_list:
        if len(fruit) < shorter:
            ret.append(fruit)
    return ret

def shorter_than_better(fruit_list, shorter):
    return [fruit for fruit in fruit_list if len(fruit) < shorter]


def fruit_beginning_with(fruit_list, letter):
    ret = []
    for fruit in fruit_list:
        if fruit.startswith(letter):
            ret.append(fruit)
    return ret


def fruit_is_in_it(fruit_list, fruit):
    if fruit in fruit_list:
        return True
    return False

def in_both_list(fruits1, fruits2):
    return list(set(fruits1).intersection(set(fruits2)))

def in_first_but_second(fruits1, fruits2):
    return list(set(fruits1) - set(fruits2))

def in_second_but_first(fruits1, fruits2):
    return list(set(fruits2) - set(fruits1))

def sort_from_sec_letter(fruits_list):
    new_fruits = fruits_list.copy()
    new_fruits.sort(key=lambda x: x[1:])
    return new_fruits


fruits = ["plum", "apple", "pear", "apricot", "grape", "banana"]

print(__name__)
if __name__ == '__main__':
    print("Fruits shorter than 6", shorter_than(fruits, 6))
    print("A begining fruits", fruit_beginning_with(fruits, "a"))
    print("is kiwi in our fruits ", fruit_is_in_it(fruits, "kiwi"))
    print(in_both_list(fruits, ["banana", "apple", "kiwi"]))
    print(in_first_but_second(fruits, ["banana", "apple", "kiwi"]))
    print(in_second_but_first(fruits, ["banana", "apple", "kiwi"]))
    print(sort_from_sec_letter(fruits))
    print(shorter_than(fruits, 3))

