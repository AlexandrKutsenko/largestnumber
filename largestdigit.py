num = int(input("Enter a natural number less than 1,000,000,000: "))
if num < 0 or num >= 1000000000:
    print("Input error")
else:
    max_digit = -1
    while num > 0:
        digit = num % 10
        if digit > max_digit:
            max_digit = digit
        num //= 10
    print("Largest digit:", max_digit)
