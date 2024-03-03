import os
f = open('bad.txt', 'r')
with open('good.txt', 'w') as file:
    for x in f:
        file.write(x)

f.close()


