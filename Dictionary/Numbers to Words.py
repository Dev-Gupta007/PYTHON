def number_to_words(n):
    ones = ["Zero", "One", "Two", "Three", "Four",
            "Five", "Six", "Seven", "Eight", "Nine"]
    
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
             "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    
    tens = ["", "", "Twenty", "Thirty", "Forty",
            "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    if n < 10:
        return ones[n]
    
    elif n < 20:
        return teens[n - 10]
    
    elif n < 100:
        return tens[n // 10] + ("" if n % 10 == 0 else " " + ones[n % 10])
    
    elif n < 1000:
        return ones[n // 100] + " Hundred" + (
            "" if n % 100 == 0 else " " + number_to_words(n % 100)
        )
    
    else:
        return "Number too large"
    
print(number_to_words(101))