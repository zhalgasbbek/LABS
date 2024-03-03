a = int(input("start number: "))
b = int(input("end number: "))
def squares(a ,b):
    for i in range(a,b+1):
        yield i**2

for x in squares(a,b):
    print(x)
