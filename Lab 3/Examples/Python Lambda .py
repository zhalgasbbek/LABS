x = lambda a : a + 10
print(x(3))


x = lambda a, b : a * b
print(x(5, 4))


x = lambda a , b ,c : a + b +c
print(x(5 , 2 , 1))


def myfunction(n):
    return lambda a : a *n
mydoubler = myfunction(2)
print(mydoubler(11))


def myfunction(n):
    return lambda a : a *n
mydoubler = myfunction(2)
mytripler = myfunction(3)
print(mydoubler(11))
print(mytripler(11))