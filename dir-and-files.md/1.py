import os

current_directory = os.getcwd()
"""
Эта строка вызывает функцию os.getcwd(), которая возвращает путь к текущей рабочей директории. Затем этот путь сохраняется в переменной current_directory.
"""

# Получаем полный список всех директорий и файлов в текущей директории
all_entries = [os.path.join(current_directory, entry) for entry in os.listdir(current_directory)]
"""
Эта строка создает список all_entries, содержащий полные пути ко всем файлам и директориям в текущей рабочей директории. Она использует генератор списка и функцию os.listdir(), чтобы получить список всех элементов в текущей директории, а затем для каждого элемента присоединяет его к текущему пути с помощью os.path.join().
    """
# Фильтруем только директории и файлы
directories = [entry for entry in all_entries if os.path.isdir(entry)]
files = [entry for entry in all_entries if os.path.isfile(entry)]

# Выводим списки директорий и файлов
print("Only directories:", directories)
print("Only files:", files)

# Просто выводим весь список всех директорий и файлов
print("All directories and files:", all_entries)
