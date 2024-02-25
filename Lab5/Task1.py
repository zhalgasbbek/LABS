import re





def yes_or_no(sequence):
    pattern = r'ab*'
    if re.fullmatch(pattern, sequence):
        return True
    else :
        return False 

pattern = r'ab*'
sequence = 'abb'

print(yes_or_no(sequence))