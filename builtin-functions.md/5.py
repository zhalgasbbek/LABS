#boolean_list = [True ,False]
#print(all(boolean_list))




boolean_tuple = tuple(map(lambda x: x.lower() == 'true', input().split()))
result = all(boolean_tuple)
print(result)
