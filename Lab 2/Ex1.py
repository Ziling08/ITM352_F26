#This program prompts the user to enter a number between 1 and 10, converts the input to an integer, calculates the square of that number, and then prints both the entered number and its square.
#number, and 


value_entered = input("Enter a number between 1 and 10:")
value_as_integer = int(value_entered)

valuesquared = value_as_integer ** 2

print("you enetered:", value_as_integer)
print(f"The square of the number you entered is: {valuesquared}")

print(f"You entered: {value_as_integer}, and the square of the number you entered is: {valuesquared}")