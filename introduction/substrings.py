s = input("Enter string: ")
n = len(s)

for i in range(n):
    for j in range(i + 1):
        print(s[j:i+1])