import re

pattern = 'a.*b$'

def ok(sequence):
    pattern = 'a.*b$'
    return bool(re.fullmatch(pattern , sequence))

sequence = input()

print(ok(sequence))