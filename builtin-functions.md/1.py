from functools import reduce 

def multiplication_of_numbers_list(numbers):
    multiplication =  reduce(lambda x ,y : x * y , numbers )
    return multiplication

numbers = list(map(int , input().split()))
print(multiplication_of_numbers_list(numbers))


#Примените функцию из двух аргументов кумулятивно к элементам последовательности или итерабельности слева направо, чтобы свести итерабельность к одному