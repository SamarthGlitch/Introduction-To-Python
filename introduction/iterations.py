"""
    1. For function1 the algorithm was:
        (4*5)/2
       So the number of iterations will be 1
        
    2. For function2 the algorithm was:
        1 + 2 + 3 + 4
       So the number of iterations will be 4

    3. For function3 the algorithm was:
        1 + (1 + 1) + (1 + 1 + 1) + (1 + 1 + 1 + 1)
       So the number of iterations will be 10

    So for our functions 1, 2 and 3, the number of iterations will depend upon n (4 in our case):
    1. Fun1: O(1)
    2. Fun2: O(n) + O(3)
    3. Fun3: O(n^2) + O(n) + O(6)
        """