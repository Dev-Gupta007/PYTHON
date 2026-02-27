Percentage = int(input("Enter the marks in Percentage: "))

if Percentage >= 90:
    print(f"Grade for {Percentage}% is A")
elif Percentage >= 80:
    print(f"Grade for {Percentage}% is B")
elif Percentage >= 70:
    print(f"Grade for {Percentage}% is C")
elif Percentage >= 60:
    print(f"Grade for {Percentage}% is D")
else:
    print(f"Grade for {Percentage}% is E")