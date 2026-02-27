n = int(input("Enter the number till you want to calculate the sum: "))

def sum_n_natural_numbers(n):
    if n == 1:
        return 1 
    return sum_n_natural_numbers(n-1)+n
    
print(f"{sum_n_natural_numbers(n)}")