
""""
class Adal:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <=20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
       
mynum = Adal()
myiter = iter(mynum)

for x in myiter:
    print(x)
   """ 
   
   
"""
n = int(input("Enter a number: "))
x = list(range(n))
z = []
for i in x:
    z.append(i**2)
print(z)
"""


'''
N = int(input("Enter a number: "))

class Adal:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= N:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

mynum = Adal()
myiter = iter(mynum)

for x in myiter:
    print(x**2)
'''

N = int(input("Enter a number: "))
def adal(N):
    for i in range(N):
        yield i**2

for x in adal(N):
    print(x)
