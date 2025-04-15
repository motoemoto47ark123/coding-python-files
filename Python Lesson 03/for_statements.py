# Examples of for statements in Python

# Simple for loop with range
print("Counting from 0 to 4:")
for i in range(5):
    print(i)

# For loop with specified range (start, stop)
print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(i)

# For loop with specified range (start, stop, step)
print("\nCounting even numbers from 0 to 10:")
for i in range(0, 11, 2):
    print(i)

# For loop with a list
print("\nIterating through a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# For loop with string
print("\nIterating through each character in a string:")
name = "Python"
for char in name:
    print(char)

# Nested for loops
print("\nNested for loops (creating a small multiplication table):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")

# For loop with conditional break
print("\nFor loop with a break statement:")
for i in range(10):
    if i == 5:
        print("Breaking the loop at 5")
        break
    print(i)

# Example from guessing game - loop a fixed number of times (6)
print("\nSimulating the guessing game loop (simplified):")
for guessesTaken in range(6):
    print(f"This is guess number {guessesTaken+1}")
    # If correct answer, we would break here
    if guessesTaken == 3:  # Simulating a correct guess on the 4th attempt
        print("You got it right!")
        break 