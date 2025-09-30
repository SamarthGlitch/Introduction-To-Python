def ltd(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result

students = [
    [1, "Jean Castro", "V"],
    [2, "Lula Powell", "V"],
    [3, "Brian Howell", "VI"],
    [4, "Lynne Foster", "VI"],
    [5, "Zachary Simon", "VII"]
]

print("\nOriginal list of Lists")
print(students)

print("\nConverted Lists to a dictionary")
print(ltd(students))