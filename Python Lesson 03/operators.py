# Examples of mathematical operators in programming

# Addition operator (+)
print("Addition operator (+):")
a = 5
b = 3
print(f"{a} + {b} = {a + b}")

# String concatenation with + operator
name = "John"
greeting = "Hello, " + name
print(f"String concatenation: {greeting}")

# Subtraction operator (-)
print("\nSubtraction operator (-):")
c = 10
d = 4
print(f"{c} - {d} = {c - d}")

# Multiplication operator (*)
print("\nMultiplication operator (*):")
e = 6
f = 7
print(f"{e} * {f} = {e * f}")

# Division operator (/)
print("\nDivision operator (/):")
g = 20
h = 5
print(f"{g} / {h} = {g / h}")  # Returns a float

# Integer division operator (//)
print("\nInteger division operator (//):")
i = 7
j = 2
print(f"{i} // {j} = {i // j}")  # Returns an integer

# Modulo operator (%)
print("\nModulo operator (%):")
k = 17
l = 5
print(f"{k} % {l} = {k % l}")  # Returns the remainder

# Exponentiation operator (**)
print("\nExponentiation operator (**):")
m = 2
n = 3
print(f"{m} ** {n} = {m ** n}")  # 2 to the power of 3

# Compound assignment operators
print("\nCompound assignment operators:")
x = 10

# Addition assignment
print(f"Initial x: {x}")
x += 5  # Same as x = x + 5
print(f"After x += 5: {x}")

# Subtraction assignment
x -= 3  # Same as x = x - 3
print(f"After x -= 3: {x}")

# Multiplication assignment
x *= 2  # Same as x = x * 2
print(f"After x *= 2: {x}")

# Division assignment
x /= 4  # Same as x = x / 4
print(f"After x /= 4: {x}")

# Comparison operators
print("\nComparison operators:")
p = 10
q = 20

print(f"{p} < {q}: {p < q}")   # Less than
print(f"{p} > {q}: {p > q}")   # Greater than
print(f"{p} <= {q}: {p <= q}")  # Less than or equal to
print(f"{p} >= {q}: {p >= q}")  # Greater than or equal to
print(f"{p} == {q}: {p == q}")  # Equal to
print(f"{p} != {q}: {p != q}")  # Not equal to

# Example from the guessing game
print("\nOperators used in the guessing game:")
guessesTaken = 3
guessesTaken = guessesTaken + 1  # Incrementing the guess counter
print(f"Guesses taken after increment: {guessesTaken}")

number = 15
guess = 10
print(f"guess < number: {guess < number}")  # Checking if guess is too low
print(f"guess > number: {guess > number}")  # Checking if guess is too high
print(f"guess == number: {guess == number}")  # Checking if guess is correct
print(f"guess != number: {guess != number}")  # Checking if guess is incorrect 