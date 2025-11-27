a = int(input("Enter 'a' for a*b (a<b)"))
b = int(input("Enter 'b' for a*b (b>a)"))

def one(a,b):
    result = 0
    for i in range(1):
        result = a*b
    return result

print("1 iteration: ", one(a,b))

def N(a,b):
    result = 0
    if b<a:
        for i in range(a):
            result += b
    else:
        for i in range(b):
            result += a
    return result

print("N iteration: ", N(a,b))