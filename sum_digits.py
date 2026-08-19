def sum_digits(n):
    if n < 10:
        return n
    
    last_digit = n % 10
    rest_of_number = n // 10

    return last_digit + sum_digits(rest_of_number)




print(sum_digits(1234))