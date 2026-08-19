def is_valid_parentheses(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if not stack or stack.pop() != pairs[char]:
                return False

    if stack:
        return False
    
    return True

print(is_valid_parentheses("()"))        # True
print(is_valid_parentheses("()[]{}"))    # True
print(is_valid_parentheses("(]"))        # False
print(is_valid_parentheses("([)]"))      # False  <- wrong order!
print(is_valid_parentheses("{[]}"))      # True   <- nested correctly
print(is_valid_parentheses("("))         # False  <- unclosed