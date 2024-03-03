def counter_of_letters(string):
    counter_of_upper = 0
    counter_of_lower = 0
    for char in string:
        if char.isupper():
            counter_of_upper+=1
            
        elif char.islower():
            counter_of_lower+=1
            
    return counter_of_lower,counter_of_upper

world = input()   
print(counter_of_letters(world)) 



world = input()
number_of_upper = sum ( map ( lambda x : x.isupper() , world))
number_of_lower = sum ( map ( lambda x : x.islower() , world))
print( number_of_lower ,  number_of_upper)