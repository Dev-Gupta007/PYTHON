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