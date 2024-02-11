thislist = ["apple","banana", "cherry"]
thislist.append("watermelon")
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


#Метод не должен добавлять списки, вы можете добавить любой итерируемый объект (кортежи, множества, словари и т.д.).extend()
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)