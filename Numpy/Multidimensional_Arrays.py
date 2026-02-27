import numpy as np

array = np.array("A")

print(array.ndim)

array_1 = np.array(['a','b','c']) 

print(array_1.ndim)

array_2 = np.array([['A','B','C'] , #Matrix(Rows and Colums )
                    ['D','E','F'] ,
                    ['G','H','I']])

print(array_2.ndim)

array_3 = np.array([[['A','B','C'] , ['D','E','F'] ,['G','H','I']],     #layer 0
                    [['J','K','L'] , ['M','N','O'] ,['P','Q','R']],     #layer 1
                    [['S','T','U'] , ['V','W','X'] ,['Y','Z','_']]])    #layer 2

print(array_3.ndim)
print(array_3.shape)

print(array_3[0][0][0]) #Chain Indexing

print(array_3[0,0,0]) #Multidimentional Indexing

word = array_3[0, 0, 0] + array_3[1, 1, 1] + array_3[0, 1, 0]

print(word)

word_2 = array_3[0,2,1] + array_3[0,2,2]

print(word_2)