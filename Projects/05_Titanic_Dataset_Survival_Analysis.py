import pandas as pd

df = pd.read_csv(r"D:\DEV\Programming\PYTHON\Projects\~~Titanic.csv")

# Loading And Inspecting Data

print(df)

print(df.shape)
print(df.columns)
print(df.head())            # Getting Index
print(df.info())
print(df.isnull().sum())    # Identifying Nan Values

# Data Cleaning

# Fill age with median

df["Age"] = df["Age"].fillna(df["Age"].median() , inplace = True)

# Droping Cabin (too many missing values)
df.drop("Cabin", axis=1, inplace=True)

# Filling Embarked with most common value
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Changing "Survived" into True or False

df["Survived"] = df["Survived"].astype(bool)
