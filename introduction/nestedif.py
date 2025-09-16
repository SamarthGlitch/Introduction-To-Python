num = int(input("Enter the number to check: "))

if num>50:
    print("Number is greater than 50 ")
    if num%2==0:
        print("It is even too")
    else:
        print("It is odd too")
elif num==50:
    print("Number is 50")
else:
    print("Number less than 50")