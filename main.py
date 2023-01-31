# Part 1:
# Assume you want to build two functions for discounting products on a website.
# Function number 1 is for student discount which discounts the current price by 10%.
# Function number 2 is for an additional discount for regular buyers which discounts an additional 5% on the current
# student discounted price.
# Depending on the situation, we want to be able to apply both discounts on the products.
# Design the above two mentioned functions and apply them both simultaneously on the price.

def ten_disc(price):
    return price - (price * .1)


def five_disc(price):
    return price - (price * .05)


print(f"Part 1: {five_disc(ten_disc(100))}")


# Part 2:
# Calculate the value of mathematical expression x*(x+5)^2 where x= 5 using lambda expression.

a = lambda x: x * (x + 5) ** 2
print(f"Part 2: {a(5)}")


# Part 3:
# Consider a list in Python which includes prices of all the items in a store.
# Build a function to discount the price of all the products by 10%.
# Use a map to apply the function to all the elements of the list so that all the product prices are discounted.

newList = [10, 5, 8, 17, 12]
result = list(map(ten_disc, newList))
print(f"Part 3: {result}")

# Part 4:
# Using the concept of object-oriented programming and inheritance, create a superclass named Computer, which has
# two subclasses named Desktop and Laptop.
# Define two methods in the Computer class named getspecs and displayspecs, to get the specifications and display the
# specifications of the computer.
# You can use any specifications that you want.
# The Desktop class and the Laptop class should have one specification which is exclusive to them for example laptop can
# have weight as a special specification.
# Make sure that the subclasses have their own methods to get and display their special specification.
# Create an object of laptop/desktop and make sure to call all the methods from the computer class as well as the
# methods from the own class


class Computer:
    def __init__(self, specs):
        self.specs = specs

    def get_specs(self, specs):
        self.specs = input("Enter specs: ")

    def display_specs(self):
        print(self.specs)


class Laptop(Computer):
    def __init__(self, weight):
        self.weight = weight

    def get_weight(self, weight):
        self.weight = input("Enter weight: ")

    def display_weight(self):
        print(self.weight)


class Desktop(Computer):
    def __init__(self, color):
        self.color = color

    def get_color(self, color):
        self.color = input("Enter color: ")

    def display_color(self):
        print(self.color)


# myTest = Desktop("")
# myTest.get_specs()
# myTest.display_specs()
# myTest.get_color()
# myTest.display_color()

# Using the concept of operator overloading in Python, change the behavior of the multiplication
# operator in a way that multiplication operator behaves like an addition operator.

class Multiply:
    def __init__(self, x):
        self.x = x

    def __mul__(self, other):
        x = self.x + other.x
        return Multiply(x)

    def __str__(self):
        return "{0}".format(self.x)


num1 = Multiply(5)
num2 = Multiply(6)

print(num1 * num2)