def generate_parentheses(n):
    results = []

    def helper(string):
        if len(string) == 2*n:
            results.append(string)
            return
        if string.count("(") < n:
            helper(string + "(")
        if string.count(")") < string.count("("):
            helper(string + ")")

    helper("")
    return results


print(generate_parentheses(3))