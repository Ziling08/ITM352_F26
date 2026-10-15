
def is_palindrome(the_string):
    if the_string == the_string[::-1]:
        return True
    else:
        return False

word = input("Enter a word: ")
print(is_palindrome(word))
