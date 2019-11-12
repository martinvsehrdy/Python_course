

def get_letter_dict(text):
    d = {}
    for t in text:
        if d.get(t):
            d[t] += 1
        else:
            d[t] = 1
    return d

    return {t: d.get(t, 0) + 1 for t in text}




if __name__ == '__main__':
    text = "Napiš funkci, která jako argument dostane řetězec a vrátí slovník, ve kterém budou jako klíče jednotlivé znaky ze zadaného řetězce a jako hodnoty počty výskytů těchto znaků v řetězci."
    letters = get_letter_dict(text)
    print(letters)
