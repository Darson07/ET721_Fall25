"""
Darson Hak
Lab #7: Accessing Data in a File
October 14th, 2025
"""

from lab7_function import *

testing()
print("\n----- Example #1: Reading a File -----")
read_data("phrases.txt")

print("\n----- Example #2: Reading Specific Portion of a File -----")
read_up("phrases.txt")

print("\n----- Example #3: Reading Specific Portion using readline -----")
read_readline("phrases.txt")

print("\n----- Example #4: Reading Specific Portion using readlines -----")
read_all("phrases.txt")

print("\n----- Example #5: Loop Through Each Line -----")
read_each("phrases.txt")

print("\n----- Example #6: Creating a New File -----")
new_file("hak.txt")

print("\n----- Example #7: Append Data Into a New File -----")
stamp_date("hak.txt")

print("\n----- LAB EXERCISE -----")
email_read("user_email.txt", "reportemail.txt")
