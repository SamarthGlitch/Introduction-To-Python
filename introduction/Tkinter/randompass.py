import random
print("Generating random password...")
n = int(input("How many characters? : "))
chrs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"

list1 = []

for i in range(n):
    list1.append(random.choice(chrs))

list1 = ''.join(list1)
print("Randomly generated password is: ", list1)