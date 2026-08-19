def power(base, exponent):
    if exponent == 0:
        return 1

    previous = power(base, exponent - 1)

    return base * previous
    

    

print(power(2, 3))    # 8   (2*2*2)
print(power(5, 0))    # 1   (anything to the power of 0 is 1)
print(power(3, 1))    # 3