#!/usr/bin/env python3

# Order operations
# PEMDAS explained

# Operations order:
# 1. Parentheses
# 2. Exponents
# 3. Multiplication/Division
# 4. Addition/Subtraction

print("ORDER OF OPERATIONS")
print("-" * 40)

# Parentheses first
print("\nParentheses first:")
print("(2 + 3) * 4 =", (2 + 3) * 4)  # Result: 20
print("2 + (3 * 4) =", 2 + (3 * 4))  # Result: 14

# Multiply first
print("\nMultiplication first:")
print("2 + 3 * 4 =", 2 + 3 * 4)  # Result: 14
print("Steps:")
print("1. 3 * 4 = 12")
print("2. 2 + 12 = 14")

# Example calculation
print("\nExample calculation:")
result = 5 + 2 * 3 - 4
print("5 + 2 * 3 - 4 =", result)  # Result: 7
print("Steps:")
print("1. 2 * 3 = 6")
print("2. 5 + 6 = 11")
print("3. 11 - 4 = 7")

# Using parentheses
print("\nWith parentheses:")
print("5 + (2 * 3) - 4 =", 5 + (2 * 3) - 4)  # Result: 7
print("(5 + 2) * 3 - 4 =", (5 + 2) * 3 - 4)  # Result: 17
print("5 + 2 * (3 - 4) =", 5 + 2 * (3 - 4))  # Result: 3

# Complex example
print("\nComplex example:")
complex_expression = 10 + 3 * 4 / 2 - 5
print("10 + 3 * 4 / 2 - 5 =", complex_expression)  # Result: 11
print("Steps:")
print("1. 3 * 4 = 12")
print("2. 12 / 2 = 6")
print("3. 10 + 6 = 16")
print("4. 16 - 5 = 11") 