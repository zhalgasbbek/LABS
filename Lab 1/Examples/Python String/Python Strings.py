print("Hello")
print('Hello')


a = "Hello"
print(a)


#You can assign a multiline string to a variable by using three quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


#Or three single quotes:
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


a = "Hello, World!"
print(a[1])


for x in "banana":
    print(x)
    
    
a = "Hello, World!"
print(len(a))


txt = "The best things in life are free!"
print("free" in txt)


txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
    
    
txt = "The best things in life are free!"
print("expencive" not in txt)


txt = "The best things in life are free!"
if "expencive" not in txt:
    print("No, 'expensive' is NOT present")

    
