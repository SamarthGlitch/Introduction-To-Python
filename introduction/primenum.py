from math import sqrt
num = int(input("Enter your number \n"))

if num > 1:
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            print(num, " is not prime")
            break
    else:
        print(num, " is prime")
else:
    print(num, "is not prime")