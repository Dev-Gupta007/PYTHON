def LShift(Arr,n):
    L = len(Arr)
    for x in range(0,n):
        y = Arr[0]
        for i in range(0 , L-1):
            Arr[i] = Arr[i+1]
        Arr[L-1] = y
    print(Arr)

def RShift(Arr,n):
    L = len(Arr)
    for x in range(0 , n):
        y = Arr[L-1]
        for i in range(L-1 , 0 , -1):
            Arr[i] = Arr[i-1]
        Arr[0] = y
    print(Arr)

LShift([1,2,3,4,5,6,7,8,9,10] , 3)
RShift([1,2,3,4,5,6,7,8,9,10] , 3)