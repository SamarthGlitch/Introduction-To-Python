file_read = open('file.txt')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

file_write = open('file.txt', 'w')
file_write.write("File in Write Mode ....")
file_write.write("Hi! I am a Penguin. I am 1 yr. old ")
file_write.close()

file_append = open('file.txt', 'a')
file_append.write("\n File in append mode ....")
file_append.write("Hi! I am a Penguin and I am 1 yr. old")
file_append.close()