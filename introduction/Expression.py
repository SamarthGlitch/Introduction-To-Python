# Define a class to handle mathematical expressions
class Solver:
    def __init__(self, expression):
        self.expression = expression

    def solve(self):
        result = eval(self.expression)
        print(f"The result of '{self.expression}' is: {result}")

express = input("Enter a math expression (ex: 5+3*2): ")

solver = Solver(express)

solver.solve()
