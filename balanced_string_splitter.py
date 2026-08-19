def balanced_string_splits(s):
    
    running_balance = 0
    cut_count = 0

    for char in s:
        if char == "R":
            running_balance += 1
        elif char == "L":
            running_balance -= 1
        if running_balance == 0:
            cut_count += 1

    return cut_count

balanced_string_splits("RLRRLLRLRL")   # 4
# splits into: "RL", "RRLL", "RL", "RL"  -- each piece has equal L's and R's

balanced_string_splits("RLLLLRRRLR")   # 3
# splits into: "RL", "LLLRRR", "LR"

balanced_string_splits("LLLLRRRR")     # 1
# only the whole string works as one balanced piece

balanced_string_splits("RLRRRLLRLL")  # 2
