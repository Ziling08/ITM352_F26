#Read json file of taxi trip data and create a dataframe and some simple stats
import pandas as pd

#Read JSON file into a Pandas dataframe
results_df = pd.read_json("Taxi_Trips.json")

#Display the first few rows of the dataframe
print(results_df.head(6))

#display basic statistics about the dataframe
print(results_df.describe())

median = results_df["fare"].median()
print("The median fare value is ", median)