thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
#Заметка: Если удаляемый элемент не существует, возникнет ошибка.remove()

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
#Заметка: Если удаляемый элемент не существует, ошибка НЕ возникнет.discard()

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)


thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)