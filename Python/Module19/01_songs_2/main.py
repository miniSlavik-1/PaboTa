def songs(n):
    long = 0.0
    for i in range(n):
        a = input("Название песни: ")
        if a in violator_songs:
            long += violator_songs[a]
    return long


violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

n = int(input("Сколько песен выбрать? "))
print(songs(n))