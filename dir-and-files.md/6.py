import string

# Generate the alphabet (uppercase)
alphabet = string.ascii_uppercase

# Iterate over each letter in the alphabet
for letter in alphabet:
    # Generate the file name (e.g., A.txt, B.txt, ..., Z.txt)
    file_name = letter + '.txt'
    
    # Open the file in write mode and write to it
    with open(file_name, 'w') as file:
        file.write(f'This is file {file_name}\n')
    
    print(f'File {file_name} has been created.')