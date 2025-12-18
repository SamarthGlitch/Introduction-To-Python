from math import sqrt

for n in range(10, 100):
    if n > 1:
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                print(n)
                break
        else:
            print(n, " is prime")
    else:
        print(n, "is not prime")