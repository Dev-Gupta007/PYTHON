import numpy as np 

rng = np.random.default_rng(seed = 1)   #Setting a seed makes it return the same results

print(rng.integers(1 , 101 , size = (3,2)))    #(inclusive , exclusive), size = (rows = 3 , columns = 2)


print(np.random.uniform(low = -1 , high = 1 , size = 3))
print(np.random.uniform(low = -1 , high = 1 , size = (3,2)))