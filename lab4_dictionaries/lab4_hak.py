"""
Darson Hak
Lab #4: Dictionary and Functions
09/09/2025
"""

print("----- Example #1: Dictionary -----")
# Contact dictionary with three different users
contacts = {"Bill": "718-111-2222", "Martha": "646-000-3333", "Peter": "212-000-1111"}
print(contacts)

# Save the value of a specific key
user1 = contacts["Martha"]
print(f"User's phone number = {user1}")

# Add content to the dictionary
contacts["Anna"] = "646-222-3333"
print(contacts)

# Update value of a specific key
contacts["Peter"] = "800-000-0000"
print(contacts)

print("\n----- Example #2: Loop Through a Dictionary -----")
# Print each key in the dictionary
for i in contacts:
    print(i)

# Print each value in the dictionary
for i in contacts:
    print(contacts[i])

# Print each key:value set in the dictionary
for i in contacts:
    print(f"{i} = {contacts[i]}")

print("\n----- Example #3: Length of a Dictionary -----")
print(f"Dictionary has {len(contacts)} users")

print("\n----- Example #4: Copy a Dictionary -----")
copy_contacts1 = contacts.copy()  # Function
copy_contacts2 = dict(contacts)  # Method
print(copy_contacts1)
print(copy_contacts2)

print("\n----- Example #5: Remove a key:value Pair in a Dictionary -----")
print(contacts)
contacts.pop("Peter")
print(contacts)

print("\n----- Example #6: Add a New key:value Pair in a Dictionary -----")
print(contacts)
contacts.update({"Lucas": "212-111-1111"})
print(contacts)

print("\n----- Example #7: Return Item, Keys, & Values in a Dictionary -----")
print(f"Return items = {contacts.items()}")
print(f"Return keys = {contacts.keys()}")
print(f"Return values = {contacts.values()}")

print("\n----- Example #8: Dictionary Application -----")
# Store in a dictionary the count of occurency of the word in a phrase
phrase = "To be or not to be"
list_phrase = phrase.split()
# Create an empty dictionary
word_count_dict = {}
for word in list_phrase:
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1

# Print result
for word in word_count_dict:
    print(f'"{word}" appears {word_count_dict[word]} time(s)')

print("\n----- EXERCISE -----")
users = [
    "peterpan@yahoo.com",
    "annie@hotmail.com",
    "Carl@hotmail.com",
    "martha@gmail.com",
    "cassie@yahoo.com",
    "Josue@hotmail.com",
    "John@hotmail.com",
]

users_dict = {"gmail": 0, "yahoo": 0, "hotmail": 0}

for email in users:
    if "gmail" in email:
        users_dict["gmail"] += 1
    elif "yahoo" in email:
        users_dict["yahoo"] += 1
    elif "hotmail" in email:
        users_dict["hotmail"] += 1

print(users_dict)
