def chastot(text):
    slovo = {}
    for j in text:
        slovo[j] = text.count(j)
    return slovo

text = input("")
print(chastot(text))