# Examples of different data types: integer, float, string, and boolean

# Integer data type
print("Integer examples:")
age = 25
count = -10
zero = 0
print(f"age: {age}, type: {type(age)}")
print(f"count: {count}, type: {type(count)}")
print(f"zero: {zero}, type: {type(zero)}")

# Float data type
print("\nFloat examples:")
price = 19.99
temperature = -2.5
pi_approx = 3.14159
print(f"price: {price}, type: {type(price)}")
print(f"temperature: {temperature}, type: {type(temperature)}")
print(f"pi_approx: {pi_approx}, type: {type(pi_approx)}")

# String data type
print("\nString examples:")
name = "John"
message = "Hello, World!"
empty_string = ""
number_as_string = "42"
print(f"name: {name}, type: {type(name)}")
print(f"message: {message}, type: {type(message)}")
print(f"empty_string: '{empty_string}', type: {type(empty_string)}")
print(f"number_as_string: {number_as_string}, type: {type(number_as_string)}")

# Boolean data type
print("\nBoolean examples:")
is_true = True
is_false = False
print(f"is_true: {is_true}, type: {type(is_true)}")
print(f"is_false: {is_false}, type: {type(is_false)}")

# Boolean values from comparisons
print("\nBoolean values from comparisons:")
is_greater = 10 > 5
is_equal = 7 == 7
is_not_equal = 5 != 5
print(f"is_greater (10 > 5): {is_greater}")
print(f"is_equal (7 == 7): {is_equal}")
print(f"is_not_equal (5 != 5): {is_not_equal}")

# Data type usage in guessing game
print("\nData types in the guessing game:")
number = 15  # Integer - the secret number
guess = 10   # Integer - user's guess
player_name = "Alex"  # String - player's name
attempts_left = 6 > 2  # Boolean - whether there are attempts left

print(f"number (secret): {number}, type: {type(number)}")
print(f"guess: {guess}, type: {type(guess)}")
print(f"player_name: {player_name}, type: {type(player_name)}")
print(f"attempts_left: {attempts_left}, type: {type(attempts_left)}")

# Type checking and comparison
print("\nComparing different data types:")
print(f"Is guess < number? {guess < number}")
print(f"Converting number to string: {str(number)}, type: {type(str(number))}")
print(f"Concatenating strings: {player_name} guessed {str(guess)}")

# Boolean type from the guessing game logic
print("\nBoolean logic examples from the guessing game:")
too_low = guess < number
too_high = guess > number
correct = guess == number
print(f"too_low (guess < number): {too_low}")
print(f"too_high (guess > number): {too_high}")
print(f"correct (guess == number): {correct}") 