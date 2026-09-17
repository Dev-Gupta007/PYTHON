import csv
f = open("Pokemon.csv" , "r")

### 1. `csv.reader()` returns an iterator

csv_reader = csv.reader(f)

# `csv_reader` is a **CSV reader object / iterator**, not a list.
# It produces one row at a time.

for line in csv_reader:
    print(line)

# Here, `line` is a **list** containing the values of that row.

# csv_reader → iterator
# line       → list
# line[0]    → first column
# line[1]    → second column

### 2. Reader iterator gets exhausted

# Once:

for line in csv_reader:
    break
# has gone through the entire file, the reader reaches **EOF (End Of File)**.

# Trying to iterate over the same reader again gives nothing.

# To read from the beginning again:

f.seek(0)

csv_reader = csv.reader(f)

# `f.seek(0)` moves the **file pointer** back to the beginning.

# However, it does **not reset the already-consumed reader iterator**, so a new `csv_reader` should be created.

# --------------------------------------------------------------------------

### 2.5 `next(csv_reader)`

# `next()` is used to get the next row from the CSV reader iterator.

line = next(csv_reader)
print(line)

# If the CSV is:
# Name,Type,HP
# Pikachu,Electric,35
# Bulbasaur,Grass,45

# Then:

line = next(csv_reader)

# gives:
# ['Name', 'Type', 'HP']

# Calling it again:

line = next(csv_reader)

# gives:
# ['Pikachu', 'Electric', '35']

# So every `next(csv_reader)` moves the iterator forward by one row.

### Getting the 5th row

# Since `csv_reader` is an iterator, you cannot directly do:

csv_reader[4]       # ❌

# You can use `next()` repeatedly:

for i in range(5):
    line = next(csv_reader)

print(line)

# After 5 calls to `next()`, `line` contains the 5th row.

### `next()` and EOF

# If there are no more rows and you call:

next(csv_reader)

# Python raises:

# StopIteration

# This happens because the iterator has reached the end of the file.

### Easy way to remember

# next(csv_reader)
#        ↓
# gets the next row
#        ↓
# moves iterator forward

# `next()` works with the iterator,
# while `line` is the list produced by the iterator.

# ---------------------------------------------------------------------------

### 2.6 Going over / Skipping the Header

# In a CSV file, the first row is usually the header.

# Example:
# Name,Type,HP
# Pikachu,Electric,35
# Bulbasaur,Grass,45

# When using csv.reader(), the header is treated just like any other row.

csv_reader = csv.reader(f)

for line in csv_reader:
    print(line)

# Output:
# ['Name', 'Type', 'HP']              ← Header
# ['Pikachu', 'Electric', '35']
# ['Bulbasaur', 'Grass', '45']


# If you don't want to process the header, use next() once before the loop:

csv_reader = csv.reader(f)

next(csv_reader)        # Skips the header

for line in csv_reader:
    print(line)

# Now the loop starts from:
# ['Pikachu', 'Electric', '35']

# `next(csv_reader)` moves the iterator forward by ONE row.
# Therefore, calling it once before the loop skips the first row (header).

# This is especially useful when you only want to process the actual data.

### Header + `next()` together

# You can also store the header instead of simply skipping it:

csv_reader = csv.reader(f)

header = next(csv_reader)

print(header)

for line in csv_reader:
    print(line)

# header → ['Name', 'Type', 'HP']
# line   → each data row


### Important

# csv.reader() does NOT automatically identify or skip the header.

# It treats:
# Header → first row
# Data   → remaining rows

# To skip the header:
next(csv_reader)

# To save the header:
header = next(csv_reader)

#----------------------------------------------------------------------------

### 3. `csv.writer()`

new_file = open("new.csv" , 'w+')

csv_writer = csv.writer(new_file)

# Creates a **CSV writer object**.

# It is used to write rows into a CSV file.

csv_writer.writerow(line)

# `writerow()` writes **one row** and takes a list-like object.

# Example:

csv_writer.writerow(["A", "B", "C"])

# ---------------------------------------------------------------------------

### 4. `delimiter`

# A delimiter specifies what separates the values in a CSV file.

# Default: delimiter = ','

csv_writer = csv.writer(new_file, delimiter="_")

csv_writer.writerow(["A", "B", "C"])

# produces:

# A_B_C

# When reading the same file, use the same delimiter:

csv_reader = csv.reader(new_file, delimiter="_")

# ------------------------------------------------------------------

### 5. `newline=""`

# When opening a CSV file for writing, use:

new_file = open("new_csv", "w", newline="")

# This prevents unwanted blank lines / newline-related issues, particularly on Windows.

# Similarly, it can be used while reading:

file = open("new_csv", "r", newline="")

# ---------------------------------------------------------------------------------

### 6. `csv.DictReader()`

csv_reader = csv.DictReader(file)

# `DictReader` returns a **reader object / iterator**.
# Each row produced by the iterator is a **dictionary** instead of a list.

# If the CSV contains:

# Name,Type,HP
# Pikachu,Electric,35

# then:

for line in csv_reader:
    print(line)

# gives approximately:

# {
#     "Name": "Pikachu",
#     "Type": "Electric",
#     "HP": "35"
# }

# The first row (header) is automatically used as the **dictionary keys**.

# Therefore, instead of accessing a column using its index:

line[1]

# you can access it using its column name:

line["Type"]

# `DictReader` handles the header automatically.
# You do NOT need to use next(csv_reader) to skip the header.


### `reader` vs `DictReader`

# csv.reader()
#     ↓
# iterator
#     ↓
# each row → list
#     ↓
# line[0], line[1], ...

# csv.DictReader()
#      ↓
# iterator
#      ↓
# each row → dictionary
#      ↓
# line["Name"], line["Type"], ...


### Important distinction

# csv_reader = csv.reader(file)
# → csv_reader is an iterator
# → each row is a list

# csv_reader = csv.DictReader(file)
# → csv_reader is also an iterator
# → each row is a dictionary

# --------------------------------------------------------------

### 6. `csv.DictReader()`

csv_reader = csv.DictReader(file)

# `DictReader` returns a **reader object / iterator**.
# Each row produced by the iterator is a **dictionary** instead of a list.

# If the CSV contains:

# Name,Type,HP
# Pikachu,Electric,35

# then:

for line in csv_reader:
    print(line)

# gives approximately:

# {
#     "Name": "Pikachu",
#     "Type": "Electric",
#     "HP": "35"
# }

# The first row (header) is automatically used as the **dictionary keys**.

# Therefore, instead of accessing a column using its index:

line[1]

# you can access it using its column name:

line["Type"]

# `DictReader` handles the header automatically.
# You do NOT need to use next(csv_reader) to skip the header.


### `reader` vs `DictReader`

# csv.reader()
#     ↓
# iterator
#     ↓
# each row → list
#     ↓
# line[0], line[1], ...

# csv.DictReader()
#      ↓
# iterator
#      ↓
# each row → dictionary
#      ↓
# line["Name"], line["Type"], ...


### Important distinction

# csv_reader = csv.reader(file)
# → csv_reader is an iterator
# → each row is a list

# csv_reader = csv.DictReader(file)
# → csv_reader is also an iterator
# → each row is a dictionary

### Important distinction

csv_reader = csv.reader(file)

#→ `csv_reader` is an **iterator**

for line in csv_reader:
    break
# → `line` is a **list**

csv_reader = csv.DictReader(file)

# → `csv_reader` is also an **iterator**

for line in csv_reader:
    break
# → `line` is a **dictionary**

# Summary

# ============================================================
#                    CSV FILE COMMANDS
# ============================================================

import csv


# ------------------------------------------------------------
# 1. OPENING A CSV FILE
# ------------------------------------------------------------

# Reading:
f = open("data.csv", "r")

# Writing:
f = open("data.csv", "w", newline="")

# Appending:
f = open("data.csv", "a", newline="")


# Common modes:

# "r"  -> Read
# "w"  -> Write
# "a"  -> Append


# ------------------------------------------------------------
# 2. csv.reader()
# ------------------------------------------------------------

# Creates a CSV reader object.

csv_reader = csv.reader(f)


# Example:

f = open("data.csv", "r")

csv_reader = csv.reader(f)

for row in csv_reader:
    print(row)

f.close()


# Each row is returned as a LIST.

# Example row:
# ['Aman', '85', '90', '78']


# ------------------------------------------------------------
# 3. ACCESSING COLUMNS
# ------------------------------------------------------------

for row in csv_reader:
    print(row[0])       # First column
    print(row[1])       # Second column


# Indexing starts from 0.


# ------------------------------------------------------------
# 4. SKIPPING HEADER
# ------------------------------------------------------------

csv_reader = csv.reader(f)

header = next(csv_reader)

for row in csv_reader:
    print(row)


# next() reads the next row and moves the iterator forward.


# ------------------------------------------------------------
# 5. next()
# ------------------------------------------------------------

row = next(csv_reader)


# Reads ONE row from the CSV reader.

# If no rows are left:
# StopIteration occurs.


# ------------------------------------------------------------
# 6. csv.writer()
# ------------------------------------------------------------

# Creates a CSV writer object.

writer = csv.writer(f)


# ------------------------------------------------------------
# 7. writerow()
# ------------------------------------------------------------

# Writes ONE row.

writer.writerow(["Aman", 90, 85, 88])


# Syntax:
# writer.writerow(list)


# ------------------------------------------------------------
# 8. writerows()
# ------------------------------------------------------------

# Writes MULTIPLE rows.

data = [
    ["Aman", 90, 85],
    ["Riya", 95, 92],
    ["Karan", 87, 89]
]

writer.writerows(data)


# Syntax:
# writer.writerows(list_of_rows)


# ------------------------------------------------------------
# 9. delimiter
# ------------------------------------------------------------

# Default delimiter is comma (,).

csv_reader = csv.reader(f, delimiter=",")


# A different separator can be specified:

csv_reader = csv.reader(f, delimiter="_")


# Example:
# Aman_90_85_88


# ------------------------------------------------------------
# 10. newline=""
# ------------------------------------------------------------

# Recommended while writing CSV files:

f = open("data.csv", "w", newline="")

writer = csv.writer(f)


# Helps avoid unwanted blank lines,
# especially on Windows.


# ------------------------------------------------------------
# 11. SEARCHING A CSV FILE
# ------------------------------------------------------------

f = open("student.csv", "r")

csv_reader = csv.reader(f)

for row in csv_reader:

    if row[0] == "Aman":
        print(row)

f.close()


# ------------------------------------------------------------
# 12. COUNTING RECORDS
# ------------------------------------------------------------

f = open("student.csv", "r")

csv_reader = csv.reader(f)

count = 0

for row in csv_reader:
    count += 1

print("Number of records =", count)

f.close()


# ------------------------------------------------------------
# 13. READING A CSV FILE INTO A LIST
# ------------------------------------------------------------

f = open("data.csv", "r")

csv_reader = csv.reader(f)

data = list(csv_reader)

print(data)

f.close()


# IMPORTANT:
# csv.reader(f) itself is NOT a list.
# It is a reader/iterator object.


# ------------------------------------------------------------
# 14. seek() WITH CSV
# ------------------------------------------------------------

f = open("data.csv", "r")

csv_reader = csv.reader(f)

# Read some rows...

f.seek(0)

# Re-create the reader after seeking:
csv_reader = csv.reader(f)


# ------------------------------------------------------------
# 15. IMPORTANT CSV COMMANDS AT A GLANCE
# ------------------------------------------------------------

# import csv
# -> Import CSV module

# open("data.csv", "r")
# -> Open CSV for reading

# open("data.csv", "w", newline="")
# -> Open CSV for writing

# open("data.csv", "a", newline="")
# -> Open CSV for appending

# csv.reader(file)
# -> Create CSV reader object

# next(csv_reader)
# -> Read one row and move forward

# csv.writer(file)
# -> Create CSV writer object

# writer.writerow(row)
# -> Write one row

# writer.writerows(rows)
# -> Write multiple rows

# file.seek(0)
# -> Move file pointer to beginning

# delimiter=","
# -> Specify separator


# ============================================================
#              TEXT vs BINARY vs CSV
# ============================================================

# TEXT FILE
#
# open("data.txt", "r")
# read()
# readline()
# readlines()
# write()
# writelines()


# BINARY FILE
#
# import pickle
# open("data.dat", "rb")
# open("data.dat", "wb")
# open("data.dat", "ab")
# pickle.dump()
# pickle.load()
# seek()
# tell()
# EOFError


# CSV FILE
#
# import csv
# open("data.csv", "r")
# open("data.csv", "w", newline="")
# open("data.csv", "a", newline="")
# csv.reader()
# csv.writer()
# next()
# writerow()
# writerows()
# seek()
# delimiter