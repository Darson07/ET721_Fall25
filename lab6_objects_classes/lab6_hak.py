"""
Darson Hak
Lab #6: Objects & Classes
09/17/2025
"""

print("----- Example #1: Create a Class -----")


class Circle(object):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    # Method
    def add_radius(self, r):
        self.radius += r
        return self.radius


class Rectangle(object):
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

    # Method to calculate the area
    def area(self):
        return self.width * self.height

    # Method to calculate the perimeter
    def perimeter(self):
        return 2 * self.width + 2 * self.height


# Creating an instance of the class, which is an object
circle1 = Circle(4, "red")
circle2 = Circle(10, "green")

rectangle1 = Rectangle(5, 2, "magenta")
rectangle2 = Rectangle(7, 3, "blue")

# Accessing information in an object
print(f"The color of circle2 = {circle2.color}")
print(f"The width of rectangle1 = {rectangle1.width}")

# Updating data in an object
# Change circle1 color from "red" to "yellow"
print(f"The color of circle1 before the update = {circle1.color}")
circle1.color = "yellow"
print(f"The color of circle1 after the update = {circle1.color}")

# Accessing a method
print(f"Radius of circle2 = {circle2.radius}")
# Update the radius by adding 5
circle2.add_radius(5)
print(f"Radius of circle2 after method add_radius = {circle2.radius}")

# Accessing methods in rectange
print(
    f"The area of the rectangle1 with width {rectangle1.width} and height {rectangle1.height} is {rectangle1.area()}"
)
print(f"The perimeter of rectangle2 = {rectangle2.perimeter()}")

print("\n----- EXERCISE -----")


class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Withdrawal cannot be made; insufficient balance"


# Creating an instance of the BankAcount class
useraccount = BankAccount(123456789, "Darson")

# Demonstrating deposits and withdrawals
useraccount.withdraw(700)
useraccount.deposit(1000)
useraccount.withdraw(500)

# Prompt result
print(f"Final balance: {useraccount.balance}")
