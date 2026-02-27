import pandas as pd

df = pd.read_csv('Pokemon.csv' , index_col = "Name")

print(df)
print(df.to_string())

