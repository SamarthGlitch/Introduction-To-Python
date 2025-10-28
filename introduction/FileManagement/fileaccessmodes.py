usrchoice = int(input("Enter your choice to continue (1: Read, 2: Add/Append, 3: exit): "))
while True:
    if usrchoice not in [1, 2, 3, 4]:
        print("Invalid option please choose a valid option")
        continue

    elif usrchoice == 1:
        file = open('roy.txt', 'r')
        print(file.read())
        file.close()
        break
    
    elif usrchoice == 2:
        u = input("Enter what you want to write.")
        file = open('roy.txt', 'a')
        print(file.write(u))
        file.close()
        break

    elif usrchoice == 2:
        t = input("Enter what you want to append")
        file = open('roy.txt', 'a')
        print("\n", file.write(t))
        file.close()
        break
    
    else:
        break