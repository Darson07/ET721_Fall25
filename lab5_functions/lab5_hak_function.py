"""
Darson Hak
Function File
09/15/2025
Lab 5: Functions
"""


# Example #1: Define a function that passes two numbers and return the product of it
def product(a=0, b=0):
    c = a * b
    return c


# Example #2: Function to Calculate the Hypotenuse
def hypotenuse(side1, side2):
    return (side1**2 + side2**2) ** 0.5


# Example #3: Function to check if the number is positive, negative, or zero
# The function returns a string
def check_number(num):
    if num > 0:
        return "POSITIVE"
    elif num < 0:
        return "NEGATIVE"
    else:
        return "ZERO"


# Example #4: Function to calculate the average of a list of grades and return 'true' is the average is greater than 60. Otherwise, it returns 'false'.
def check_grades(grades):
    # Initialize the average grade value
    avg = 0
    # Sum the individual 'g' from list 'grades' into 'avg'
    for g in grades:
        avg += g
    # Find the average grade
    avg /= len(grades)
    return avg


def check_pass(avg_grade):
    # Check if the average is greater than 60
    if avg_grade >= 60:
        return True
    else:
        return False


# ----- EXERCISE: Guess a Number ----- #
import random


def randNum(min, max):
    return random.randint(min, max)


def guessNum(number):
    guess_number = 10
    if guess_number == number:
        return "You got it!"
    elif guess_number > number:
        return "The number is smaller than the guess number"
    else:
        return "The number is bigger than the guess number"
