# Examples of using modules in Python

# What is a module?
# A module is like a code library that contains functions, classes, and variables
# that you can use in your program. Python has many built-in modules.

# Example 1: Using the random module
print("Example 1: Using the random module")
import random

# Generate a random integer between 1 and 10
random_number = random.randint(1, 10)
print(f"Random number between 1 and 10: {random_number}")

# Choose a random element from a list
fruits = ["apple", "banana", "orange", "grape", "kiwi"]
random_fruit = random.choice(fruits)
print(f"Randomly selected fruit: {random_fruit}")

# Shuffle a list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled list: {numbers}")

# Generate a random float between 0 and 1
random_float = random.random()
print(f"Random float between 0 and 1: {random_float}")

# Example 2: Using the math module
print("\nExample 2: Using the math module")
import math

# Constants
print(f"Value of pi: {math.pi}")
print(f"Value of e: {math.e}")

# Functions
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Factorial of 5: {math.factorial(5)}")
print(f"Ceiling of 4.3: {math.ceil(4.3)}")
print(f"Floor of 4.7: {math.floor(4.7)}")

# Trigonometric functions
print(f"Sine of 90 degrees: {math.sin(math.radians(90))}")
print(f"Cosine of 0 degrees: {math.cos(math.radians(0))}")

# Example 3: Using the time module
print("\nExample 3: Using the time module")
import time

# Get current time in seconds since epoch
current_time = time.time()
print(f"Current time in seconds since epoch: {current_time}")

# Sleep for 1 second
print("Waiting for 1 second...")
time.sleep(1)
print("Done waiting!")

# Convert time to a readable format
readable_time = time.ctime(current_time)
print(f"Current time in readable format: {readable_time}")

# Example 4: Using the datetime module
print("\nExample 4: Using the datetime module")
import datetime

# Get current date and time
now = datetime.datetime.now()
print(f"Current date and time: {now}")

# Get individual components
print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")
print(f"Hour: {now.hour}")
print(f"Minute: {now.minute}")
print(f"Second: {now.second}")

# Create a specific date
specific_date = datetime.datetime(2023, 12, 25, 8, 0, 0)
print(f"Christmas 2023: {specific_date}")

# Example 5: Modules in the guessing game
print("\nExample 5: Modules in the guessing game")
import random

# This is how the guessing game uses the random module
secret_number = random.randint(1, 20)
print(f"Secret number generated: {secret_number}")

print("\nHow to import and use modules:")
print("1. Use 'import module_name' to import a whole module")
print("2. Use 'from module_name import function_name' to import specific functions")
print("3. Use 'import module_name as alias' to give the module a shorter name")
print("4. Access functions or variables using dot notation: module_name.function()")

# Example of different import styles
print("\nDifferent ways to import:")
# Method 1: Import the whole module
import random
print(f"Method 1: {random.randint(1, 10)}")

# Method 2: Import specific functions
from math import sqrt, pi
print(f"Method 2: Square root of 16 is {sqrt(16)} and pi is {pi}")

# Method 3: Import with an alias
import datetime as dt
print(f"Method 3: Current day using alias: {dt.datetime.now().day}") 