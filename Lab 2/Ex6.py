#This program will ask the user to enter their weight in pounds and display the equivalent weight in kilograms.
#Name: Ziling He
#Date: September 4, 2026

#print("the weight in kilogram is:", float(input("Enter weight in pounds: "))* 0.453592)

KG_TO_POUNDS = 0.453592
weight_in_pounds= input("Enter weight in pounds: ")
Weight_in_pounds_float = float(weight_in_pounds)
weight_in_kilograms = Weight_in_pounds_float * KG_TO_POUNDS

print("you entered:", Weight_in_pounds_float)
print("The weight in kilograms is:", weight_in_kilograms)