# Printing to console "Hello World" (That is the first thing all programmers do :))
print("Hello World!")

header = "Transport Credit"
print(header)

# %%Data Types
# string => Textual Expression
header2 = "Personal Finance Credit"
print(header2)

# int, integer values
maturity = 36
additional_term = 6

# That is string value be careful about it!
maturity2 = "36"

# float, decimal, double values
# In Python, we generally use snake case for naming convention.
# (like monthly_payment)
monthly_payment = 200.45

# bool, boolean => True or False values
is_valid = True

# %% math Operations

# Summation
print(5 + 6)
print(maturity + 12)
print(maturity + additional_term)

# Substraction
print(5 - 5)
print(maturity - 12)
print(maturity - additional_term)

# Multiplication
print(5 * 5)
interest_rate = 1.08
principal = 10000
time = 3
paid_amount = interest_rate * principal * time
print("Amount to be paid:", paid_amount)

# Division
print(10/5)
print(maturity / 2)
print(maturity / additional_term)

new_maturity = maturity / 2

# Mod(Modulus) Operator
print(10 % 2)

# Logical Operators
print(1 == 1)  # This expression returns True
print(1 == 2)  # This expression returns False

print(1 > 2)  # False
print(3 >= 1)  # True

print(1 != 1)  # False
print(1 != 2)  # True

# or, and keyword
print(1 > 2 or 5 > 2)  # True
print(1 > 2 and 5 > 2)  # False
print(1 > 2 or 5 > 2 and 3 > 2)  # False

# %%Decision Structures

# if else structures

number1 = 10
number2 = 15

# if number1 is bigger than number2, print "number1 is bigger than number2"
# Indentation is significant

if number1 > number2:
    print("number1 is bigger than number2.")

elif number1 == number2:
    print("These are equal.")

else:
    print("number1 is smaller than number2.")

print("It's out of if structure.")
