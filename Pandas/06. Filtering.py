import pandas as pd

df = pd.read_csv('Pokemon.csv' , index_col = "Name")

# Filtering ---> Keeping the rows that match a condition

tall_pokemon = df[df["Height"] >= 2]
heavy_pokemon = df[df["Weight"] > 100]
legendary_pokemon = df[df["Legendary"] == 1]
# legendary_pokemon = df[df["Legendary"] == True]   # Same


print(tall_pokemon)
print(heavy_pokemon)
print(legendary_pokemon)