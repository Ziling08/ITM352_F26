
searchMe = [2, 5, 7, 11, 15, 22, 27, 30, 34, 41, 55, 57, 58, 60, 77]
def search_number(number):
    for item in searchMe:
        if item == number:
            return True
    return False

num = int(input("Enter a number: "))
print(search_number(num))

