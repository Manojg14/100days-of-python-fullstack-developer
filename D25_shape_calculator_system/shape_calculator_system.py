from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def total_angle_type(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def display_type(self):
        print("\nShape: Rectangle")

    def total_angle_type(self):
        return '360 Degree'


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def display_type(self):
        print("\nShape: Circle")

    def total_angle_type(self):
        return '360 Degree'


class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.sides = (side1, side2, side3)

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def calculate_perimeter(self):
        return sum(self.sides)

    def display_type(self):
        print("\nShape: Triangle")

    def total_angle_type(self):
        return '180 Degree'


def main():
    while True:
        print("=== Welcome To Shape Calculator System ===")
        print("\n=== Shape Calculator Options ===")
        print("1. Rectangle\n2. Circle\n3. Triangle\n4. Exit")
        choice = int(input("Choose a shape (1/2/3/4): "))

        if choice == 1:
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            shape = Rectangle(length, width)

        elif choice == 2:
            radius = float(input("Enter radius: "))
            shape = Circle(radius)

        elif choice == 3:
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            side1 = float(input("Enter side 1: "))
            side2 = float(input("Enter side 2: "))
            side3 = float(input("Enter side 3: "))
            shape = Triangle(base, height, side1, side2, side3)

        elif choice == 4:
            print("Exiting program. Thank you!")
            break

        else:
            print("Invalid choice. Try again.")
            continue

        shape.display_type()
        shape.total_angle_type()
        print(f"Area: {shape.calculate_area():.2f}")
        print(f"Perimeter: {shape.calculate_perimeter():.2f}")
        print("-" * 30)

if __name__ == '__main__':
    main()
