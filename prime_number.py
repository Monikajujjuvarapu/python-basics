num = int(input("Enter number: "))

if num <= 1:
    print("Not a prime number")
else:
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break

    if flag:
        print("Prime number")
    else:
        print("Not a prime number")
