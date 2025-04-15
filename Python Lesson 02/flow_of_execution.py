# This program demonstrates flow of execution in Python
print('Program starts here')

# Variables are defined and created in the order they appear
first_number = 10
print('First number is:', first_number)

second_number = 5
print('Second number is:', second_number)

# Operations happen in the order of execution
sum_result = first_number + second_number
print('The sum is:', sum_result)

# Input pauses execution until the user enters something
print('Enter your name:')
name = input()
print('You entered:', name)

# Function definitions don't execute until called
def multiply(a, b):
    print('Inside the multiply function')
    return a * b

print('Function is defined but not yet called')

# Function calls happen when they are reached
result = multiply(first_number, second_number)
print('The result of multiplication is:', result)

print('Program ends here') 