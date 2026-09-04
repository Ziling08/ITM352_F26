#This program will ask the user to enter a temperature in Fahrenheit, and then it will convert that temperature to Celsius and print it out.
#Name: Ziling He
#Date: September 4, 2026

farenheit_input = input("Enter temperature in Fahrenheit: ")
farenheit_float = float(farenheit_input)

celsius_value = (farenheit_float - 32) * 5 / 9

celsius_value= round(celsius_value, 2)

print("You entered:", farenheit_float)
print("the temperature in Celsius is:", celsius_value)
