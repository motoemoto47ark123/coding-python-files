#!/usr/bin/env python3

# Syntax errors
# Common mistakes

print("SYNTAX ERRORS")
print("-" * 40)

# Correct example
print("\n# Correct syntax")
print("5 + 3 =", 5 + 3)  # Works fine

# Syntax error
print("\n# Error example")
print("5 +")
print("SyntaxError: invalid syntax")

# The fix
print("\n# Fix it")
print("5 + 3 =", 5 + 3)  # Fixed it

# Undefined var
print("\n# Undefined variable")
print("undefined_variable + 5")
print("NameError: not defined")

# The fix
print("\n# Fix it")
defined_variable = 10  # Define it
print("defined_variable + 5 =", defined_variable + 5)  # Now works

# Missing parenthesis
print("\n# Missing parenthesis")
print("(5 + 3")
print("SyntaxError: unclosed parenthesis")

# The fix
print("\n# Fix it")
print("(5 + 3) =", (5 + 3))  # Closed it

# Error tips
print("\n# Avoid errors")
print("1. Complete operators")
print("2. Define variables")
print("3. Match parentheses")
print("4. Check indentation")
print("5. Read errors")

# IDLE errors
print("\n# When errors happen")
print("1. Read message")
print("2. Check line")
print("3. Fix it")
print("4. Try again")

# Error types
"""
Error Types:
1. SyntaxError
2. NameError
3. TypeError
4. ValueError
5. IndexError
6. KeyError
7. AttributeError
8. IndentationError
""" 