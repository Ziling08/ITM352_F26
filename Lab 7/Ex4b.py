def check_budget(purchases, budget):
    for purchase in purchases:
        if purchase > budget:
            print(f"${purchase} is over budget.")
        else:
            print(f"${purchase} is within budget.")


# test 1
check_budget([20, 40, 70], 50)

# test 2
check_budget([10, 15, 25], 30)

# test 3
check_budget([60, 80, 100], 50)