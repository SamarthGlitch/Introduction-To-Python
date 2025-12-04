numlargest = int(input("Enter the largest number: "))
numsmallest = int(input("Enter the smallest number: "))
while numsmallest:
    numstore = numsmallest
    numsmallest = numlargest % numsmallest
    numlargest = numstore

print("HCF is: ", numlargest)