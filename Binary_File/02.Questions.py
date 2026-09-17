# Question 1

# A file, PASSENGERS.DAT, stores the records of passengers using the

# following structure :

# [PNR, PName, BRDSTN, DESTN, FARE]
# where:
# PNR
# PName: Passenger Number (string type)
# BRDSTN: Passenger Name (string type)
# DESTN: Boarding Station Name (string type)
# FARE: Destination Station Name (string type)
 
# Fare amount for the journey (float type)

# Write user defined functions in Python for the following tasks :

# (i)   Create () — to input data for passengers and write it in the binary
#       file PASSENGERS . DAT.

# (ii)  SearchDestn (D) — to read contents from the file PASSENGERS . DAT
#       and display the details of those Passengers whose DESTN matches
#       with the value of D.

# (iii) UpdateFare ()— to increase the fare of all passengers by 5% and
#       rewrite the updated records into the file PASSENGERS . DAT.

import pickle

def Create():
    file = open("PASSENGERS.DAT" , "ab")

    PNR = int(input("Enter PNR: "))
    PName = input("Passenger Number: ") 
    BRDSTN = input("Passenger Name: ") 
    DESTN = input("Boarding Station Name: ") 
    FARE = float(input("Destination Station Name: "))

    Details = [PNR , PName , BRDSTN , DESTN , FARE]

    pickle.dump(Details , file)

    file.close()

def SearchDstn(D):
    file = open("PASSENGERS.DAT" , "rb")

    try:
        while True:
            data = pickle.load(file)

            if data[3] == D:
                print(data)
    except EOFError:
        file.close()

def UpdateFare():
    file = open("PASSENGERS.DAT" , "rb")

    records = []

    try:
        while True:
            data = pickle.load(file)
            data[4] = (data[4]*105)/100
            records.append(data)

    except EOFError:
        file.close()

    file = open("PASSENGERS.DAT" , "wb")

    for record in records:
        pickle.dump(record , file)

    file.close()

# Question 2
# Mr. Ravi, a manager at a tech company, needs to maintain records of employees. Each
# record should include: Employee_lD, Employee_Name, Department and Salary.

# Write the Python functions to:

# |.Input employee data and append it to a binary file.
# ||. Update the salary of employees in the "IT" department to 200000.

import pickle

def InputEmployee():
    f = open("employee.dat", "ab")

    Employee_ID = int(input("Enter Employee ID: "))
    Employee_Name = input("Enter Employee Name: ")
    Department = input("Enter Department: ")
    Salary = float(input("Enter Salary: "))

    record = [Employee_ID, Employee_Name, Department, Salary]

    pickle.dump(record, f)

    f.close()


def UpdateSalary():
    f = open("employee.dat", "rb")

    records = []

    try:
        while True:
            record = pickle.load(f)

            if record[2] == "IT":
                record[3] = 200000

            records.append(record)

    except EOFError:
        f.close()

    f = open("employee.dat", "wb")

    for record in records:
        pickle.dump(record, f)

    f.close()