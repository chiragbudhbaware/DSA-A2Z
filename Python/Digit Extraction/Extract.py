num = int(input("Enter a Number : "))
count = 0

while num > 0:
    last_digit = num % 10
    count += 1
    num = num // 10

print(count)