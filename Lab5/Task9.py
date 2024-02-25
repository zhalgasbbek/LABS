import re

def insert_spaces(text):
    # Use re.sub() to insert a space before each word starting with a capital letter
    modified_text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    return modified_text

# Test the function
input_string = "ThisIsAStringWithWordsStartingWithCapitalLetters"
result = insert_spaces(input_string)
print("Modified text:", result)