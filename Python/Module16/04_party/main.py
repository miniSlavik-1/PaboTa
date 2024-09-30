guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

was = ""
while was != "Пора спать":
    print("Сейчас на вечеринке", len(guests), "гостей:", guests)
    was = input("Гость пришёл или ушёл: ")
    if was == "пришёл":
        wer = input("Имя гостя: ")
        guests.append(wer)
    elif was == "ушёл":
        wer = input("Имя гостя: ")
        guests.remove(wer)

if len(guests) <= 6:
    print("Вечеринка закончилась, все легли спать.")
else:
    print("Отдохнуть сейчас не получится: рядом бродят монстры")