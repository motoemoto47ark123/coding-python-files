# Examples of breaking loops in Python

# Example 1: Breaking a simple while loop
print("Example 1: Breaking a while loop when a condition is met")
counter = 0
while counter < 10:
    print(f"Counter: {counter}")
    if counter == 5:
        print("Counter reached 5, breaking the loop")
        break
    counter += 1
print("Loop finished\n")

# Example 2: Breaking a for loop
print("Example 2: Breaking a for loop")
for i in range(10):
    print(f"i = {i}")
    if i == 7:
        print("i reached 7, breaking the loop")
        break
print("For loop finished\n")

# Example 3: Breaking nested loops (only breaks the innermost loop)
print("Example 3: Breaking nested loops")
for x in range(3):
    print(f"Outer loop: x = {x}")
    for y in range(5):
        print(f"  Inner loop: y = {y}")
        if y == 2:
            print("  y reached 2, breaking the inner loop")
            break
    print("  Inner loop finished")
print("Nested loops finished\n")

# Example 4: Breaking when user input meets a condition
print("Example 4: Breaking based on user input (simulated)")
attempts = 0
max_attempts = 3

# Simulating user input for demonstration
simulated_inputs = ["password1", "password2", "correct_password"]

while attempts < max_attempts:
    # In a real program this would be: user_input = input("Enter password: ")
    user_input = simulated_inputs[attempts]
    print(f"User entered: {user_input}")
    
    attempts += 1
    
    if user_input == "correct_password":
        print("Correct password! Access granted.")
        break
    else:
        print(f"Incorrect password. {max_attempts - attempts} attempts remaining.")

if attempts == max_attempts and user_input != "correct_password":
    print("Too many failed attempts. Access denied.")
print("Password check finished\n")

# Example 5: Breaking a loop in a number guessing game (simplified)
print("Example 5: Number guessing game with break")
import random

# Set a fixed number for demonstration
secret_number = 7
print(f"(Secret number is {secret_number} for demonstration)")

# Simulated guesses
simulated_guesses = [3, 10, 7]
max_guesses = 6
guesses_taken = 0

while guesses_taken < max_guesses:
    # In a real program: guess = int(input("Take a guess: "))
    guess = simulated_guesses[guesses_taken]
    print(f"User guessed: {guess}")
    
    guesses_taken += 1
    
    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        print(f"Good job! You guessed the number in {guesses_taken} guesses!")
        break  # Exit the loop when the correct number is guessed

if guess != secret_number:
    print(f"Nope. The number I was thinking of was {secret_number}")
print("Game finished") 