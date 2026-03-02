import pandas as pd

# Data cleaning in Pandas is the process of preparing raw data for analysis
# by detecting and fixing errors, inconsistencies, and 
# missing values using the Pandas library in Python.

# It typically involves:

# Handling missing values (e.g., removing or filling NaN values)

# Removing duplicates

# Correcting data types (e.g., converting strings to dates or numbers)

# Fixing inconsistent formatting (such as extra spaces or inconsistent capitalization)

# Filtering or correcting incorrect data entries

df = pd.read_csv("Pokemon.csv")

# 1 Drop irelevent columns
df2 = df.drop(columns = ["Legendary" , "No"])

print(df2)

# 2.Drop na

df3 = df.dropna(subset = ["Type2"])

print(df3.to_string())

# Handle missing Values

df = df.fillna({'Type2' : "None"})

print(df)

# Fix Inconsistent Values
df["Type1"] = df["Type1"].replace({"Grass" : "GRASS" , 
                                   "Fire" : "FIRE" , 
                                   "Water" : "WATER"})

print(df)

# Standardise Text

df["Name"] = df["Name"].str.lower()

print(df)

# FIX DATA TYPES

df["Legendary"] = df["Legendary"].astype(bool)

print(df.to_string())