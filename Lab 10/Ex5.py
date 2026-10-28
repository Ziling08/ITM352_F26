#import homes data and creat a dataframe
import pandas as pd

homes_data_file = "https://drive.google.com/uc?export=download&id=1M-X_bypJJ6K5p6eM6aYBwt1qIizIiIex"
homes_df = pd.read_csv(homes_data_file)
print(homes_df.head())

#print the dimensions of the dataframe
shape = homes_df.shape
print("The dimensions of the dataframe are: ", shape)

df_big = homes_df[homes_df['units']>= 500]
df_big = df_big.drop(columns=['units'])
print(df_big.head(10))

#Look at the data type
print(df_big.info())

#create land_sqft, gross_sqft, and sale_price to numeric
df_big['land_sqft'] = pd.to_numeric(df_big['land_sqft'], errors='coerce')
df_big['gross_sqft'] = pd.to_numeric(df_big['gross_sqft'], errors='coerce')
df_big['sale_price'] = pd.to_numeric(df_big['sale_price'], errors='coerce')

#Look at the data types and print the clean data
print("After cleaning...")
print(df_big.info())
print(df_big.head(10))

#we have some null values, drop them
df_big = df_big.dropna()

#Now drop duplicates records
df_big = df_big.drop_duplicates()
print("After dropping duplicates...")
print(df_big.info())
print(df_big.head(10))

#filter out zero sales
df_big = df_big[df_big['sale_price'] > 0]
print("After filtering out zero sales...")
print(df_big.info())
print(df_big.head(10))
