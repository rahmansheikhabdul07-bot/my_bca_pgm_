# Program to perform all arithmetic operations on two integers
# Handles division by zero error

# Reading two integers from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("\nResults of Arithmetic Operations")
print("--------------------------------")

# Addition, subtraction and multiplication
print("Addition (a + b)        =", a + b)
print("Subtraction (a - b)     =", a - b)
print("Multiplication (a * b)  =", a * b)

# Division, floor division and modulus (need check for zero)
if b == 0:
    print("Error: Division by zero is not allowed!")
else:
    print("Division (a / b)        =", a / b)
    print("Floor Division (a // b) =", a // b)
    print("Modulus (a % b)         =", a % b)

# Exponentiation
print("Exponent (a ** b)       =", a ** b)
