x = ('apple','banana','cherry')
y = list(x)
y[1] = 'kiwi'
x = tuple(y)
print (x)

x = ('apple','banana','cherry')
y = list(x)
y.append('orange')
x = tuple(y)
print (x)

x = ('apple','banana','cherry')
y = ('orange',)
x+= y
print (x)

x = ('apple','banana','cherry')
y = list(x)
y.remove('banana')
x = tuple(y)
print (x)

x = ('apple','banana','cherry')
del x
print (x)
