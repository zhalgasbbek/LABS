import os

# Записываем список в файл
lissst = list(input("Введите элементы списка через пробел: ").split())
with open('inform.txt', 'w') as f:
    for i in lissst:
        f.write(str(i) + '\n')

# Считываем и выводим содержимое файла
with open('inform.txt', 'r') as f:
    file_contents = f.read()
    print("Содержимое файла 'inform.txt':")
    print(file_contents)