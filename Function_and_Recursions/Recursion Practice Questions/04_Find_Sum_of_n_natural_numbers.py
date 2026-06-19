n = int(input("Enter The Number till you want the sum: "))

def n_sum(n):
    if n < 0:
        raise ValueError("n must not be negetive ")
    if n == 0:
        return 0 
    return n+n_sum(n-1)

print(n_sum(n))