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

#Water Pokemon

Water_Pokemon = df[(df["Type1"] == "Water")|
                   (df["Type2"] == "Water")]

print(Water_Pokemon)

# Fire Flying Pokemon

Fire_Flying_Pokemon = df[(df["Type1"] == "Fire") &
                         (df["Type2"] == "Flying")]

print(Fire_Flying_Pokemon)