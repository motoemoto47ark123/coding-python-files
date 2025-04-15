# Examples of converting values with int(), float(), and str() functions

# Converting strings to integers
print("Converting strings to integers:")
string_number = "42"
integer_number = int(string_number)
print(f"string_number: {string_number}, type: {type(string_number)}")
print(f"integer_number: {integer_number}, type: {type(integer_number)}")

# Adding an integer to a converted string
print("\nAdding an integer to a converted string:")
result = 3 + int("33")
print(f"3 + int('33') = {result}")

# Converting to float
print("\nConverting to float:")
int_value = 42
float_value = float(int_value)
print(f"int_value: {int_value}, type: {type(int_value)}")
print(f"float_value: {float_value}, type: {type(float_value)}")

# Converting string to float
string_float = "42.5"
float_value2 = float(string_float)
print(f"string_float: {string_float}, type: {type(string_float)}")
print(f"float_value2: {float_value2}, type: {type(float_value2)}")

# Converting to string
print("\nConverting to string:")
int_value2 = 42
string_value = str(int_value2)
print(f"int_value2: {int_value2}, type: {type(int_value2)}")
print(f"string_value: {string_value}, type: {type(string_value)}")

# Converting float to string
float_value3 = 42.2
string_value2 = str(float_value3)
print(f"float_value3: {float_value3}, type: {type(float_value3)}")
print(f"string_value2: {string_value2}, type: {type(string_value2)}")

# Input always returns a string
print("\nInput function example (commented out in code):")
# user_input = input("Enter a number: ")
user_input = "5"  # Simulating user input
print(f"user_input: {user_input}, type: {type(user_input)}")

# Converting user input to an integer
user_input_int = int(user_input)
print(f"user_input_int: {user_input_int}, type: {type(user_input_int)}")

# Why conversion is important - comparing values
print("\nWhy conversion is important:")
string_five = "5"
int_five = 5
print(f"string_five == int_five: {string_five == int_five}")  # False - different types
print(f"int(string_five) == int_five: {int(string_five) == int_five}")  # True - same type

# Example from the guessing game
print("\nExample from the guessing game:")
guess_input = "10"  # Simulating user entering 10
guess = int(guess_input)  # Convert to integer for comparison
print(f"Original input: {guess_input}, type: {type(guess_input)}")
print(f"After conversion: {guess}, type: {type(guess)}")
print("Now we can compare with a number: guess < 15 is", guess < 15) 