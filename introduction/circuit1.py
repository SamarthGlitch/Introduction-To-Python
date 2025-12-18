A = int(input("Enter A (0 or 1): "))
B = int(input("Enter A (0 or 1): "))
C = int(input("Enter A (0 or 1): "))

Q = B and (A or C)

print("Q = ", int(Q))

#A&B
                        #(A&B) + (B&C) = B(A+C) = Q
#B+C
        #(B+C)(B&C) = B&C
#B&C