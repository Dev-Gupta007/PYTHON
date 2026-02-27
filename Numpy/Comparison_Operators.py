import numpy as np

#Comparsion Operators

Scores = np.array([91, 58, 90, 100, 40, 63])

print(Scores == 100)    #Boolean Array # Who got a 100!
print(Scores >= 60)     # Who passed
print(Scores < 60)      # Who failed

Scores [Scores < 60 ] = 0   #Those Who failed get a zero 
print(Scores)