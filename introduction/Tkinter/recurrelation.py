def myfunction1(n):
    if n>0:
        return
    for i in range(0,n+1):
        print("Codingal")
    myfunction1(n/2)
    myfunction1(n/3)

    #Recurence Relation => T(n) = T(n/2) + T(n/3) + O(n)
    """O(n) grows fastest so, T(n) = O(n)"""

def myfunction2(n):
    if n<=1:
        return
    print("Codingal")
    myfunction2(n-1)
    
    #Recurrence Relatio => T(n) = T(n-1) + O(1)
    """T(n) = 1 + 1 + 1... n times so, T(n) = O(n)"""