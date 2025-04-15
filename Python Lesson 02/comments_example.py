# This program demonstrates the use of comments in Python

# Comments start with a # character and continue to the end of the line
# They are ignored by Python when running the program
# Good programmers use comments to explain their code

# This is a single-line comment

"""
This is a multi-line comment or docstring
It can span multiple lines
And is useful for longer explanations
"""

# Comments can explain what a variable is for
user_name = "John"  # Storing the user's name

# Comments can explain complex operations
tax_rate = 0.07  # 7% sales tax
price = 100
tax_amount = price * tax_rate  # Calculate the tax amount
total_price = price + tax_amount  # Add tax to get final price

# Print the results
print("Price:", price)
print("Tax amount:", tax_amount)
print("Total price:", total_price)

# Comments can explain the purpose of functions
def calculate_area(length, width):
    """
    This function calculates the area of a rectangle
    by multiplying its length by its width.
    """
    return length * width

# Using the function
room_length = 10
room_width = 12
room_area = calculate_area(room_length, room_width)
print("Room area:", room_area, "square units")

# Comments should not state the obvious
# BAD: This adds 1 to x
# x = x + 1

# GOOD: Increment counter for each user interaction
# counter = counter + 1 