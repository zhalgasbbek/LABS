'''

\+?
\d?
[ ]?
[- (]?
\d{3}
[- )]?
[ ]?
\d{3}
[ -]?
\d{2}
[ -]?
\d{2}
[ .,\n]



\d - digit
\s - space
\w - [a - zA-Z0-9]

Квантификаторы - специальные символы сигнолизирующие щ том что последоветельность может повторятс нескольно раз

? - 0 or 1 time
+ - 1 or more times 
* - 0 or more times

\D - all thing except digits
\S - all thing except space
\W - all thing except [a - zA-Z0-9]
. - all thing

.{3,5}

^Dengelois - checking at the beginning
Dengelois$ - cheking at the end 

(^Dengelois){3,5} - it is 1 group that will checking
(^Dengelois|Red){3,5} - it is 1 group that will checking Red or Dengelois

'''

pattern = r'<[^>]*'

re.sub(pattern , '' , text )




import re

pattern = r'[\w\.-]+@[\w\-]+\.[a-zа-я]{2,9}'
wrong_sequence = 'foobar foobaz'
correct_sequence = 'zhalgasbbek@mail.ru'

#r - означает что все символы нужно трактовать напрямую

#print(r'foo\nbar')

re.search(pattern , wrong_sequence)
re.search(pattern , correct_sequence)

def is_valid_email(sequence):
    pattern = r'[\w\.-]+@[\w\-]+\.[a-zа-я]{2,9}'
    return bool(re.search(pattern , sequence))

print(is_valid_email(wrong_sequence))

long_sequence = """
 adal.zhalgasbek2mail.ru
sami123@yahoo.education
zhalgasbbek@mail.ru
sami123@gmail.com
adal@.com
"""

found = re.search(pattern , long_sequence)

dir(found)
print(found.group())


print(re.search(pattern , long_sequence).group())

print(re.findall(pattern , long_sequence))

print(list(re.finditer(pattern , long_sequence)))

found2 = list(re.finditer(pattern , long_sequence))
print([x.group() for x in found2])
