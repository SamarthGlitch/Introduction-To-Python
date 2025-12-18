num = int(input("Enter number: "))

if num == 0:
    print("No set bit present")
else:
    position = 1
    while num & 1 == 0:
        num >>= 1
        position += 1

    print("Position of the first set bit:", position)
