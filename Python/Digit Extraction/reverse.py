num = int(input("Enter a number : "))
rev = 0
num1 = num

while num > 0:
    last = num % 10
    rev = rev * 10 + last
    num = num // 10

print(f"Reverse Number is ",rev)

if num1 == rev:
    print("Palindrome")
else:
    print("Not palindrome")
