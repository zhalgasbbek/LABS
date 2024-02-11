#Will be ERROR
"""txt = "We are the so-called "Vikings" from the north."
"""


txt = "We are the so-called \"Vikings\" from the north."


"""
\'	Single Quote
txt = 'It\'s alright.'
print(txt) 	
It's alright.

\\	Backslash
	txt = "This will insert one \\ (backslash)."
print(txt) 
  This will insert one \ (backslash).
   
\n	New Line
	txt = "Hello\nWorld!"
      print(txt) 
    Hello
    World!

\r	Carriage Return	
txt = "Hello\rWorld!"
print(txt) 
Hello
World!

\t	Tab	
txt = "Hello\tWorld!"
print(txt) 
Hello   World!

\b	Backspace	
#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt)
HelloWorld!

\f	Form Feed	

\ooo	Octal value	
#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 
Hello

\xhh	Hex value
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 
Hello
"""