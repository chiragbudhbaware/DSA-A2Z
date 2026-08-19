s = "azyxyyzaaaa"
q = ["d", "a", "y", "x"]

# Brute Force

for char in q:
    count = 0
    for i in s:
        if char == i:
            count += 1
    print(count)
    
# Optimal Solution

hash_list = [0] * 26

for ch in s:
    ascii_value = ord(ch)
    index = ascii_value - 97
    hash_list[index] += 1

for ch in q:
    ascii_value = ord(ch)
    index = ascii_value - 97
    print(hash_list[index])
