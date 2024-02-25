import re 


pattern = r'abbb?'
def yes_or_no(sequence):
    pattern = r'abbb?'
    return bool(re.fullmatch(pattern, sequence))


sequence = input()

print(yes_or_no(sequence))