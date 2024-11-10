from operator import index

def Razgad(Word, Key):
    Word1 = ""
    for i in range(len(Word)):
        word_ind = alp.index(Word[i])
        key_ind = alp.index(Key[i % len(Key)])
        Word1 += alp[(word_ind - key_ind) % len(alp)]
    return Word1

def Zagad(Word, Key):
    Word2 = ""
    for i in range(len(Word)):
        word_ind = alp.index(Word[i])
        key_ind = alp.index(Key[i % len(Key)])
        Word2 += alp[(word_ind + key_ind) % len(alp)]
    return Word2

alp = "abcdefghijklmnopqrstuvwxyz"

word = str(input("Введите слово: "))
key = str(input("Введите ключ: "))

was = int(input("1 - расшифровать, 2 - расшифровать: "))
if was == 1:
    print("Получено слово ", Razgad(word, key))

elif was == 2:
    print("Получено слово", Zagad(word, key))