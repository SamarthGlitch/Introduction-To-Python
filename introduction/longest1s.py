def longestchain(n):
    count = 0
    while n != 0:
        n = n & (n << 1)
        count += 1
    return count

n = int(input("Enter your number: "))
print(f"Longest consecutive 1's length: {longestchain(n)}")