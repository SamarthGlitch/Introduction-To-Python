numlargest = int(input("Enter the largest number: "))
numsmallest = int(input("Enter the smallest number: "))
product = numlargest * numsmallest
while numsmallest:
    numstore = numsmallest
    numsmallest = numlargest % numsmallest
    numlargest = numstore
lcm = product/numlargest
print(f"LCM is: {lcm}")