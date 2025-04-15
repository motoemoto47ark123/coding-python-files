# This program demonstrates functions in Python

# A simple function that prints a greeting
def say_hello():
    print('Hello!')

# A function that takes an argument
def greet_person(name):
    print('Hello, ' + name + '!')

# A function that returns a value
def create_greeting(name):
    greeting = 'Welcome, ' + name + '!'
    return greeting

# Function calls
say_hello()

print('What is your name?')
user_name = input()
greet_person(user_name)

message = create_greeting(user_name)
print(message)

# Demonstrating the built-in print() and input() functions
print('The print() function displays text on the screen')
print('The input() function collects user input') 