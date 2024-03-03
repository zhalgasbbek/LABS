import math

n= int(input("Input degree: "))
def torad(n):
    return n * math.pi/180
print("Output radian: " , torad(n))
