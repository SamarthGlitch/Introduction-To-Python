#Body mass index
h=float(input("Enter Your height in cm"))
w=float(input("Enter Your weight in kg"))

bmi = w/(h/100)**2

print("Your BMI is ", bmi)

if bmi <= 18.4:
    print("You are underweight")
elif bmi <= 24.9:
    print("You are Healthy")
elif bmi <= 34.9:
    print("You are overweight")
elif bmi <= 39.9:
    print("You are severely overweight")
else:
    print("You are severely obese.")