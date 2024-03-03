import os

current_directory = os.getcwd()

# Проверка доступности текущей рабочей директории
existence = os.access(current_directory, os.F_OK)   #проверяется существование пути
readability = os.access(current_directory, os.R_OK) #доступность для чтения пути
writability = os.access(current_directory, os.W_OK) #доступность для записи пути
executability = os.access(current_directory, os.X_OK)  #доступность для выполнения пути 

# Вывод результатов проверки доступности
print(f"Check for accessibility:\nExistence: {existence} \nReadability: {readability} \nWritability: {writability} \nExecutability: {executability}")

"""
Для проверки доступа к файлам и директориям в Python используются следующие константы:

os.F_OK: Проверяет доступ к файлу или директории вообще.
os.R_OK: Проверяет доступ на чтение файла или директории.
os.W_OK: Проверяет доступ на запись в файл или директорию.
os.X_OK: Проверяет доступ на выполнение файла или директории.

"""