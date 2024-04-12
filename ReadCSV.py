import pandas as pd

# Read the CSV files into DataFrames
df1 = pd.read_csv('flipkart.csv')
df2 = pd.read_csv('shopsy.csv')

# Merge the DataFrames on the common column (e.g., 'product_id')
merged_df = pd.merge(df1, df2, on='Name', how='inner')

# Display the common products
print(merged_df)