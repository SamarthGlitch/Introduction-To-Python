with open('file5.txt', 'w') as file:
    file.write("Hi! I am Penguin and I am 1 yr old.")
file.close()

with open('file5.txt', 'r') as file:
    data = file.readlines()
    print("Words in the file are....")
    for line in data:
        word = line.split()
        print(word)
file.close()