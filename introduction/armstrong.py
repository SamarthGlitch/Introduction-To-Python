number = int(input("Enter a number   (example: 1634): "))

def armstrong(num):
    if num in range(1, 10):
        return True
    
    order = len(str(num))
    sum=0
    original = num

    while num > 0:
        digit = num % 10
        sum += digit**order
        num = num // 10
    if sum == original:
        return True
    return False

if armstrong(number):
    print(number, " is an armstrong number")
else:
    print(number, " is not an armstrong number")