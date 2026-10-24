
# Calculate total fare, average fare, and max trip distance
# for fares greater than $10

import csv

filename = "taxi_1000.csv"

total_fare = 0.0
max_distance = 0.0
average_fare = 0.0
count = 0

with open(filename, "r") as file:
    csv_reader = csv.reader(file)

    headers = next(csv_reader)
    fare_index = headers.index("Fare")
    distance_index = headers.index("Trip Miles")

    for row in csv_reader:
        if not row:
            continue

        try:
            fare = float(row[fare_index])
            distance = float(row[distance_index])
        except (ValueError, IndexError):
            continue

        if fare > 10:
            total_fare += fare
            count += 1

            if distance > max_distance:
                max_distance = distance

if count > 0:
    average_fare = total_fare / count

print(f"Total Fare: ${total_fare:.2f}")
print(f"Average Fare: ${average_fare:.2f}")
print(f"Max Trip Distance: {max_distance:.2f} miles")

