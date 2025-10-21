import math
from abc import ABC, abstractmethod

class Polygon(ABC):
    def area(self):
        pass

class Rectangle(Polygon):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width


class Triangle(Polygon):
    def __init__(self, base, height):
        self.__base = base
        self.__height = height

    def area(self):
        return 0.5 * self.__base * self.__height


class Circle(Polygon):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * (self.__radius ** 2)


class Square(Polygon):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side ** 2


def main():
    print("Polygon Area Calculator")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    print("4. Square")

    choice = input("Choose a shape (1-4) to calculate area: ")

    if choice == '1':
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        shape = Rectangle(l, w)

    elif choice == '2':
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        shape = Triangle(b, h)

    elif choice == '3':
        r = float(input("Enter radius: "))
        shape = Circle(r)

    elif choice == '4':
        s = float(input("Enter side: "))
        shape = Square(s)

    else:
        print("Invalid choice!")
        return

    print(f"\nArea of {shape.__class__.__name__}: {shape.area():.2f}")

if __name__ == "__main__":
    main()
