'''
Darson Hak
Lab #5: Functions
09/15/2025
'''

'''
- Pre-defined functions: Python library
- User-defined functions: Created by the programmer

What is a function? 
- Block of code that begins with 'def' followed by the name of the function and parantheses()
- The body of the function is indented ater the :
- The body of the function only runs when the function is called
- To call a function, we need to write the function's name and parantheses
'''

print("----- Example #1: Intro Function -----")
# Import Python files
from lab5_hak_function import *

# Call function product()
n1 = 2
n2 = 5
p = product(n1,n2)
print(f"The product of {n1} and {n2} is {p}")
p = product()
print(f"The product is {p}")
p = product(5)
print(f"The product is {p}")

print("\n----- Example #2: Function to Calculate the Hypotenuse -----")
s1 = 5
s2 = 3
hyp = hypotenuse(s1,s2)
print(f"The hypotenuse is {hyp:0.2f}")

print("\n----- Example #3: Check if the number is positive, negative, or zero -----")
c = check_number(-3)
print(f"The number is {c}")
c = check_number(5)
print(f"The number is {c}")
c = check_number(0)
print(f"The number is {c}")

print("\n----- Example #4: Function in a List -----")
grades = [50, 60, 85, 93, 72, 98]
avg = check_grades(grades)
print(f"Did I pass the class? {check_pass(avg)}")
grades = [50, 60, 30, 50]
print(f"Did I pass the class? {check_pass(check_grades(grades))}")

print("\n----- EXERCISE: Guess a Number -----")
random_num = randNum(1,50)
result = guessNum(random_num)
print(f"The random number is {random_num}")
print(result)