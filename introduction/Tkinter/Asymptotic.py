def myfunction(n):
    for i in range(0, n+1):
        print("First Loop")
        #"Time Complexity: O(n)"

    j=1
    while(j<=n+1):
        print("Second Loop ", j)
        j*=2
        #Time Complexity: O(log n)

    for i in range(0, 100):
        print("Third Loop")
        #Time Complexity: O(1)

"""
        Total Time Complexity = O(n) [As O(log n) and O(1) grow slower than O(n)]
                                                                                        """