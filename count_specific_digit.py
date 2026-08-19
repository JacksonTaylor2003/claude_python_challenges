def count_digit_occurrences(n, digit):
    if n < 10:
        if n % 10 == digit:
            return 1
        else:
            return 0

    last_digit = n % 10
    rest_digits = count_digit_occurrences(n // 10, digit)

    if last_digit == digit:
        return rest_digits + 1
    else:
        return rest_digits


print(count_digit_occurrences(122345, 2))   # 2   (two 2's)
print(count_digit_occurrences(555, 5))      # 3
print(count_digit_occurrences(12345, 9))    # 0
print(count_digit_occurrences(7, 7))        # 1