# | Distribution | Meaning                          |
# | ------------ | -------------------------------- |
# | 50% / 50%    | Perfectly balanced               |
# | 60% / 40%    | Slightly imbalanced (still fine) |
# | 70% / 30%    | Moderately imbalanced            |
# | 80% / 20%    | Strongly imbalanced              |
# | 90% / 10%    | Severely imbalanced              |

print("="*50)
print("TITANIC SURVIVAL ANALYSIS")
print("="*50)

import pandas as pd

df = pd.read_csv(r"D:\DEV\Programming\PYTHON\Projects\~~Titanic.csv")

# Loading And Inspecting Data

# print(df.shape)
# print(df.columns)
# print(df.head())            # Getting Index
# print(df.info())
# print(df.isnull().sum())    # Identifying Nan Values

# Data Cleaning

# Fill age with median

df["Age"] = df["Age"].fillna(df["Age"].median())

# Droping Cabin (too many missing values)
df.drop("Cabin", axis=1, inplace=True)

# Filling Embarked with most common value
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Changing "Survived" into True or False

df["Survived"] = df["Survived"].astype(bool)

# What Percentage Suvived?

Survived = df[df["Survived"] == True] 

Percentage = (Survived.count()/df["Survived"].count())*100

print()

print(f"{Survived["Survived"].count()} people survived out of {df["Survived"].count()}")

print(f"{(Percentage["Survived"]).round(2)} % People Survived" )

print()

print("-"*50)
print(f"The Data is Slightly Imbalanced")
print("-"*50)

Number_of_Males = (df[df["Sex"] == "male"].count())["Sex"]
Number_of_Females = df[df["Sex"] == "female"].count()["Sex"]

print(f"""No. of Males Survived = {Number_of_Males}
No. of Females Survived = {Number_of_Females}""")

print(f"Male/Female Ratio = {(Number_of_Males/Number_of_Females):.2f}")

print()
print("-"*50)
print("Class Wise Survival Rate")
print("-"*50)

# First Class Survival Rate

First_Class_Survivived = Survived[Survived["Pclass"]  == 1].count()["Pclass"]
Total_First_Class_Passengers = df[df["Pclass"] == 1].count()["Pclass"]
First_Class_Survival_Rate = First_Class_Survivived*100 / Total_First_Class_Passengers

print(f"First Class Survival Rate = {First_Class_Survival_Rate:.2f}")

# Second Class Survival Rate

Second_Class_Survivived = Survived[Survived["Pclass"]  == 2].count()["Pclass"]
Total_Second_Class_Passengers = df[df["Pclass"] == 2].count()["Pclass"]
Second_Class_Survival_Rate = Second_Class_Survivived*100 / Total_Second_Class_Passengers

print(f"Second Class Survival Rate = {Second_Class_Survival_Rate:.2f}")

# Third Class Survival Rate

Third_Class_Survivived = Survived[Survived["Pclass"]  == 3].count()["Pclass"]
Total_Third_Class_Passengers = df[df["Pclass"] == 3].count()["Pclass"]
Third_Class_Survival_Rate = Third_Class_Survivived*100 / Total_Third_Class_Passengers

print(f"Third Class Survival Rate = {Third_Class_Survival_Rate:.2f}")

print()
print("-"*50)
print("Adult and Child Survival Rate")
print("-"*50)

# Adult and Child Passengers and Survival Rate

Total_Passengers = df["PassengerId"].count()
No_of_Adult_Passengers = df[df["Age"] >= 18].count()["Age"]
No_of_Child_Passengers = df[df["Age"] < 18].count()["Age"]

print(f"Percentage of Adult Passengers = {(No_of_Adult_Passengers*100/Total_Passengers):.2f}")
print(f"Percentage of Child Passengers = {(No_of_Child_Passengers*100/Total_Passengers):.2f}")

Survived_Adult_Passengers = Survived[Survived["Age"] >= 18].count()["Age"]
Survived_Child_Passengers = Survived[Survived["Age"] < 18].count()["Age"]

Adult_Survival_Rate = Survived_Adult_Passengers*100/No_of_Adult_Passengers
Child_Survival_Rate = Survived_Child_Passengers*100/No_of_Child_Passengers
print()
print(f"Adult Survival Rate : {Adult_Survival_Rate:.2f}")
print(f"Child Survival Rate : {Child_Survival_Rate:.2f}")
print()