# Basic Calculator by MohamadKh75
# 2017-03-21
# ********************

import cmd_functions


print("The Basic Calculator")
print("**********\n")

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print("____")

print("Choose your operation:")
print("*******")
print("1. Summation")
print("2. Subtraction")
print("3. Multiply")
print("4. Division")
print()

c = int(input("Choose: "))

if c is 1:
    print(cmd_functions.sum_numbers(x, y))

elif c is 2:
    print(cmd_functions.sub_numbers(x, y))

elif c is 3:
    print(cmd_functions.multi_numbers(x, y))

elif c is 4:
    print(cmd_functions.dev_numbers(x, y))

else:
    print("Invalid input!")


print(":)")
