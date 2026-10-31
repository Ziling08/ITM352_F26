import pandas as pd
import ssl

csv_file = 'https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K'

ssl._create_default_https_context = ssl._create_unverified_context


try:
    df = pd.read_csv(  
        csv_file,
        engine='pyarrow',
         dtype_backend='pyarrow',
        on_bad_lines='skip')
    print(df.head())
    print(df.dtypes)
    df['order_date'] = pd.to_datetime(
        df['order_date'], errors='coerce', format='%Y-%m-%d')

except Exception as e:
    print("Error reading the CSV file:", e)
