print("You need atleast a 75% attendance to be eligible for this exam")
n=int(input("Enter the Total working days of your school (usually 170-200 days): "))
ab=int(input("Enter the total number of days you were absent: "))

pres=n-ab
attendance=(pres/n)*100
if attendance >= 75:
    print("Student is eligible to write exam")
else:
    print("Student is not eligible for this exam")
