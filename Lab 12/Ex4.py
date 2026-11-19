import pandas as pd
from sodapy import Socrata

client = Socrata("data.cityofchicago.org", None, timeout=30)
records = client.get("rr23-ymwb", limit=500)
client.close()

vehicles = pd.DataFrame(records)
print("First five records:")
print(vehicles.head())
print("\nNumber of records:", len(vehicles))

print("\nVehicles and fuel sources:")
print(vehicles[["public_vehicle_number", "vehicle_type", "vehicle_fuel_source"]].to_string(index=False))

fuel_counts = vehicles.groupby("vehicle_fuel_source", dropna=False).size()
print("\nNumber of vehicles per fuel source:")
print(fuel_counts)
