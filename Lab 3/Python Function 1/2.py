
import math
from itertools import permutations

def grams_to_ounces(grams):
    return 28.3495231 * grams

def fahrenheit_to_centigrade(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

def filter_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    return [n for n in numbers if is_prime(n)]

def print_permutations(string):
    return [''.join(p) for p in permutations(string)]

def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

def volume_of_sphere(radius):
    return (4/3) * math.pi * radius ** 3

def unique_elements(lst):
    unique_lst = []
    for element in lst:
        if element not in unique_lst:
            unique_lst.append(element)
    return unique_lst

def is_palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]

# File: my_functions.py
numbers_list = [4, 9, 7]
def histogram(numbers):
    for num in numbers:
        print('*' * num)
histogram(numbers_list)
number_list = [2]
histogram(number_list)
        

if __name__ == "__main__":
    print("100 grams is equal to", grams_to_ounces(100), "ounces")
    print("32 Fahrenheit is equal to", fahrenheit_to_centigrade(32), "Centigrade")
    primes = filter_prime([1, 2, 3, 4, 5, 6, 7, 11, 13, 17])
    print("Prime numbers:", primes)
    print("Permutations of 'abc':", print_permutations("abc"))
    print("Reversed sentence:", reverse_sentence("We are ready"))
    print("Volume of a sphere with radius 3:", volume_of_sphere(3))
    print("Unique elements:", unique_elements([1, 2, 3, 3, 2, 4, 5]))
    print("'madam' is a palindrome:", is_palindrome("madam"))
