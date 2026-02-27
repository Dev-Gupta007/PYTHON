import numpy as np

# # Creating Arrays

# Array_1 = np.array([1, 2, 3, 4, 5])
# Array_2 = np.array([0, 0, 0, 0, 0])
# Array_3 = np.array([1, 1, 1, 1, 1])
# Array_4 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Array_1 = np.arange(1,6)        # np.arange(start, stop(exclusive), step)  
# Array_2 = np.zeros(5)
# Array_3 = np.ones(5)
# Array_4 = np.arange(10)

# print(Array_1)
# print(Array_2)
# print(Array_3)
# print(Array_4)

# #Matrix Problems

# Matrix_1 = np.arange(1, 13).reshape(3, 4)
# print(Matrix_1)

# Matrix_2 = np.arange(1, 17).reshape(4, 4)
# print(Matrix_2)
# print(Matrix_2[1:3 , 1:3])

# Matrix_3 = np.arange(1, 11)
# # Matrix_3[Matrix_3 % 2 == 0 ] = -1
# # print(Matrix_3)

# Matrix_3[Matrix_3 > 5] = 100
# print(Matrix_3)

# Matrix_4 = np.array([10, 20, 30, 40, 50])

# mean = np.mean(Matrix_4)
# std = np.std(Matrix_4)
# z = (Matrix_4 - mean)/std

# print(z)
# print(np.mean(z))
# print(np.std(z))

Matrix_5 = np.array([[10, 20, 30],
                     [40, 50, 60],
                     [70, 80, 90]])

mean = np.mean(Matrix_5, axis=0)
std = np.std(Matrix_5, axis=0)

z = (Matrix_5 - mean) / std

print(z)

