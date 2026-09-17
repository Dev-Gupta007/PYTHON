# ============================================================
#                    BINARY FILES
#                 CBSE CLASS 12 CS
# ============================================================

# Binary files store data in binary form (0s and 1s).
# They can store Python objects such as lists, tuples,
# dictionaries, etc.

# The pickle module is used to work with Python objects
# in binary files.

import pickle


# ------------------------------------------------------------
# 1. OPENING A BINARY FILE
# ------------------------------------------------------------

# Writing binary data
f = open("data.dat", "wb")

# Reading binary data
f = open("data.dat", "rb")

# Appending binary data
f = open("data.dat", "ab")


# Common modes:

# "rb"  -> Read Binary
# "wb"  -> Write Binary
# "ab"  -> Append Binary


# ------------------------------------------------------------
# 2. pickle.dump()
# ------------------------------------------------------------

# dump() is used to write a Python object
# into a binary file.

import pickle

f = open("data.dat", "wb")

data = [10, 20, 30, 40]

pickle.dump(data, f)

f.close()


# Syntax:
# pickle.dump(object, file)


# Example:

student = {
    "Name": "Rahul",
    "Marks": 95
}

f = open("student.dat", "wb")

pickle.dump(student, f)

f.close()


# IMPORTANT:
# dump() -> WRITE an object into a binary file.


# ------------------------------------------------------------
# 3. pickle.load()
# ------------------------------------------------------------

# load() is used to READ an object from a binary file.

import pickle

f = open("data.dat", "rb")

data = pickle.load(f)

print(data)

f.close()


# Syntax:
# pickle.load(file)


# IMPORTANT:
# load() -> READ one object from a binary file.


# ------------------------------------------------------------
# 4. dump() vs load()
# ------------------------------------------------------------

# dump()
# Python object ---> Binary File

# load()
# Binary File ---> Python object


# Example:

data = [10, 20, 30]

f = open("data.dat", "wb")
pickle.dump(data, f)
f.close()


f = open("data.dat", "rb")
x = pickle.load(f)
print(x)
f.close()


# ------------------------------------------------------------
# 5. WRITING MULTIPLE OBJECTS
# ------------------------------------------------------------

# Multiple objects can be stored in the same binary file.

f = open("data.dat", "wb")

pickle.dump(10, f)
pickle.dump(20, f)
pickle.dump(30, f)

f.close()


# The objects are stored one after another.


# ------------------------------------------------------------
# 6. READING MULTIPLE OBJECTS
# ------------------------------------------------------------

# load() reads ONE object at a time.

f = open("data.dat", "rb")

x = pickle.load(f)
print(x)

x = pickle.load(f)
print(x)

x = pickle.load(f)
print(x)

f.close()


# Output:
# 10
# 20
# 30


# ------------------------------------------------------------
# 7. EOFError
# ------------------------------------------------------------

# If we keep using pickle.load() after all objects
# have been read, EOFError occurs.

# Example:

f = open("data.dat", "rb")

try:
    while True:
        data = pickle.load(f)
        print(data)

except EOFError:
    print("End of file reached")

f.close()


# This is a VERY IMPORTANT pattern for CBSE questions.


# ------------------------------------------------------------
# 8. Reading a Binary File using while True
# ------------------------------------------------------------

import pickle

f = open("student.dat", "rb")

try:
    while True:
        student = pickle.load(f)
        print(student)

except EOFError:
    pass

f.close()


# EOFError tells us that there are no more objects
# to read.


# ------------------------------------------------------------
# 9. SEARCHING A BINARY FILE
# ------------------------------------------------------------

# Example:
# Find students whose marks are greater than 90.

import pickle

f = open("student.dat", "rb")

try:
    while True:
        student = pickle.load(f)

        if student["Marks"] > 90:
            print(student)

except EOFError:
    pass

f.close()


# ------------------------------------------------------------
# 10. COUNTING RECORDS
# ------------------------------------------------------------

import pickle

f = open("student.dat", "rb")

count = 0

try:
    while True:
        student = pickle.load(f)
        count += 1

except EOFError:
    pass

f.close()

print("Number of records =", count)


# ------------------------------------------------------------
# 11. MODIFYING / UPDATING A BINARY FILE
# ------------------------------------------------------------

# A common CBSE method is:
#
# 1. Read records from the original file
# 2. Modify the required record
# 3. Write records into a temporary file
# 4. Replace the original file


# Example idea:

import pickle

f = open("student.dat", "rb")
temp = open("temp.dat", "wb")

try:
    while True:
        student = pickle.load(f)

        if student["RollNo"] == 5:
            student["Marks"] = 95

        pickle.dump(student, temp)

except EOFError:
    pass

f.close()
temp.close()


# The original file can then be replaced with temp file
# using os module.


# ------------------------------------------------------------
# 12. os.replace()
# ------------------------------------------------------------

# Used to replace the original file with another file.

import os

os.replace("temp.dat", "student.dat")


# Syntax:
# os.replace(source, destination)


# ------------------------------------------------------------
# 13. tell()
# ------------------------------------------------------------

# tell() returns the current position of the file pointer.

f = open("data.dat", "rb")

print(f.tell())

f.close()


# Example:

f = open("data.dat", "rb")

print(f.tell())

data = pickle.load(f)

print(f.tell())

f.close()


# NOTE:
# With binary files, tell() gives the current position
# of the file pointer in bytes.


# ------------------------------------------------------------
# 14. seek()
# ------------------------------------------------------------

# seek() moves the file pointer to a specified position.

# Syntax:

# file.seek(position)


f = open("data.dat", "rb")

f.seek(0)

data = pickle.load(f)

print(data)

f.close()


# seek(0) moves the file pointer to the beginning.


# ------------------------------------------------------------
# 15. seek() with tell()
# ------------------------------------------------------------

f = open("data.dat", "rb")

print(f.tell())       # Current position

f.seek(10)

print(f.tell())       # Position 10

f.close()


# ------------------------------------------------------------
# 16. FILE POINTER
# ------------------------------------------------------------

# When a file is opened:

f = open("data.dat", "rb")

# File pointer starts at the beginning.

# Reading data moves the pointer forward.

# seek() can move the pointer to another position.

# tell() tells us the current position.


# ------------------------------------------------------------
# 17. IMPORTANT DIFFERENCE:
#     TEXT FILE vs BINARY FILE
# ------------------------------------------------------------

# TEXT FILE:

f = open("data.txt", "r")

# Reads text data.


# BINARY FILE:

f = open("data.dat", "rb")

# Reads binary data.


# Binary files commonly use:
# .dat


# ------------------------------------------------------------
# 18. pickle.dump() DOES NOT MEAN NORMAL WRITE
# ------------------------------------------------------------

# For binary files containing Python objects:

pickle.dump(data, f)


# NOT:

f.write(data)


# because write() expects bytes when the file
# is opened in binary mode.


# ------------------------------------------------------------
# 19. read() AND write() WITH BINARY FILES
# ------------------------------------------------------------

# Binary files can also use read() and write()
# when working directly with bytes.

f = open("data.dat", "wb")

f.write(b"Hello")

f.close()


# b"Hello" is a bytes object.


# Reading:

f = open("data.dat", "rb")

data = f.read()

print(data)

f.close()


# Output:
# b'Hello'


# ------------------------------------------------------------
# 20. pickle vs read/write
# ------------------------------------------------------------

# pickle.dump() / pickle.load()
#
# Used when storing Python objects.

data = [10, 20, 30]

pickle.dump(data, f)


# read() / write()
#
# Used when directly working with bytes.

f.write(b"Hello")


# ------------------------------------------------------------
# 21. APPENDING RECORDS
# ------------------------------------------------------------

# "ab" is used to add objects at the end
# of an existing binary file.

import pickle

f = open("student.dat", "ab")

student = {
    "RollNo": 4,
    "Name": "Aman",
    "Marks": 88
}

pickle.dump(student, f)

f.close()


# ------------------------------------------------------------
# 22. COMPLETE RECORD-WRITING EXAMPLE
# ------------------------------------------------------------

import pickle

f = open("student.dat", "wb")

student1 = [1, "Aman", 90]
student2 = [2, "Riya", 95]
student3 = [3, "Karan", 87]

pickle.dump(student1, f)
pickle.dump(student2, f)
pickle.dump(student3, f)

f.close()


# ------------------------------------------------------------
# 23. COMPLETE RECORD-READING EXAMPLE
# ------------------------------------------------------------

import pickle

f = open("student.dat", "rb")

try:
    while True:
        student = pickle.load(f)
        print(student)

except EOFError:
    pass

f.close()


# ------------------------------------------------------------
# 24. SEARCHING BY ROLL NUMBER
# ------------------------------------------------------------

import pickle

f = open("student.dat", "rb")

roll = int(input("Enter roll number: "))

try:
    while True:
        student = pickle.load(f)

        if student[0] == roll:
            print(student)

except EOFError:
    pass

f.close()


# ------------------------------------------------------------
# 25. DELETING A RECORD
# ------------------------------------------------------------

# Binary files are generally not modified directly
# record-by-record.
#
# Instead:
#
# Original File
#       |
#       v
# Read each record
#       |
#       v
# Skip unwanted record
#       |
#       v
# Write remaining records to temporary file
#       |
#       v
# Replace original file


# ------------------------------------------------------------
# 26. IMPORTANT METHODS AT A GLANCE
# ------------------------------------------------------------

# open("file.dat", "rb")
# -> Open binary file for reading

# open("file.dat", "wb")
# -> Open binary file for writing

# open("file.dat", "ab")
# -> Open binary file for appending

# pickle.dump(obj, file)
# -> Write one Python object

# pickle.load(file)
# -> Read one Python object

# file.read()
# -> Read bytes

# file.write(bytes)
# -> Write bytes

# file.seek(position)
# -> Move file pointer

# file.tell()
# -> Return current file pointer position

# os.replace(old, new)
# -> Replace one file with another


# ============================================================
#                    MOST IMPORTANT
# ============================================================

# Text File:
#
# open("data.txt", "r")
# read()
# readline()
# readlines()
# write()
# writelines()


# Binary File:
#
# import pickle
#
# open("data.dat", "rb")
# open("data.dat", "wb")
# open("data.dat", "ab")
#
# pickle.dump()
# pickle.load()
#
# seek()
# tell()
#
# EOFError while reading until the end