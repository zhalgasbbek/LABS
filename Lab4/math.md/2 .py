import math
a= int(input("Height: "))
b= int(input("Base, first value: "))
h = int(input("Base, second value: "))
def areatrap(a , b , h):
    return  ((a+b)/2)*h
print("Expected Output:",areatrap(a , b,h))


height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))


area =  (base1 + base2)/2 * height

print("Expected Output:", area)