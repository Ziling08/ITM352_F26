# Open names.txt and read its contents
# Append a new name at the end of the file

with open("names.txt", "a") as file_object:
    file_object.write("Ziling He\n")


with open("names.txt", "r") as file_object:
    contents = file_object.read()
    print(contents)