# Learning Target 4: Understanding how to use the end="" command

# Normal print statements add a newline at the end
print("This is the first line")
print("This is the second line")

print("\n--- Using end parameter ---")

# Using end="" to continue on the same line
print("Hello ", end="")
print("World!")

# Using end=" " to add a space instead of a newline
print("These", end=" ")
print("words", end=" ")
print("are", end=" ")
print("spaced")

print("\n--- Joke Example ---")

# The interrupting cow joke 
print("Knock knock.")
print("Who's there?")
print("Interrupting cow.")
print("Interrupting cow wh", end="")
print("-MOO!") 