num = int(input("Enter a number : "))
num1 = num

nod = len(str(num))
total = 0

while num > 0:
    last = num % 10
    last = last ** nod
    total += last
    num = num // 10

if total == num1:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")