#This program will ask the user to enter a temperature in Fahrenheit, and then it will convert that temperature to Celsius and print it out.
#Create the conversion as a function
# Name: Ziling He
#Date: September 4, 2026

def F_to_C(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    rounded_celsius = round(celsius, 2)
    return rounded_celsius

farenheit_input = input("Enter temperature in Fahrenheit: ")
farenheit_float = float(farenheit_input)

celsius_value = F_to_C(farenheit_float)

celsius_value= round(celsius_value, 2)

print("You entered:", farenheit_float)
print("the temperature in Celsius is:", celsius_value)