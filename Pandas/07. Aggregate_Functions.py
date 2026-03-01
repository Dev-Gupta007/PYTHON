import pandas as pd

df = pd.read_csv("Pokemon.csv")

print(df.mean(numeric_only = True))
print(df.sum(numeric_only = True))
print(df.min(numeric_only = True))
print(df.max(numeric_only = True))
print(df.count())   # Does not count Nan

# Single Column

print(df["Height"].mean())
print(df["Height"].sum())
print(df["Height"].min())
print(df["Height"].max())
print(df["Height"].count())
print(df["Type2"].count())

# Group by object

Group = df.groupby("Type1")

print(Group["Height"].mean())
print(Group['Height'].sum())
print(Group['Height'].min())
print(Group['Height'].max())
print(Group["Height"].count())