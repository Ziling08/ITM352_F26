data = ("hello", 10, "Goodbye", 3, "goodnight", 5)

new_value = input("Enter a value: ")

data = list(data)

data.append(new_value)

data = tuple(data)

print(data)