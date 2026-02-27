import numpy as np

rng = np.random.default_rng()

array = np.array([1,2,3,4,5])
rng.shuffle(array)

print(array)

fruits = np.array(['apple','banana','pineapple','orange','guava'])
fruits_0 = rng.choice(fruits , size = (3,3))
rng.shuffle(fruits)
print(fruits_0)
print(fruits)