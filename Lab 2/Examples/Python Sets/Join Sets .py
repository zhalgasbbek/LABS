set = {"apple", "banana", "cherry"}
set2 = {1 , 2 , 3}
set3 =set.union(set2)
print(set3)

set = {"apple", "banana", "cherry"}
set2 = {1 , 2 , 3}
set.update(set2)
print(set)

#Сохраняйте элементы, которые существуют как в set , так и в set :xy
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

#Сохраните предметы, которых нет в обоих наборах:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)


x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}
z = x.symmetric_difference(y)
print(z)


