recent_perchases = [36.13, 23.87, 183.35, 22.93, 11.62]
budget = 60
total_spend = 0

for purchase in recent_perchases:
    total_spend += purchase
    if total_spend > budget:
        print(f"${purchase} is over budget.")
        break
    else:
        print(f"This purchase ${purchase} is within budget.")