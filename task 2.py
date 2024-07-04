import pandas as pd

# Week 1: Load and Explore Data
data_path = "sample_data.cvs"  
df = pd.read_csv("E:\\sample_data.csv")

# Basic exploration
print(df.head())  # Display first 5 rows
print(df.shape)  # Number of rows and columns
print(df.info()) # Data types and missing values summary

# Week 2: Data Cleaning
df_cleaned = df.dropna()  # Drop rows with any missing values
df_cleaned = df_cleaned.drop_duplicates()  # Remove duplicate rows

# Example data type conversion (if needed)
if 'Price' in df_cleaned.columns: 
    df_cleaned['Price'] = pd.to_numeric(df_cleaned['Price'], errors='coerce')  # Convert to numeric, force errors to NaN


# Week 3: Data Manipulation
filtered_df = df_cleaned[df_cleaned['Category'] == 'Electronics']  # Filter by category
sorted_df = df_cleaned.sort_values(by='Date', ascending=False)  # Sort by date

# Group by and calculate statistics
grouped_df = df_cleaned.groupby('Category')['Price'].mean() # Calculate the average price per category

# Creating a new column
df_cleaned['PricePerItem'] = df_cleaned['Price'] / df_cleaned['Quantity']  # Calculate price per item

# (Week 4: Visualization - Example with Matplotlib)
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.hist(df_cleaned['Price'], bins=20, color='skyblue', alpha=0.7)
plt.title('Distribution of Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.5)
plt.show()
