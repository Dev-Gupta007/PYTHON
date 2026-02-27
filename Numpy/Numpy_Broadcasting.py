import numpy as np

#Broadcasting allows Numpy to performoperations on arrays with different shapes by virtually
#expanding dimensions so they match the larger array.

#The dimensions have the same size.
#               OR
# One of the dimensions have the size of 1.

array_1 = np.array([[1, 2, 3, 4]])      # 1 row , 4 columns
array_2 = np.array([[1],[2],[3],[4]])   # 4 rows , 1 columns

print(array_1.shape)    #(1,4)  (Rows , Columns)
print(array_2.shape)    #(4,1)  One of them is 1 or they match  | vetically
print(array_1 * array_2)

