def t9(text):
    text2 = ""
    for i in text:
        if i == "," or i == ".":
            text2 += " " + i + " "
        else:
            text2 += i
    list = text2.split()
    for i in range(len(list)):
        if i == 0 or list[i - 1] == ".":
            list[i] = list[i].capitalize()
    for i in range(len(list)):
        if i != 0 and list[i] != "." and list[i] != ",":
            list[i] = " " + list[i]
    res = "".join(list)
    return res

if __name__ == "__main__":
    print(t9("hello .hello,hello  . hello.  "))