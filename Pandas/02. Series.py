import pandas as pd

data = [100 , 101 , 400 , 200 , 202]

series = pd.Series(data , index = ["a" , "b" , "c" , "d" , "e"])

print(series)

print(series.loc["a"]) #loc ----> Location by label

series.loc["a"] = 200

print(series)

print(series.iloc[0])   #iloc Location by integer

print(series[series >= 200])

calories = {"Day 1" : 1750 , "Day 2" : 2100 , "Day 3" : 1700}

series = pd.Series(calories)

print(series)

series.loc["Day 3"] += 500

print(series.loc["Day 1"])

print(series[series >= 2000])

print(series[series < 2000])

#Example

Pokemon_names = ["Bulbasaur","Ivysaur","Charizard","Charmandar","Pikachu"]

Series_1 = pd.Series(Pokemon_names , index = [1 , 2 , 3 , 4 , 5 ])

print(Series_1)