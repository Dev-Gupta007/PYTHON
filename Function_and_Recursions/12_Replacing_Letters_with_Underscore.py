def Puzzle(w,n):
    length = len(w)
    for i in range(length):
        if i == 0:
            print(w[0] , end = "")
        elif (i+1) % n == 0:
            print('_' , end = "")
        else :
            print(w[i] , end = "")

Puzzle("TELEVISION" , 3)