import pandas as pd

d = {
    "Names" : ["A","B","C"] , 
    "Age" : [35 , 43 , 24] ,
    "Gender" : ["M" , "F" , "M"]
}

df = pd.DataFrame(d , index = ["Employee 1","Employee 2","Employee 3"])

print(df)

print(df.loc["Employee 1"])

print(df.iloc[0])

# Adding a new column

df["Position"] = ["Cook","N/A","Cashier"]

print(df)

# Adding a new row

new_row = pd.DataFrame([{"Names" : "D" , "Age" : 28 , "Gender" : "F" , "Position" : "Engineer" }] , 
                       index = ["Employee 4"])

df = pd.concat([df , new_row])

print(df)