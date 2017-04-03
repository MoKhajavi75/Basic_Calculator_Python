#Basic Calculator by Morpheus
#2017-03-21
#********************

import functions

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
    print(functions.sum(x, y))

elif c is 2:
    print(functions.sub(x, y))

elif c is 3:
    print(functions.multi(x, y))

elif c is 4:
    print(functions.dev(x, y))

else:
    print("Invalid input!")


print(":)")