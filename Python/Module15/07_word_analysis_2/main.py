word = input("Введите слово: ")
revers = word[::-1]
if revers == word:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")