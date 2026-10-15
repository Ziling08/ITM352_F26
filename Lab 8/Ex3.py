
num1 = 48
num2 = 18

for count in range(min(num1, num2), 0, -1):
    if num1 % count == 0 and num2 % count == 0:
        print("GCD =", count)
        break
