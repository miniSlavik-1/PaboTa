def conserva(spis):
    new_spis = []
    for i in range(len(spis)):
        for j in range(len(spis[i])):
            for z in range(len(spis[i][j])):
                copy = spis[i][j][z]
                new_spis.append(copy)
    return new_spis


nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
print("Ответ:", conserva(nice_list))