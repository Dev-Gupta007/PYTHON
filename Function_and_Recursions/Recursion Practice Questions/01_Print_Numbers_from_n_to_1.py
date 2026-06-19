n = int(input("Enter ther number till you want to print "))

def print_n_to_1(n):
    if n == 0:
        return 0
    print(n)
    print_n_to_1(n-1)

print_n_to_1(n)