def float_to_fixed_point_binary(n, places=10):
    """ Convert float to a fixed-point binary string with a limited number of fractional places. """
    if n < 0:
        sign = "-"
        n = abs(n)
    else:
        sign = ""

    # Convert integer part to binary
    integer_part = int(n)
    fractional_part = n - integer_part
    binary_int = bin(integer_part)[2:] # Remove the '0b' prefix

    # Convert fractional part to binary
    binary_frac = ""
    for _ in range(places):
        fractional_part *= 2
        if fractional_part >= 1:
            binary_frac += '1'
            fractional_part -= 1
        else:
            binary_frac += '0'
        if fractional_part == 0: # Stop if the fraction becomes exactly zero
            break
            
    if binary_frac:
        return f"{sign}{binary_int}.{binary_frac}"
    else:
        return f"{sign}{binary_int}"

# Example usage:
number = 1000.25
print(f"The fixed-point binary of {number} is: {float_to_fixed_point_binary(number)}")

number_approx = 0.1
print(f"The fixed-point binary of {number_approx} is: {float_to_fixed_point_binary(number_approx, places=20)}")