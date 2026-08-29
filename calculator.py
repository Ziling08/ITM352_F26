# Basic calculator program with repeat capability

whpython3 -

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = num1 / num2
        else:
            print("Error: Invalid operation selected.")
            continue

        print(f"Result: {result}")

    except ValueError:
        print("Error: Please enter valid numbers.")
