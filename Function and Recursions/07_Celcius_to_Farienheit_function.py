Temp_Celcius = float(input("Input temperature in Celcius: "))

def Celcius_To_Farenheit(Temp_Celcius):
    Temp_Farenheit = (9/5)*(Temp_Celcius) + 32
    return Temp_Farenheit

print(f"{round (Celcius_To_Farenheit(Temp_Celcius) , 2)}" , "°F")