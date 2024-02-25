import re

def camel_to_snake(camel_case):
    snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case).lower()
    return snake_case

# Test the function
camel_case_string = "ThisIsCamelCaseString"
snake_case_string = camel_to_snake(camel_case_string)
print("Camel case string:", camel_case_string)
print("Snake case string:", snake_case_string)