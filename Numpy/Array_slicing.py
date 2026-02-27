import numpy as np

# Columns          0 , 1, 2 , 3 

array = np.array([['1','2','3','4'],        # row 0 , -4
                  ['5','6','7','8'],        # row 1 , -3
                  ['9','10','11','12'],     # row 2 , -2
                  ['13','14','15','16']])   # row 3 , -1

#array[start:end(exclusive):step]
#[rows              : columns ]
#[start:end:step    , start:end:end]
# Rows selection

print(array[0])
print(array[0:3])
print(array[1:4])
print(array[0:4:2])
print(array[::2])
print(array[::-1])
print(array[::-2])

#Column Selection

print(array[0,0])
print(array[ :, 0])
print(array[ :, -1])
print(array[ :, -2])
print(array[ :, 0:3])
print(array[ :, 1:4])
print(array[ :, 0: ])
print(array[ :, ::2]) #21:00  https://www.youtube.com/watch?v=VXU4LSAQDSc
print(array[ :, 1::2])
print(array[ :, ::-1])
print(array[ :, ::-2])

# Row and Column Selection

print(array[0:2,0:2])  
print(array[0:2,2:4])   #print(array[0:2,2:])
print(array[2:4,0:2])   #print(array[2:,0:2])
print(array[2:4,2:4])   #print(array[2:,2:])

