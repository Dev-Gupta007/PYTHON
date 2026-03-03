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

def make_table(labels, values, column_names=("Metric", "Value")):
    """
    Creates a pandas DataFrame table from labels and values.

    labels: list of row names
    values: list of corresponding values
    column_names: tuple for column titles
    """

    if len(labels) != len(values):
        raise ValueError("Labels and values must have the same length.")

    table = pd.DataFrame({
        column_names[0]: labels,
        column_names[1]: values
    })

    return table

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

Survived = df[df["Survived"]] 

Percentage = (Survived.count()/df["Survived"].count())*100

print()

summary = make_table(   
    ["  Total Passengers    ",
     "Passengers Survived   ",
     "Survival Percentage   "],

    [df['PassengerId'].count().round(2),
     Survived['Survived'].count().round(2),
     f"{(Survived['Survived'].count()*100 / df['Survived'].count()):.2f}%"],

    ("     Statistic     ", 
     "Value")
)

print(summary.to_string(index = False))

print()

# Survival By Gender

print("-"*50)
print(f"The Data is Slightly Imbalanced")
print("-"*50)

Number_of_Males = (df[df["Sex"] == "male"].count())["Sex"]
Number_of_Females = df[df["Sex"] == "female"].count()["Sex"]
Number_of_Males_Survived = Survived[Survived["Sex"] == 'male'].count()['Sex']
Number_of_Females_Survived = Survived[Survived["Sex"] == 'female'].count()['Sex']

Male_Female_Stat = make_table(
    ["No. of Males                  ",
     "No. of Females                ",
     "Number of Males Survived      ",
     "Number of Females Survived    ",
     "Male/Female Surviving Ratio   ",
     "Percentage Males Survived     ",
     "Percentage Females Survived   "],

    [Number_of_Males,
     Number_of_Females,
     Number_of_Males_Survived,
     Number_of_Females_Survived,
     round(Number_of_Males_Survived/Number_of_Females_Survived, 2),
     f"{(Number_of_Males_Survived*100/Number_of_Males):.2f} %",
     f"{(Number_of_Females_Survived*100/Number_of_Females):.2f} %"],

     ("          Metric           ",
      "Value")
)

print(Male_Female_Stat.to_string(index = False))

print()
print("-"*50)
print("Class Wise Survival Rate")
print("-"*50)

# First Class Survival Rate

First_Class_Survivived = Survived[Survived["Pclass"]  == 1].count()["Pclass"]
Total_First_Class_Passengers = df[df["Pclass"] == 1].count()["Pclass"]
First_Class_Survival_Rate = First_Class_Survivived*100 / Total_First_Class_Passengers

# Second Class Survival Rate

Second_Class_Survivived = Survived[Survived["Pclass"]  == 2].count()["Pclass"]
Total_Second_Class_Passengers = df[df["Pclass"] == 2].count()["Pclass"]
Second_Class_Survival_Rate = Second_Class_Survivived*100 / Total_Second_Class_Passengers

# Third Class Survival Rate

Third_Class_Survivived = Survived[Survived["Pclass"]  == 3].count()["Pclass"]
Total_Third_Class_Passengers = df[df["Pclass"] == 3].count()["Pclass"]
Third_Class_Survival_Rate = Third_Class_Survivived*100 / Total_Third_Class_Passengers

Class_Wise_Survival_Report = make_table(
    ["Second Class Survival Rate    ",
     "First Class Survival Rate     ",
     "Third Class Survival Rate     "],

    [f"{Second_Class_Survival_Rate:.2f} %", 
     f"{First_Class_Survival_Rate:.2f} %", 
     f"{Third_Class_Survival_Rate:.2f} %"],

     ("Class             " , "Value")
)


print(Class_Wise_Survival_Report.to_string(index = False))
print()
print("-"*50)
print("Adult and Child Survival Rate")
print("-"*50)

# Survival by Age

Total_Passengers = df["PassengerId"].count()
No_of_Adult_Passengers = df[df["Age"] >= 18].count()["Age"]
No_of_Child_Passengers = df[df["Age"] < 18].count()["Age"]
Survived_Adult_Passengers = Survived[Survived["Age"] >= 18].count()["Age"]
Survived_Child_Passengers = Survived[Survived["Age"] < 18].count()["Age"]
Adult_Survival_Rate = Survived_Adult_Passengers*100/No_of_Adult_Passengers
Child_Survival_Rate = Survived_Child_Passengers*100/No_of_Child_Passengers

Adult_Child_Survival_Rate_Summary = make_table(
    ["Percentage of Adult Passengers    ",
     "Percentage of Child Passengers    ",
     "Adult Survival Rate               ",
     "Child Survival Rate               "],
 
    [f"{(No_of_Adult_Passengers*100/Total_Passengers):.2f} %",
     f"{(No_of_Child_Passengers*100/Total_Passengers):.2f} %",
     f"{Adult_Survival_Rate:.2f} %",
     f"{Child_Survival_Rate:.2f} %"],

     ("Metric                 " , "Value")

)

print(Adult_Child_Survival_Rate_Summary.to_string(index = False))
print()

# Survival By Embarked Port

# | Code | Port Name   | Country |
# | ---- | ----------- | ------- |
# | C    | Cherbourg   | France  |
# | Q    | Queenstown  | Ireland |
# | S    | Southampton | England |

Survival_Per_C = Survived[Survived["Embarked"] == "C"].count()["Embarked"]*100/df[df["Embarked"] == "C"].count()["Embarked"]
Survival_Per_Q = Survived[Survived["Embarked"] == "Q"].count()["Embarked"]*100/df[df["Embarked"] == "Q"].count()["Embarked"]
Survival_Per_S = Survived[Survived["Embarked"] == "S"].count()["Embarked"]*100/df[df["Embarked"] == "S"].count()["Embarked"]

Survival_By_Embarked_Port = make_table(

    ["Survival Percentage of Cherbourg   ",
     "Survival Percentage of Queenstown  ",
     "Survival Percentage of Southampton "],

    [Survival_Per_C,
     Survival_Per_Q,
     Survival_Per_S],

    ("Port                   ",
     "Percent")
)

print(Survival_By_Embarked_Port)


