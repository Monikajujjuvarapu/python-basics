num = int(input("Enter number: "))
count = 0
temp = num
while temp != 0:
    count += 1
    temp //= 10
print("Number of digits:", count)
