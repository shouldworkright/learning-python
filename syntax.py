# A program showcasing basic Python functionality.
# Author: Dan Mello
# Date: 2020-06-02

# Importing packages
import numpy as np

# Function definitions
def factorial(num):

    # Base case
    if num == 1:
        print(num)
        return num

    # Recursive case
    else:
        print(num, '*', end=' ')
        return num * factorial(num-1)

# Basic data types
number = 5                                              # Integer
precise = 5.25                                          # Double
states = ["Massachusetts", "Maine", "Colorado"]         # List
things = [5, "Apple", False, "September", 8.22]         # Also a list (multiple data types)
people = {1:"Matthew", 2:"Mark", 3:"Luke", 4:"John"}    # Dict
decision = True                                         # Boolean
fruit = "Banana"                                        # String
groceries = ("Apple", "Orange", "Banana", "Underwear")  # Tuple
furniture = "Chair", "Couch", "Toilet", "Bed"           # Also a tuple (doesn't need parentheses)
A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}                     # A set
B = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}                # Another set

# Basic loops
for x in states:                # Print each item in the list
    print(x)

for x in states[0]:             # Print each character in item 0 of the list
    print(x)

for x in states:                # Skip one item in the list
    if x == "Maine":
        continue
    print(x)

for x in range(5):              # Print numbers in range [0, 4]
    print(x)

for x in range(4, 8):           # Print numbers in range [4, 7]
    print(x)

for x in range(0, 10, 2):       # Print numbers in range [0, 8] in increments of 2
    print(x)
else:
    print("Loop complete.")     # Print a message once the loops finishes

for x in states:                # Print pairs of items in a list and integers in a range
    for y in range(3):
        print(x, y)

for x in states:                # End the loop immediately
    pass

# User Input
username = input("Enter username: ")        # Prompt the user to enter data
print("Hello " + username + "!")            # Print the data in a sentence

# File Handling
f = open("test.txt", "r+")                  # Open a file for reading and writing
print(f.read())                             # Read the entire file

f.seek(0)                                   # Reset the cursor to the beginning of the file
print(f.readline())                         # Read only 1 line from the file

f.read()                                    # Set cursor to the end of the file
sentence = ["\nI'm writing to the file!\n"] # Create a string
f.writelines(sentence)                      # Write the string as a line to the file
f.seek(0)                                   # Set the cursor to the beginning of the file
print(f.read())                             # Read the file

f.close()                                   # Close the file

# Using methods
print(factorial(5))     # Print the result of factorial(5)
print(np.sqrt(4))       # Print the result of np.sqrt(2)
print(np.abs(-5))       # Print the result of np.absolute(50