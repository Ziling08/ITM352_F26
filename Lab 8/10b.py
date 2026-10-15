
def assign_requirements(student_id, num_reqs):
    if num_reqs < 2:
        return None

    total = 0
    product = 1

    for digit in student_id:
        num = int(digit)
        total += num

        if num != 0:
            product *= num

    first = (total % num_reqs) + 1
    second = (product % num_reqs) + 1

    while first == second:
        if num_reqs == 2:
            second = (second % num_reqs) + 1
        else:
            second += 1
            second = (second % num_reqs) + 1

    return first, second


student_id = input("Enter student ID: ")
num_reqs = int(input("Enter number of requirements: "))

if student_id.isdigit() and num_reqs >= 2:
    result = assign_requirements(student_id, num_reqs)
    print("Assigned requirements:", result)
else:
    print("Invalid input")

