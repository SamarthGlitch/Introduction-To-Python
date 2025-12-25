n = int(input("Enter a number: "))
rev = 0

while n > 0:
    rev = (rev << 1) | (n & 1)
    n = n >> 1

print(rev)