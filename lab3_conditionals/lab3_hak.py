"""
Darson Hak
Lab 3: Python Conditional Statements and Loops
09/08/2025
"""

# Conditional Statements
print("\n ----- Example #1: if, elif,..., else -----")
# Guess a number between 1 and 9
GUESS_NUM = 8
# Collect the number
user_num = int(input("Guess a number: "))
# Compare
if user_num == GUESS_NUM:
    print(f"Great job! {user_num} is the guess number")
elif user_num > GUESS_NUM:
    print(f"{user_num} should be lower")
elif user_num < GUESS_NUM:
    print(f"{user_num} should be higher")
else:
    print(f"ERROR!")

print("End of guessing!")


print("\n ----- Example #2: Control Flow with Logical Operators -----")
# 'and', 'or', 'not' operators
# 'and' operator returns TRUE ONLY if all statements are true
# 'or' operator returns TRUE if at least ONE of the statements are true
# 'not' operator returns the inverse of the statements. Ex. True ---> not operator ---> false
"""
Example #2: 
- Children from 5 to 9 are only given milk for breakfast
- Children from 10 to 14 are given sandwiches
- Children from 15 to 17 are given a burger
"""
age_student = int(input("Enter an age: "))
lunch = "None"
if age_student <= 9 and age_student >= 5:
    lunch = "milk"
elif age_student >= 10 and age_student <= 14:
    lunch = "sandwich"
elif age_student >= 15 and age_student <= 17:
    lunch = "burger"
else:
    lunch = "None"

print(f"At age {age_student} the food is {lunch}")


print("\n ----- Example #3: For Loops as a Counter -----")
# 'for' loops enables the program to eexecutre a code block multiple times
for n in range(2, 10):
    print(n)


print("\n ----- Example #4: For Loops in a List -----")
years = [2011, 2005, 1998, 1980, 1973]
for y in years:
    print(y)

for index in range(len(years)):
    print(f"Year {index+1} = {years[index]}")


print("\n ----- Example #5: While Loop as a Counter -----")
count = 1
while count <= 5:
    print(count)
    count += 1


print("\n ----- Example #6: While Loop to Validate a Number -----")
# Validate If a Number is Between -5 and 5 (Inclusive)
num = int(input("Enter a number between -5 and 5: "))
# Use a while loop to recollect if the num is not between -5 and 5
while num < -5 or num > 5:
    num = int(input("ERROR! Enter a number between -5 and 5: "))

print(f"Entered number = {num}")


print("\n ----- Modify Example #1 -----")
"""
Modify Example #1:
- Use while loop to validate if the user number is between 1 and 9
- User can only guess three times. This can be done using a for loop or a while loop
"""
GUESS_NUM = 8
attempts_left = 3
count = 1

user_num = int(input("Guess a number between 1 and 9. You have 3 tries: "))
while count != 3:
    if user_num < 1 or user_num > 9:
        attempts_left -= 1
        count += 1
        int(
            input(f"That's not within the range. You have {attempts_left} tries left: ")
        )
    elif user_num == GUESS_NUM:
        print(f"Nice! You guessed it right. Attempts: {count}")
    elif user_num < GUESS_NUM:
        attempts_left -= 1
        count += 1
        int(
            input(
                f"Your number should be higher. You have {attempts_left} tries left: "
            )
        )
    elif user_num > GUESS_NUM:
        attempts_left -= 1
        count += 1
        int(
            input(f"Your number should be lower. You have {attempts_left} tries left: ")
        )
    else:
        print(f"ERROR! ERROR!")
