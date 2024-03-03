import os
with open('TSIS\Lab6\dir-and-files.md\inform.text', 'r') as f:
    x = sum(1 for i in f)
print(x)