N = int(input("Enter a number: "))
def adal(N):
    for i in range(N , -1 , -1):
        yield i

for x in adal(N):
    print(x)


A = int(input("Enter a number: "))
def adal(A):
    
        while A>=0:
            yield A
            A-=1
            
for x in adal(N):
    print(x)