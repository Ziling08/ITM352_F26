#open file use "with"

with open("name.txt", "r") as file_object:
    print(type(file_object))

print("file is closed", file_object.closed)

