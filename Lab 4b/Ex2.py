#Properly format an inputted name in title case.

raw_name = input("Enter your name: ")

stripped_name = raw_name.strip()
print("stripped name:", stripped_name)


title_case_name = stripped_name.title()
print("formatted name in title case:", title_case_name)
