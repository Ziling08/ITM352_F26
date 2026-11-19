import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202603" 

tables = pd.read_html(url, flavor="lxml")
rates = tables[0]
print("Columns:")
print(rates.columns)

print("\nDate and 1-month interest rate:")
for index, row in rates.iterrows():
    print(row["Date"], row["1 Mo"])
