# HandyMath.py

def midpoint(num1, num2):
    return (num1 + num2) / 2


def squareroot(num):
    return num ** 0.5


def exponent(base, exponent):
    return base ** exponent


def max(num1, num2):
    return num1 if num1 > num2 else num2


def min(num1, num2):
    return num1 if num1 < num2 else num2

def use_function(x, y, function):
    return f"The function {function.__name__} {x},{y} = {function(x, y)}"


print(use_function(4, 2, min))
print(use_function(4, 2, max))
print(use_function(4, 2, exponent))