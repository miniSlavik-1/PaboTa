violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

singen = int(input("Сколько песен выбрать? "))
Uhr = 0.0
for i in range(singen):
    print("Название", str(i + 1) + "-й песни: ", end=" ")
    s = input("")
    for i in violator_songs:
        if i[0] == s:
            Uhr += i[1]

print("Общее время звучания песен:", Uhr, "минуты")