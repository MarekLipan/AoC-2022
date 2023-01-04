import numpy as np
import functools

# read the input into a list
file = open('Day-13/input.txt', 'r')
L = file.read().splitlines()

right_order_indices = []

# -1... right order
# 1... not right order
# 0... same, need to continue


def compare(left: list, right: list) -> int:
    """
    Recursive function to compare two lists
    """
    ll_len = len(left)
    rl_len = len(right)

    for i in range(min(ll_len, rl_len)):
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] < right[i]:
                return -1
            elif left[i] > right[i]:
                return 1
        elif isinstance(left[i], list) and isinstance(right[i], list):
            comparison_output = compare(left[i], right[i])
            if comparison_output==-1 or comparison_output==1:
                return comparison_output
        elif isinstance(left[i], int) and isinstance(right[i], list):
            comparison_output = compare([left[i]], right[i])
            if comparison_output==-1 or comparison_output==1:
                return comparison_output
        elif isinstance(left[i], list) and isinstance(right[i], int):
            comparison_output = compare(left[i], [right[i]])
            if comparison_output==-1 or comparison_output==1:
                return comparison_output

    if ll_len < rl_len:
        return -1
    elif ll_len > rl_len:
        return 1

    return 0
    

for i in range(0, len(L), 3):

    index_of_pair = int(i/3)+1

    left = eval(L[i])
    right = eval(L[i+1])

    if compare(left, right) == -1:
        right_order_indices.append(index_of_pair)

print(f"part 1 result: {sum(right_order_indices)}")


### PART 2
all_packets = [[[2]], [[6]]]
for i in range(0, len(L), 3):
    all_packets.append(eval(L[i]))
    all_packets.append(eval(L[i+1]))

all_packets_sorted = sorted(all_packets, key=functools.cmp_to_key(compare))

print(f"part 2 result: {(all_packets_sorted.index([[2]]) + 1) * (all_packets_sorted.index([[6]]) + 1)}")