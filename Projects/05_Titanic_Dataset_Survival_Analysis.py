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

    if len(labels) != len(values):
        raise ValueError("Labels and values must have the same length.")

    table = pd.DataFrame({
        column_names[0]: labels,
        column_names[1]: values
    })

    return table


df = pd.read_csv(r"D:\DEV\Programming\PYTHON\Projects\~~Titanic.csv")

# -------------------------------
# DATA CLEANING
# -------------------------------

df["Age"] = df["Age"].fillna(df["Age"].median())

df.drop("Cabin", axis=1, inplace=True)

df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

df["Survived"] = df["Survived"].astype(bool)

Survived = df[df["Survived"]]

# -------------------------------
# OVERALL SURVIVAL STATISTICS
# -------------------------------

print("\n" + "="*50)
print("OVERALL SURVIVAL STATISTICS")
print("="*50)

summary = make_table(
    ["Total Passengers",
     "Passengers Survived",
     "Survival Percentage"],

    [len(df),
     len(Survived),
     f"{(len(Survived)*100 / len(df)):.2f}%"],

    ("Statistic", "Value")
)

print(summary.to_string(index=False))

print("\nConclusion:")
print(f"Out of {len(df)} passengers, {len(Survived)} survived.")
print("This indicates that survival was relatively rare during the disaster.")

# -------------------------------
# SURVIVAL BY GENDER
# -------------------------------

print("\n" + "="*50)
print("SURVIVAL BY GENDER")
print("="*50)

Number_of_Males = len(df[df["Sex"] == "male"])
Number_of_Females = len(df[df["Sex"] == "female"])

Number_of_Males_Survived = len(Survived[Survived["Sex"] == "male"])
Number_of_Females_Survived = len(Survived[Survived["Sex"] == "female"])

Male_Female_Stat = make_table(
    ["No. of Males",
     "No. of Females",
     "Number of Males Survived",
     "Number of Females Survived",
     "Male/Female Surviving Ratio",
     "Percentage Males Survived",
     "Percentage Females Survived"],

    [Number_of_Males,
     Number_of_Females,
     Number_of_Males_Survived,
     Number_of_Females_Survived,
     round(Number_of_Males_Survived/Number_of_Females_Survived, 2),
     f"{(Number_of_Males_Survived*100/Number_of_Males):.2f} %",
     f"{(Number_of_Females_Survived*100/Number_of_Females):.2f} %"],

    ("Metric", "Value")
)

print(Male_Female_Stat.to_string(index=False))

print("\nConclusion:")
print("Female passengers had a significantly higher survival rate.")
print("This supports the 'women and children first' evacuation policy during the sinking of the",
      "the", ".")

# -------------------------------
# CLASS WISE SURVIVAL RATE
# -------------------------------

print("\n" + "="*50)
print("CLASS WISE SURVIVAL RATE")
print("="*50)

First_Class_Survivived = len(Survived[Survived["Pclass"] == 1])
Total_First_Class_Passengers = len(df[df["Pclass"] == 1])
First_Class_Survival_Rate = First_Class_Survivived*100 / Total_First_Class_Passengers

Second_Class_Survivived = len(Survived[Survived["Pclass"] == 2])
Total_Second_Class_Passengers = len(df[df["Pclass"] == 2])
Second_Class_Survival_Rate = Second_Class_Survivived*100 / Total_Second_Class_Passengers

Third_Class_Survivived = len(Survived[Survived["Pclass"] == 3])
Total_Third_Class_Passengers = len(df[df["Pclass"] == 3])
Third_Class_Survival_Rate = Third_Class_Survivived*100 / Total_Third_Class_Passengers

First_Class_Male_Survival = (
    len(Survived[(Survived["Sex"] == "male") & (Survived["Pclass"] == 1)]) *100 /
    len(df[(df["Sex"] == "male") & (df["Pclass"] == 1)])
)

Third_Class_Female_Survival = (
    len(Survived[(Survived["Sex"] == "female") & (Survived["Pclass"] == 3)]) *100 /
    len(df[(df["Sex"] == "female") & (df["Pclass"] == 3)])
)

Class_Wise_Survival_Report = make_table(
    ["First Class Survival Rate",
     "Second Class Survival Rate",
     "Third Class Survival Rate",
     "Survival of First Class Males",
     "Survival of Third Class Females"],

    [f"{First_Class_Survival_Rate:.2f} %",
     f"{Second_Class_Survival_Rate:.2f} %",
     f"{Third_Class_Survival_Rate:.2f} %",
     f"{First_Class_Male_Survival:.2f} %",
     f"{Third_Class_Female_Survival:.2f} %"],

    ("Class", "Value")
)

print(Class_Wise_Survival_Report.to_string(index=False))

print("\nConclusion:")
print("Passengers in higher classes had better survival chances.")
print("However, even third-class females had higher survival chances than first-class males.")
print("This indicates that gender had a stronger influence on survival than class.")

# -------------------------------
# ADULT VS CHILD SURVIVAL
# -------------------------------

print("\n" + "="*50)
print("ADULT VS CHILD SURVIVAL")
print("="*50)

Total_Passengers = len(df)

No_of_Adult_Passengers = len(df[df["Age"] >= 18])
No_of_Child_Passengers = len(df[df["Age"] < 18])

Survived_Adult_Passengers = len(Survived[Survived["Age"] >= 18])
Survived_Child_Passengers = len(Survived[Survived["Age"] < 18])

Adult_Survival_Rate = Survived_Adult_Passengers*100/No_of_Adult_Passengers
Child_Survival_Rate = Survived_Child_Passengers*100/No_of_Child_Passengers

Adult_Child_Survival_Rate_Summary = make_table(
    ["Percentage of Adult Passengers",
     "Percentage of Child Passengers",
     "Adult Survival Rate",
     "Child Survival Rate"],

    [f"{(No_of_Adult_Passengers*100/Total_Passengers):.2f} %",
     f"{(No_of_Child_Passengers*100/Total_Passengers):.2f} %",
     f"{Adult_Survival_Rate:.2f} %",
     f"{Child_Survival_Rate:.2f} %"],

    ("Metric", "Value")
)

print(Adult_Child_Survival_Rate_Summary.to_string(index=False))

print("\nConclusion:")
print("Children had a higher survival rate than adults.")
print("This again supports the 'women and children first' rescue priority.")

# -------------------------------
# SURVIVAL BY EMBARKED PORT
# -------------------------------

print("\n" + "="*50)
print("SURVIVAL BY EMBARKED PORT")
print("="*50)

Survival_Per_C = len(Survived[Survived["Embarked"] == "C"]) *100 / len(df[df["Embarked"] == "C"])
Survival_Per_Q = len(Survived[Survived["Embarked"] == "Q"]) *100 / len(df[df["Embarked"] == "Q"])
Survival_Per_S = len(Survived[Survived["Embarked"] == "S"]) *100 / len(df[df["Embarked"] == "S"])

Survival_By_Embarked_Port = make_table(
    ["Cherbourg Survival Percentage",
     "Queenstown Survival Percentage",
     "Southampton Survival Percentage"],

    [f"{Survival_Per_C:.2f} %",
     f"{Survival_Per_Q:.2f} %",
     f"{Survival_Per_S:.2f} %"],

    ("Port", "Percent")
)

print(Survival_By_Embarked_Port.to_string(index=False))

print("\nConclusion:")
print("Survival rates vary depending on the embarkation port.")
print("This may be related to differences in passenger class distribution across ports.")

# -------------------------------
# FINAL ANALYSIS SUMMARY
# -------------------------------

print("\n" + "="*50)
print("FINAL ANALYSIS SUMMARY")
print("="*50)

print("1. Gender was the strongest survival factor.")
print("2. Passenger class also strongly influenced survival chances.")
print("3. Children had better survival chances than adults.")
print("4. Embarkation port showed smaller differences in survival.")