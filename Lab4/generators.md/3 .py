n = int(input())
def adal(n):
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i
divisible = adal(n)
for x in divisible:
    print(x)