# This program demonstrates variable naming best practices

# Good variable names are descriptive
user_name = 'John'
age = 25
email_address = 'john@example.com'

print('User information:')
print('Name:', user_name)
print('Age:', age)
print('Email:', email_address)

# Poor variable names (don't use these in practice)
a = 'John'
b = 25
c = 'john@example.com'

print('\nSame information with poor variable names:')
print('Name:', a)
print('Age:', b)
print('Email:', c)

# Variable names should make sense for their purpose
first_number = 10
second_number = 20
sum_of_numbers = first_number + second_number

print('\nMath with descriptive variable names:')
print(first_number, '+', second_number, '=', sum_of_numbers)

# Variables store values that can be changed
score = 0
print('\nInitial score:', score)

score = score + 10
print('After earning 10 points:', score)

score = score + 5
print('After earning 5 more points:', score) 