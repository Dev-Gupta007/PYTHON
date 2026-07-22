marks = {
    "Aman": 85,
    "Rahul": 91,
    "Neha": 88,
    "Riya": 95
}

highest = 0

for i in marks.keys():
    if marks[i] > highest:
        highest = marks[i]
        index = i

print("Highest Marks:" , index , highest)