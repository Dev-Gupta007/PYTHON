#Function Definition

def avg():
    a = int(input("Enter your Number : "))
    b = int(input("Enter your Number : "))
    c = int(input("Enter your Number : "))

    avg = (a+b+c)/3
    print(avg)
    return avg

#Function Call

avg()

a = avg()
print(a)