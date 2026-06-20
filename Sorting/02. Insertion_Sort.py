L = [33, 14, 39, 6, 11, 29, 1, 56, 75, 23]

def Insertion_Sort(L):
    n = len(L)
    temp = 0

    for i in range(1 , n):
        temp = L[i]
        for j in range(i , -1 , -1):
            if temp < L[j]:
                L[j] , L[j+1] = L[j+1] , L[j]
    return L
print("Sorted List" , Insertion_Sort(L))