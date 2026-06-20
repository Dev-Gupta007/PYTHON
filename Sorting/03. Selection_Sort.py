L = [30, 56, 23, 58, 34, 63, 98, 28 , 48 , 75]

def Selection_Sort(L):
    n = len(L)
    
    for i in range(n):
        index_min = i
        for j in range(i , n):
            if L[j] < L[index_min]:
                index_min = j 
        L[index_min] , L[i] = L[i] , L[index_min]
    return L

print("Sorted List" , Selection_Sort(L))
