import os

current_path = os.getcwd()

def check_for_existence(some_path):
    if os.access(some_path, os.F_OK):
        print(os.listdir(current_path))
    else:
        print("Указанный путь не существует")

check_for_existence(current_path)



import os

def check_for_existence(some_path):
    if os.path.exists(some_path):
        directory, filename = os.path.split(some_path)
        print("Directory portion:", directory)
        print("Filename portion:", filename)
    else:
        print("Указанный путь не существует")

# Get the specified path from the user
path = input("Введите путь: ")

# Check if the path exists and find filename and directory portions
check_for_existence(path)
