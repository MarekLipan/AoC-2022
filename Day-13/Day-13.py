import numpy as np

# read the input into a list
file = open('Day-13/input.txt', 'r')
L = file.read().splitlines()

right_order_indices = []

# 0... right order
# 1... not right order
# 2... same, need to continue


def compare(left: list, right: list) -> int:
    """
    Resurvise function to compare two lists
    """
    ll_len = len(left)
    rl_len = len(right)

    for i in range(min(ll_len, rl_len)):
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] < right[i]:
                return 0
            elif left[i] > right[i]:
                return 1
        elif isinstance(left[i], list) and isinstance(right[i], list):
            comparison_output = compare(left[i], right[i])
            if comparison_output==0 or comparison_output==1:
                return comparison_output
        elif isinstance(left[i], int) and isinstance(right[i], list):
            comparison_output = compare([left[i]], right[i])
            if comparison_output==0 or comparison_output==1:
                return comparison_output
        elif isinstance(left[i], list) and isinstance(right[i], int):
            comparison_output = compare(left[i], [right[i]])
            if comparison_output==0 or comparison_output==1:
                return comparison_output

    if ll_len < rl_len:
        return 0
    elif ll_len > rl_len:
        return 1

    return 2
    

for i in range(0, len(L), 3):

    index_of_pair = int(i/3)+1

    left = eval(L[i])
    right = eval(L[i+1])

    if compare(left, right) == 0:
        right_order_indices.append(index_of_pair)


print(f"result: {sum(right_order_indices)}")