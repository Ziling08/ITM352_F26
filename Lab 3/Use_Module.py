import HandyMath
from HandyMath import max, min

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(f"The midpoint of {num1} and {num2} is {HandyMath.midpoint(num1, num2)}.")

print(f"The square root of the square of {num1} is {HandyMath.squareroot(num1 ** 2)}.")

print(f"{num1} raised to the power of {num2} is {HandyMath.exponent(num1, num2)}.")

print(f"The maximum of {num1} and {num2} is {max(num1, num2)}.")

print(f"The minimum of {num1} and {num2} is {min(num1, num2)}.")