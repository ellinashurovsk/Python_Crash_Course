# ЧТЕНИЕ ИЗ ФАЙЛА
with open('C:\\Users\\Эллина\\Desktop\\Python\\10\\pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())  # удаление лишней пустой строк

# ЧТЕНИЕ ПО СТОРОКАМ
with open('C:\\Users\\Эллина\\Desktop\\Python\\10\\pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())
