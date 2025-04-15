#!/usr/bin/env python3

# Variables basics
# Store values

print("VARIABLES")
print("-" * 40)

# First variable
print("\n# First variable")
cheese = 12  # Value 12
print("cheese =", cheese)  # Show value
print("Type:", type(cheese))  # Show type

# Using variables
print("\n# Variable expressions")
print("cheese + 5 =", cheese + 5)  # Addition
print("cheese * 12 =", cheese * 12)  # Multiplication

# More examples
print("\n# More expressions")
print("17 - cheese =", 17 - cheese)  # Subtraction
print("(cheese * 3) + (cheese + 2) =", (cheese * 3) + (cheese + 2))  # Complex math

# Error example
print("\n# Error example")
print("chicken + cheese")
print("NameError: 'chicken' undefined")

# Another variable
print("\n# Second variable")
chicken = 10  # Value 10
print("chicken =", chicken)
print("chicken + cheese =", chicken + cheese)  # Adding variables

# Change values
print("\n# Change values")
print("cheese =", cheese)
cheese = 5  # New value
print("new cheese =", cheese)
print("chicken + cheese =", chicken + cheese)  # New result

# Multiple variables
print("\n# Multiple variables")
milk = 5  # Milk value
print("milk =", milk)
rennet = 8  # Rennet value
print("rennet =", rennet)
cheese = milk + rennet  # Calculate cheese
print("cheese =", cheese)  # Show result

# Variable rules
"""
Naming Rules:
1. Letters/numbers/_
2. No starting numbers
3. Case sensitive
4. No keywords
5. Be descriptive
""" 