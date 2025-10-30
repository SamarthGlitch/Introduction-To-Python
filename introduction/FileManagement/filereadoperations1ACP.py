file = open('ACP.txt', 'r')
print(file.read())
file.close()

file = open('ACP.txt', 'r')
print("Read in Parts \n")
print(file.read(8))
file.close()

file = open('ACP.txt', 'a')
file.write(" Hi! I am Penguin and I am a year old.")
file.close()