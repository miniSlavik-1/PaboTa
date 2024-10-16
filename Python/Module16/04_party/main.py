guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

was = ""
while was != "Пора спать":
    print("Сейчас на вечеринке", len(guests), "гостей:", guests)
    was = input("Гость пришёл или ушёл: ")
    if was == "пришёл":
        wer = input("Имя гостя: ")
        if len(guests) <= 6:
            guests.append(wer)
        else:
            print(f"Прости, {wer}, но мест нет")
    elif was == "ушёл":
        wer = input("Имя гостя: ")
        if wer in guests:
            guests.remove(wer)
        else:
            print("Такого гостя нет")



print("Вечеринка закончилась, все легли спать.")