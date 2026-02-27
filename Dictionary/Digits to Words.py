# 876 ---> 'Eight Seven Six'

D = {
    0: 'Zero',
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine'
}

Num = int(input("Enter the Number: "))
Word_List = []

Copy = Num

# Special case if number is 0
if Num == 0:
    print(D[0])
else:
    while Copy > 0:
        Digit = Copy % 10
        Copy = Copy // 10
        Word_List.append(D[Digit])

    Word_List.reverse()
    Word = " ".join(Word_List)

    print(Word) 