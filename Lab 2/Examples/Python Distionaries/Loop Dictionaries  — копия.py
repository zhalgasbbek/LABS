thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])
  
#Вы также можете использовать метод для Возвращаемые значения словаря:values()
for x in thisdict.values():
  print(x)
  
#Вы можете использовать этот метод для Возвращает ключи словаря:keys()
for x in thisdict.keys():
  print(x)
  
  
#Переберите в цикле как ключи, так и значения с помощью метода:items()
for x, y in thisdict.items():
  print(x, y)
  
  