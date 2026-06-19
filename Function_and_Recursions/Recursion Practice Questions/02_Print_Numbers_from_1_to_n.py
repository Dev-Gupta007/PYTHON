n = int(input("Enter the number till you want to print: "))

def print_1_to_n(n):
    if n == 0:
        return 
    print_1_to_n(n-1)
    print(n)

print_1_to_n(n)