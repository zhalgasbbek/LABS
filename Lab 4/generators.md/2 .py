n = int(input("Введите число: "))

def adal(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i
evennum = adal(n)
for x in evennum:
    print(','.join(map(str,evennum)))



        
    

