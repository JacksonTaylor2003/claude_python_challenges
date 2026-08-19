def count_digits(n):
    if n < 10:
        return 1

    return count_digits(n // 10) + 1


print(count_digits(12345))   # 5
count_digits(7)       # 1
print(count_digits(100))     # 3
count_digits(0)       # 1