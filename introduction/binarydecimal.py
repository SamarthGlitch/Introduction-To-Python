binary = input("Enter your Binary: ")
reversedbinary = binary[::-1]
decimal = 0
power = 0
for i in reversedbinary:
    if i == '1':
        decimal = decimal + 2**power
    power += 1
print("Decimal: ",decimal)