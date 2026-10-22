#open a file and read its contents

with open("name.txt", "r") as file_object:
    contents = file_object.read()
    print(contents)
    content_list = contents.split('\n')
    print(f"number of names: {len(content_list)}")
    for name in content_list:
        print(name)



