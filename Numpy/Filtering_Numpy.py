import numpy as np
Ages = np.array([[1,2,3,4,5,6,7,8,9,10],
                  [11,12,13,14,15,16,17,18,19,20]])

Greater_Than_10 = Ages[Ages >= 10]
Between_10_15 = Ages[(Ages >= 10) & (Ages <= 15)]                # & ----> And
Lessthan_5_or_greater_than_15 = Ages[(Ages <= 5) | (Ages >= 15)]  # | -----> OR
Even = Ages[Ages % 2 == 0]
Odd = Ages[Ages % 2 != 0]


print(Greater_Than_10)
print(Between_10_15)
print(Lessthan_5_or_greater_than_15)
print(Even)
print(Odd)

# WHERE FUNCTION

A = np.where(Ages < 15 , Ages , 0)
print(A)