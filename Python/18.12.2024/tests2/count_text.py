def word(text):
    worder = {}
    for i in text:
        if i not in worder:
            worder[i] = 1
        else:
            worder[i] += 1

    return worder


def schifter(mass):
    return mass[::-1]


if __name__ == "__main__":
    text = input()
    print(word(text))