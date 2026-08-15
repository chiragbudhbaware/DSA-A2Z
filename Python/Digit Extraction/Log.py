from math import *

num = int(input("Enter a number : "))

def count_digit(num):
    return int (log10(num) + 1)

print(count_digit(num))