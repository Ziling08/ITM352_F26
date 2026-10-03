data = ("hello", 10, "Goodbye", 3, "goodnight", 5)

new_value = input("Enter a value: ")

try:
    data.append(new_value)

except:
    data = data + (new_value,)

print(data)