def printPowerSet(arr, set_size):
    power_set_size = 2**set_size

    for outer in range(power_set_size):
        subset = ""
        for inner in range(set_size):
            if outer & (1 << inner):
                subset += str(arr[inner]) + " "
        print("(",subset.strip(),")")

arr = [1, 2, 3]
printPowerSet(arr, len(arr))