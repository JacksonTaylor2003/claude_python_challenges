def generate_binary_strings(n):
    results = []

    def helper(string):
        if len(string) == n:
            results.append(string)
            return
        helper(string + "0")
        helper(string + "1")

    helper("")
    return results



print(generate_binary_strings(1))
# ["0", "1"]
print(generate_binary_strings(2))
# ["00", "01", "10", "11"]
        