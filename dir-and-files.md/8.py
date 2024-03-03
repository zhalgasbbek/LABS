import os
if os.path.exists('bad.txt'):
    os.remove('bad.txt')
    
    
import os
file = input()
if os.path.exists(file):
    os.remove(file)