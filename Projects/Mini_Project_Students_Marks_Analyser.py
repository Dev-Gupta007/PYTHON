import numpy as np

# Marks of 5 students

# Student 1: [78, 85, 90]  
# Student 2: [88, 79, 92]  
# Student 3: [67, 70, 72]  
# Student 4: [90, 91, 89]  
# Student 5: [56, 65, 60]

# 1. Create the dataset
# Store the marks in a NumPy array
# Shape should be (5, 3)

print()
print("="*50)
print(" "*20 , "Dataset")
print("="*50)
print()

Dataset = np.array([
    [78, 85, 90] , 
    [88, 79, 92] , 
    [67, 70, 72] , 
    [90, 91, 89] , 
    [56, 65, 60]
])


print(Dataset)
print()
print("Shape" , np.shape(Dataset))

# 2. Basic Analysis
# Find:
# Average marks per student
# Average marks per subject
# Highest and lowest marks

print()
print("="*50)
print(" "*16 , "Basic Analysis")
print("="*50)
print()

Avg_Marks_per_Std = np.mean(Dataset , axis = 1)
Avg_Marks_per_Sub = np.mean(Dataset , axis = 0)

print("Avg Marks Per Student" , np.round(Avg_Marks_per_Std , 2))
print("Avg Marks Per Subject" , np.round(Avg_Marks_per_Sub , 2))

# 3. Top Performer
# Find which student has the highest total marks

print()
print("="*50)
print(" "*16 , "Top Performer")
print("="*50)
print()

Total_marks_per_std = np.sum(Dataset , axis = 1)

print(f"Highest Marks = {np.max(Total_marks_per_std)} Student 4 ")

# 4. Filtering
# Find students who scored more than 80 in all subjects

print()
print("="*50)
print("Students who scored more than 80 in all Subjects")
print("="*50)
print()

Consistent_Std = Dataset[np.all(Dataset > 80 , axis = 1)]

print(Consistent_Std)

# 5. Grade Assignment

# Convert marks to grades:

# A → ≥ 85
# B → 70–84
# C → < 70

print()
print("="*50)
print(" "*20 , "Grades")
print("="*50)
print()

grades = np.where(Dataset >= 85, 'A', 
         np.where(Dataset >= 70, 'B', 'C'))     # np.where(condition, value_if_true, value_if_false)

print(grades)

# 6. Garce Marks

print()
print("="*50)
print(" "*10 , "Marks after adding Grace Marks")
print("="*50)
print()

updated_marks = np.clip(Dataset + 5, 0, 100)        # np.clip(array, min_value, max_value)
print(updated_marks)

