my_list = [
    [1, 2, 3],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
]

for test in my_list:
    if len(test) < 5:
        print("The list has fewer than 5 elements.")
    elif len(test) <= 10:
        print("The list has between 5 and 10 elements.")
    else:
        print("The list has more than 10 elements.")