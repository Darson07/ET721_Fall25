'''
Darson Hak
Function File
October 14th, 2025
Lab #7: 
'''
def testing():
    print("Darson Hak")

# EXAMPLE #1: Read File
def read_data(filename):
    # pipe a text line in a file with a Python code
    with open(filename, "r") as file1:
        filecontent = file1.read()
        print(filecontent)

    # check if the file is closed. If it is closed, it should return True
    print(f"Is the file closed? {file1.closed}")

# EXAMPLE #2: Reading specific portion of a file 
def read_up(filename):
    with open(filename, "r") as file1:
        # read the first 30 characters
        print(file1.read(30))
        # read the next 5 characters
        print(file1.read(5))

# EXAMPLE #3: Readlines
def read_readline(filename):
    with open(filename, "r") as file1:
        # read up to 30 characters of the first line
        print(file1.readline(30))
        # continues reading next line up to 5 characters
        print(file1.readline(5))

# EXAMPLE #4: Readlines
def read_all(filename):
    with open(filename, "r") as file1:
        print(file1.readlines())

# EXAMPLE #5: Loop Through a Readlines File
def read_each(filename):
    with open(filename, "r") as file1:
        filelines = file1.readlines()

        # Loop through each item in 'filelines'
        for eachline in filelines:
            print(eachline.strip())
            # strip() removes the newline character \n

# EXAMPLE #6: Create a New File
def new_file(filename):
    with open(filename, "w") as file:
        file.write("Python Basics for data analysis\n")
        file.write("Darson Hak")

# EXAMPLE #7: Append Data into an Existing File
from datetime import datetime
def stamp_date(filename):
    with open(filename, "a") as file:
        file.write(f"\n\n{datetime.now()}")

# LAB EXERCISE
def email_read(filename, report):
    try:
        count_yahoo = 0
        count_gmail = 0
        count_hotmail = 0

        with open(filename, "r") as file1:
            for eachline in file1:
                email = eachline.lower().strip()

                if "@yahoo.com" in email:
                    count_yahoo += 1

                elif "gmail.com" in email:
                    count_gmail += 1 

                elif "hotmail.com" in email:
                    count_hotmail += 1

        with open(report, "w") as file:
            file.write(f"yahoo = {count_yahoo}\n")
            file.write(f"gmail = {count_gmail}\n")
            file.write(f"hotmail = {count_hotmail}\n")
    
    except FileNotFoundError:
        print("'user_email.txt' was not found")