import re

def split_at_uppercase(text):
    # Use re.findall() to find all occurrences of uppercase letters
    parts = re.findall('[A-Z][^A-Z]*', text)
    return parts

# Test the function
input_string = "SplitThisStringAtUppercaseLetters"
result = split_at_uppercase(input_string)
print( result)

#Конструкция "(?=pattern)" используется для создания условия, что после текущей позиции в строке должен следовать определенный шаблон pattern, но сам шаблон не входит в результат совпадения.