L = [10, 56, 23, 58, 34, 63, 98, 28 , 48 , 75]

def Bubble_Sort(L):

    n = len(L)

    for i in range(n , 0 , -1) :
        for j in range(0 , i-1):
            if L[j] > L[j+1]:
                L[j] , L[j+1] = L[j+1] , L[j]
            else:
                continue
    return(L)

print("Sorted List" , Bubble_Sort(L))