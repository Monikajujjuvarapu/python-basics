num = int(input("Enter number: "))
original = num
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

if original == rev:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
