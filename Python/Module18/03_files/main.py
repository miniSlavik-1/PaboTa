name = input("Название файла: ")
if name[0] in "@№$%^&\*()":
    print("Ошибка: название начинается на один из специальных символов")
else:
    if name[-4::] != ".txt" and name[-5::] != ".docx":
        print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx")
    else:
        print("Файл назван верно")