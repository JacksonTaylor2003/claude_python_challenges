def run_length_encode(s):
    new_s = ""

    if not s:
        return new_s

    current_char = s[0]
    count = 1

    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            new_s += (current_char + str(count))
            current_char = char
            count = 1
    new_s += (current_char + str(count))

    return(new_s)

run_length_encode("aaabbc")      # "a3b2c1"
run_length_encode("abcd")        # "a1b1c1d1"
run_length_encode("aaaaaaaaaa")  # "a10"
run_length_encode("")            # ""