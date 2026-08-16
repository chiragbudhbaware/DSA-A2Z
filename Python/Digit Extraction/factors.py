# Brute Force
# result = []

# num = int(input("Enter a number : "))

# for i in range(1, num+1):
#     if num % i == 0:
#         # print(i)
#         result.append(i)
        
# print(result)

# Better Approach

# num = int(input("Enter a number : "))

# result = []

# for i in range(1, num // 2 + 1):
#     if num % i == 0:
#         result.append(i)

# result.append(num)
# print(result)


# Optimal Approach 
from math import *

num = int(input("Enter a number : "))
result = []

for i in range(1, int(sqrt(num)) + 1):
    if num % i == 0:
        result.append(i)
        if num // i != i:
            result.append(num // i)

result.sort()
print(result)