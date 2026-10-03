data = ("hello", 10, "Goodbye", 3, "goodnight", 5)

new_input = input("Enter something to add: ")

try:
    data.append(new_input)

except Exception as error:
    print("I tried to append a value to the tuple.")
    print(error)