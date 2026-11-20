
# ============================================================
#        CLASS XII COMPUTER SCIENCE
#        CONNECTIVITY OF SQL WITH PYTHON
#                 COMPLETE NOTES
# ============================================================

# 1. INTRODUCTION TO DATABASE CONNECTIVITY
# ------------------------------------------------------------

# Database Connectivity means establishing a connection between
# a Python program and a MySQL database so that Python can
# interact with the database.

# Using Python, we can:
# 1. Create databases and tables.
# 2. Insert records into tables.
# 3. Retrieve records from tables.
# 4. Update existing records.
# 5. Delete records.
# 6. Execute SQL queries.

# Python communicates with MySQL using the mysql.connector
# module.

# 2. ESTABLISHING A CONNECTION
# ------------------------------------------------------------

# The connect() function establishes a connection between
# Python and MySQL.

# SYNTAX:
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="school"
)

# PARAMETERS:

# host       : Address of MySQL server.
# user       : MySQL username.
# password   : MySQL password.
# database   : Name of database to connect to.

# IMPORTANT POINTS:

# 1. localhost means MySQL server running on the same computer.
# 2. mydb is a connection object.
# 3. The database must exist before connecting using the
#    database parameter.

# 3. CREATING A CURSOR
# ------------------------------------------------------------

# A cursor is an object used to execute SQL statements and
# retrieve query results.

# SYNTAX:

mycursor = mydb.cursor()

# Here:
# mydb      : Connection object.
# mycursor  : Cursor object.

# Connection object:
# Establishes connection with MySQL.

# Cursor object:
# Executes SQL commands and retrieves query results.

# 4. EXECUTING SQL QUERIES
# ------------------------------------------------------------

# The execute() method is used to execute an SQL statement
# through a cursor.

# SYNTAX:

mycursor.execute("SQL QUERY")

# EXAMPLE:

mycursor.execute("SELECT * FROM STUDENT")

# 5. CREATING A DATABASE
# ------------------------------------------------------------

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE SCHOOL")

# To display databases:

# mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

# 6. CREATING A TABLE
# ------------------------------------------------------------

# SQL QUERY:

# CREATE TABLE STUDENT (
#     ROLLNO INT PRIMARY KEY,
#     NAME VARCHAR(30),
#     MARKS FLOAT
# );

# PYTHON:

mycursor.execute("""
CREATE TABLE STUDENT (
    ROLLNO INT PRIMARY KEY,
    NAME VARCHAR(30),
    MARKS FLOAT
)
""")

# 7. INSERTING RECORDS
# ------------------------------------------------------------

# SQL SYNTAX:

# INSERT INTO TABLE_NAME
# VALUES (value1, value2, value3);

# PYTHON:

sql = "INSERT INTO STUDENT VALUES (1, 'Aman', 95)"

mycursor.execute(sql)

mydb.commit()

# COMMIT():

# The commit() method saves changes made to the database.

# It is generally required after:
# 1. INSERT
# 2. UPDATE
# 3. DELETE

# 8. INSERTING MULTIPLE RECORDS
# ------------------------------------------------------------

# The executemany() method executes the same SQL statement
# for multiple sets of values.

# SYNTAX:

# mycursor.executemany(sql, values)

# EXAMPLE:

sql = "INSERT INTO STUDENT VALUES (%s, %s, %s)"

values = [
    (1, "Aman", 95),
    (2, "Rahul", 88),
    (3, "Riya", 92)
]

mycursor.executemany(sql, values)

mydb.commit()

# DIFFERENCE:

# execute():
# Executes a statement with one set of parameters.

# executemany():
# Executes a statement for multiple sets of parameters.

# 9. PARAMETERIZED QUERIES
# ------------------------------------------------------------

# Parameterized queries allow values to be passed separately
# from the SQL query.

# %s is the placeholder used by MySQL Connector for values
# of different data types.

# EXAMPLE:

sql = "INSERT INTO STUDENT VALUES (%s, %s, %s)"

values = (1, "Aman", 95)

mycursor.execute(sql, values)

mydb.commit()

# IMPORTANT:

# 1. %s is a placeholder.
# 2. Values are passed as a tuple or suitable sequence.
# 3. Strings do not need manual quotation marks inside the
#    values tuple.
# 4. Parameterized queries help prevent SQL injection.

# 10. DISPLAYING RECORDS - SELECT
# ------------------------------------------------------------

# SELECT retrieves records from a database.

# mycursor.execute("SELECT * FROM STUDENT")

# A. fetchone()

# Returns one record at a time.

# record = mycursor.fetchone()

# If no more records are available, it returns None.

# B. fetchall()

# Returns all remaining records as a list of tuples.

# records = mycursor.fetchall()

# for row in records:
#     print(row)

# C. fetchmany(n)

# Returns up to n remaining records.

# records = mycursor.fetchmany(2)

# COMPARISON:

# fetchone():
# One record; returns a tuple or None.

# fetchall():
# All remaining records; returns a list of tuples.

# fetchmany(n):
# Up to n remaining records; returns a list of tuples.

# IMPORTANT:

# Fetching methods consume records from the cursor's current
# result position.

# If SELECT returns 5 records:

mycursor.execute("SELECT * FROM STUDENT")

print(mycursor.fetchone())
print(mycursor.fetchall())

# fetchone() retrieves the first record.
# fetchall() retrieves the remaining 4 records.

# 11. UPDATING RECORDS
# ------------------------------------------------------------

# UPDATE modifies existing records.

# SQL:

# UPDATE STUDENT
# SET MARKS = 98
# WHERE ROLLNO = 1;

# PYTHON:

sql = "UPDATE STUDENT SET MARKS = %s WHERE ROLLNO = %s"

values = (98, 1)

mycursor.execute(sql, values)

mydb.commit()

# Without WHERE, all records in the table may be updated.

# 12. DELETING RECORDS
# ------------------------------------------------------------

# DELETE removes records from a table.

# SQL:

# DELETE FROM STUDENT
# WHERE ROLLNO = 2;

# PYTHON:

sql = "DELETE FROM STUDENT WHERE ROLLNO = %s"

values = (2,)

mycursor.execute(sql, values)

mydb.commit()

# DELETE:
# Removes records.

# DROP TABLE:
# Removes the entire table structure and its records.

# TRUNCATE TABLE:
# Removes all records but retains table structure.

# 13. IMPORTANT CURSOR AND CONNECTION METHODS
# ------------------------------------------------------------

# connect()      : Establishes connection.
# cursor()       : Creates cursor object.
# execute()      : Executes SQL statement.
# executemany()  : Executes statement for multiple parameter sets.
# fetchone()     : Retrieves one record.
# fetchall()     : Retrieves all remaining records.
# fetchmany(n)   : Retrieves up to n records.
# commit()       : Saves database changes.
# rollback()     : Undoes uncommitted transactional changes.
# close()        : Closes cursor or connection.

# 14. IMPORTANT CURSOR ATTRIBUTES
# ------------------------------------------------------------

# A. rowcount

# Returns the number of rows affected by the last operation,
# or the number of rows returned by SELECT after fetching has
# completed, depending on the connector.

# EXAMPLE:

mycursor.execute(
    "UPDATE STUDENT SET MARKS = 90 WHERE ROLLNO = 1"
)

print(mycursor.rowcount)

mydb.commit()

# B. lastrowid

# Returns the generated value for an AUTO_INCREMENT column
# after an INSERT, when applicable.

# EXAMPLE:

mycursor.execute(
    "INSERT INTO EMPLOYEE (NAME, SALARY) VALUES ('Aman', 25000)"
)

print(mycursor.lastrowid)

mydb.commit()

# C. description

# Provides information about columns in the result of a query.

# EXAMPLE:

mycursor.execute("SELECT * FROM STUDENT")

print(mycursor.description)

# 15. SQL COMMANDS THROUGH PYTHON
# ------------------------------------------------------------

# CREATE DATABASE:
# mycursor.execute("CREATE DATABASE SCHOOL")

# SHOW DATABASES:
# mycursor.execute("SHOW DATABASES")

# CREATE TABLE:
# mycursor.execute("CREATE TABLE ...")

# SHOW TABLES:
# mycursor.execute("SHOW TABLES")

# INSERT:
# mycursor.execute("INSERT INTO ...")

# SELECT:
# mycursor.execute("SELECT ...")

# UPDATE:
# mycursor.execute("UPDATE ...")

# DELETE:
# mycursor.execute("DELETE ...")

# ALTER TABLE:
# mycursor.execute("ALTER TABLE ...")

# DROP TABLE:
# mycursor.execute("DROP TABLE ...")

# 16. CRUD OPERATIONS
# ------------------------------------------------------------

# C - CREATE (INSERT)
# R - READ (SELECT)
# U - UPDATE (UPDATE)
# D - DELETE (DELETE)

# These are the four basic operations performed on a database.

# 17. COMPLETE PYTHON-MYSQL PROGRAM
# ------------------------------------------------------------

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="school"
)

mycursor = mydb.cursor()

# INSERT

sql = "INSERT INTO STUDENT VALUES (%s, %s, %s)"

values = (4, "Karan", 91)

mycursor.execute(sql, values)

mydb.commit()

# DISPLAY

mycursor.execute("SELECT * FROM STUDENT")

records = mycursor.fetchall()

for row in records:
    print(row)

# UPDATE

sql = "UPDATE STUDENT SET MARKS = %s WHERE ROLLNO = %s"

mycursor.execute(sql, (95, 4))

mydb.commit()

# DELETE

sql = "DELETE FROM STUDENT WHERE ROLLNO = %s"

mycursor.execute(sql, (4,))

mydb.commit()

# CLOSE

mycursor.close()

mydb.close()

# 18. UNDERSTANDING SELECT QUERY OUTPUT
# ------------------------------------------------------------

# Suppose STUDENT contains:

# ROLLNO    NAME       MARKS
# 1         Aman       95
# 2         Rahul      88
# 3         Riya       92

# CODE:

mycursor.execute("SELECT * FROM STUDENT")

records = mycursor.fetchall()

print(type(records))
print(records)

# OUTPUT:

# <class 'list'>

# [(1, 'Aman', 95.0),
#  (2, 'Rahul', 88.0),
#  (3, 'Riya', 92.0)]

# IMPORTANT STRUCTURE:

# fetchall() returns a LIST OF TUPLES.

# Each tuple represents one row.

# Each element inside a tuple represents a column value.

# ACCESSING INDIVIDUAL VALUES:

records = mycursor.fetchall()

print(records[0])       # First record
print(records[0][0])    # Roll number
print(records[0][1])    # Name
print(records[0][2])    # Marks

# 19. USING CONDITIONS WITH SELECT
# ------------------------------------------------------------

# EXAMPLE 1:
# Find students scoring more than 90.

mycursor.execute(
    "SELECT * FROM STUDENT WHERE MARKS > 90"
)

records = mycursor.fetchall()

for row in records:
    print(row)

# EXAMPLE 2:
# Display students in descending order of marks.

mycursor.execute(
    "SELECT * FROM STUDENT ORDER BY MARKS DESC"
)

for row in mycursor.fetchall():
    print(row)

# EXAMPLE 3:
# Display only student names.

mycursor.execute("SELECT NAME FROM STUDENT")

for row in mycursor.fetchall():
    print(row[0])

# EXAMPLE 4:
# Count total students.

mycursor.execute("SELECT COUNT(*) FROM STUDENT")

result = mycursor.fetchone()

print("Total Students:", result[0])

# 20. USING PYTHON LOOPS WITH DATABASE RECORDS
# ------------------------------------------------------------

# EXAMPLE 1:
# Find students scoring above 90.

mycursor.execute("SELECT * FROM STUDENT")

records = mycursor.fetchall()

for row in records:

    if row[2] > 90:
        print(row)

# EXAMPLE 2:
# Calculate average marks.

mycursor.execute("SELECT MARKS FROM STUDENT")

records = mycursor.fetchall()

total = 0
count = 0

for row in records:
    total += row[0]
    count += 1

if count > 0:
    print("Average:", total / count)

# 21. EXCEPTION HANDLING IN DATABASE CONNECTIVITY
# ------------------------------------------------------------

# Exceptions can occur while connecting to MySQL or executing
# SQL statements.

# EXAMPLE:

import mysql.connector

try:

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="school"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM STUDENT")

    for row in mycursor.fetchall():
        print(row)

except mysql.connector.Error as err:

    print("Error:", err)

finally:

    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()

# IMPORTANT TERMS:

# try:
# Contains statements that may generate an exception.

# except:
# Handles the exception.

# finally:
# Executes whether an exception occurs or not.

# 22. DIFFERENCE BETWEEN IMPORTANT METHODS
# ------------------------------------------------------------

# connect()      : Establishes connection.
# cursor()       : Creates cursor object.
# execute()      : Executes a query.
# executemany()  : Executes query for multiple parameter sets.
# fetchone()     : Returns one record.
# fetchall()     : Returns all remaining records.
# fetchmany()    : Returns up to specified number of records.
# commit()       : Saves changes.
# rollback()     : Reverses uncommitted transactional changes.
# close()        : Closes connection or cursor.

# 23. IMPORTANT POINTS FOR CBSE BOARD EXAMS
# ------------------------------------------------------------

# 1. The module used for connectivity is mysql.connector.
# 2. connect() establishes the connection.
# 3. cursor() creates a cursor object.
# 4. execute() executes SQL queries.
# 5. executemany() executes queries for multiple sets of parameters.
# 6. fetchone() retrieves one record.
# 7. fetchall() retrieves all remaining records.
# 8. commit() saves database modifications.
# 9. close() closes the connection or cursor.
# 10. SELECT results are generally returned as tuples.
# 11. fetchall() returns a list of tuples.
# 12. %s is the placeholder used for parameterized queries.
# 13. A single-element tuple must have a trailing comma.
# 14. WHERE specifies the condition for UPDATE and DELETE.

# 24. COMMON ERRORS AND THEIR CORRECTIONS
# ------------------------------------------------------------

# INCORRECT: mydb.cursor
# CORRECT:   mydb.cursor()

# INCORRECT: mycursor.execute
# CORRECT:   mycursor.execute()

# INCORRECT: mydb.commit
# CORRECT:   mydb.commit()

# INCORRECT: mycursor.fetchall
# CORRECT:   mycursor.fetchall()

# INCORRECT: mycursor.execute(sql, 5)
# CORRECT:   mycursor.execute(sql, (5,))

# INCORRECT: mydb.close
# CORRECT:   mydb.close()

# IMPORTANT: SINGLE-ELEMENT TUPLE

# values = (5)

# This is an integer, NOT a tuple.

# CORRECT:

# values = (5,)

# ============================================================
#                     END OF NOTES
# ============================================================
