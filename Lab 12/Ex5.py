import requests
import pandas as pd

url = ( "https://data.cityofchicago.org/resource/97wa-y6ff.json?$select=driver_type,count(license)&$group=driver_type"
)

response = requests.get(url, timeout=30)
response.raise_for_status()
records = response.json()
print(response)
print(records)

drivers = pd.DataFrame(records)
drivers = drivers.rename(columns={"count_license": "count"})
drivers = drivers[["count", "driver_type"]]
drivers["count"] = drivers["count"].astype(int)
drivers = drivers.set_index("driver_type")
print("\nLicenses by driver type:")
print(drivers)