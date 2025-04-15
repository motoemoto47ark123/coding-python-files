#!/usr/bin/env python3

# IDLE guide
# Interactive shell

print("IDLE GUIDE")
print("-" * 40)

print("""
# What's IDLE?
Python's default IDE
Two ways:
1. Shell window - quick commands
2. Editor window - saved programs

# Start IDLE:
- Windows: Start menu
- Mac: Terminal command
- Linux: Terminal command

# Prompt looks like: >>>
""")

print("\n# EXAMPLES")
print("-" * 40)

print("""
# Basic math:
>>> 2 + 2
4
>>> 2+2+2+2+2
10
>>> 8*5
40
>>> 2        +        3
5

# Order operations:
>>> 5 + 2 * 3 - 4
7

# Variables:
>>> cheese = 12    # Define variable
>>> cheese         # See value
12
>>> cheese + 5     # Use variable
17
>>> cheese * 12    # Multiply
144
>>> 17 - cheese    # Subtract
5
>>> (cheese * 3) + (cheese + 2)  # Complex math
50

# Error:
>>> chicken + cheese
NameError: 'chicken' missing

# Fix error:
>>> chicken = 10   # Define it
>>> chicken + cheese
22

# Change values:
>>> cheese = 5     # New value
>>> cheese
5
>>> chicken + cheese
15

# Multiple variables:
>>> milk = 5
>>> rennet = 8
>>> cheese = milk + rennet
>>> cheese
13
""")

print("\n# SHELL TIPS")
print("-" * 40)

print("""
1. Experiment easily
2. Use arrow keys
3. Variables persist
4. Type help()
5. Type dir()
6. Type quit()

# Editor use:
1. File > New
2. Write code
3. Save .py
4. Press F5
""")

# Running code
print("\n# DEMO CODE")
print("-" * 40)
print("This actually runs!")

# Variables demo
x = 10  # First value
y = 5   # Second value
print(f"x = {x}, y = {y}")
print(f"x + y = {x + y}")  # Addition
print(f"x * y = {x * y}")  # Multiply
print(f"x - y = {x - y}")  # Subtract

print("\nTry IDLE yourself!")
print("Type 'python' to start") 