# Question 1


# Raj is the manager of a medical store. 
# To keep track of sales records, he has created a CSV file named Sales.csv, 
# which stores the details of each sale.   
# The columns of the CSV file are: Product_ID, Product_Name, Quantity_Sold and Price_Per_Unit.
# Help him to efficiently maintain the data by creating the following user-defined functions: 
# I. Accept() – to accept a sales record from the user and add it to the file Sales.csv. 
# II. CalculateTotalSales() – to calculate and return the total sales based on the Quantity_Sold and Price_Per_Unit. 

import csv

def Accept():
    
    f = open("Sales.csv" , "a")
    Product_Id = input("Enter Product Id: ")
    Product_Name = input("Enter Product Name: ")
    Quantity_Sold = float(input("Enter Quantity Sold: "))
    Price_Per_Unit = float(input("Enter Price Per Unit: "))

    csv_writer = csv.writer(f)
    csv_writer.writerow([Product_Id , Product_Name , Quantity_Sold , Price_Per_Unit])

    f.close()

def CalculateTotalSales():

    f = open("Sales.csv" , "r")
    csv_reader = csv.reader(f)
    Total = 0

    next(csv_reader)

    for i in csv_reader:
        Qty_Sold = float(i[2])
        Price = float(i[3])

        Total += Qty_Sold*Price
    f.close()

    return Total

    
# Question 2

# A csv file "P_record.csv" contains the records of patients in a hospital.
# Each record of the file contains the following data :

# ~Name of a patient
# ~Disease
# ~Number of days patient is admitted
# ~Amount

# For example, a sample record of the file may be :
# ["Gunjan" , Jaundice" , 4 , 15000]
# Write the following Python functions to perform the specified operations
# on this file :
# (i)Write a function read data ( ) which reads all the data from the
# file and displays the details of all the Cancer patients.
# (ii)Write a function count rec ( ) which counts and returns the
# number of records in the file.

import csv

def read_data():
    f = open("P_record.csv" , "r")

    reader = csv.reader(f)
    next(reader)

    for i in reader:
        if i[1] == "Cancer":
            print(i)
    f.close()

def count_rec():
    f = open("P_record.csv" , "r")

    count = 0
    reader = csv.reader(f)
    next(reader)

    for i in reader:
        count += 1

    print("Total Records" , count)
    f.close()

# Question 3

# A csv file "States.csv" contains some data about all the states of India.
# Each record of the file contains the following data : 4

# ~ Name of the State
# ~ Capital of the State
# ~ Population of the State
# ~ Official Language of the State

# For example, a sample record in the file is :
# ['Andhra Pradesh','Amaravati',52221000,'Telugu']

# Write a Python program which reads the data from this file and appends
# all those records where population is more than 10000000 into another
# csv file 'More.csv'.

# Note : "States.csv" also contains the Header row. The Header row
# should NOT be copied to "More.csv".

import csv

States = open("States.csv" , "r")
More = open("More.csv" , "a")

S_reader = csv.reader(States)
next(S_reader)

M_writer = csv.writer(More)

for i in S_reader:
    if int(i[2]) > 10000000:
        M_writer.writerow(i)

States.close()
More.close()
