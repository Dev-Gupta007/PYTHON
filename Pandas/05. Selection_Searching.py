import pandas as pd

df = pd.read_csv('Pokemon.csv' , index_col = "Name")

# SELECTION BY COLUMN

print(df["Name"].to_string())
print(df["Height"].to_string())
print(df["Weight"].to_string())
print(df[["Name","Height","Weight"]].to_string())

# SELECTION BY ROW

print(df.loc["Moltres"])
print(df.loc["Pikachu"])
print(df.loc["Charizard" : "Blastoise" , ["Height" , "Weight"]])
print(df.iloc[0:11:2 , 0:3])

# Searching By User Input

pokemon = input("Enter the Name of Pokemon: ")

try:
    print("Details Are : \n" , df.loc[pokemon])
except KeyError:
     print("Pokemon Not found: ")