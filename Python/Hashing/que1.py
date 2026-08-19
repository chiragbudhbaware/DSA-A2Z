n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

# Brute Force

for num in m:
    count = 0
    for x in n:
        if x == num:
            count += 1
    print(count)


# Optimal Solution

hash_list = [0] * 11

for num in n:
    hash_list[num] += 1

print(hash_list)

for num in m:
    if num < 1 or num > 10:
        print("0")
    else:
        print(hash_list[num])