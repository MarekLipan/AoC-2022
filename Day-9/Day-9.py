import numpy as np
import re

# read the input into a list
file = open('Day-9/input.txt', 'r')
L = file.read().splitlines()

def positions_visited_by_tail(l: list, no_knots: int) -> int:
    """
    Number of positions in space visited by the tail.
    """

    # initial positions
    knot_positions = []
    for n in range(no_knots):
        knot_positions.append([0, 0])

    visited_positions = set()

    def move_tail(H_x, H_y, T_x, T_y):
        """
        Adjust position of the tail based on the (new) position of the head
        """
        # horizontal and vertical diffs
        h_diff = H_x - T_x
        v_diff = H_y - T_y

        # simple vertical or horizontal move
        if (h_diff == 0) or (v_diff == 0):
            T_x += int(h_diff/2)
            T_y += int(v_diff/2)
        # diagonal moves
        elif (abs(h_diff) == 2) and (abs(v_diff) == 2):
            T_x += int(h_diff/2)
            T_y += int(v_diff/2)
        elif abs(h_diff) == 2:
            T_x += int(h_diff/2)
            T_y += v_diff
        elif abs(v_diff) == 2:
            T_y += int(v_diff/2)
            T_x += h_diff

        return T_x, T_y

    for i in l:
        steps = int(re.findall(r'\d+', i)[0])
        direction = i[0]

        if direction == "U":
            for s in range(steps):
                knot_positions[0][1] += 1
                for n in range(1, no_knots):
                    knot_positions[n][0], knot_positions[n][1] = move_tail(knot_positions[n-1][0], knot_positions[n-1][1], knot_positions[n][0], knot_positions[n][1])
                visited_positions.add((knot_positions[-1][0], knot_positions[-1][1]))
        elif direction == "D":
            for s in range(steps):
                knot_positions[0][1] -= 1
                for n in range(1, no_knots):
                    knot_positions[n][0], knot_positions[n][1] = move_tail(knot_positions[n-1][0], knot_positions[n-1][1], knot_positions[n][0], knot_positions[n][1])
                visited_positions.add((knot_positions[-1][0], knot_positions[-1][1]))
        elif direction == "R":
            for s in range(steps):
                knot_positions[0][0] += 1
                for n in range(1, no_knots):
                    knot_positions[n][0], knot_positions[n][1] = move_tail(knot_positions[n-1][0], knot_positions[n-1][1], knot_positions[n][0], knot_positions[n][1])
                visited_positions.add((knot_positions[-1][0], knot_positions[-1][1]))
        elif direction == "L":
            for s in range(steps):
                knot_positions[0][0] -= 1
                for n in range(1, no_knots):
                    knot_positions[n][0], knot_positions[n][1] = move_tail(knot_positions[n-1][0], knot_positions[n-1][1], knot_positions[n][0], knot_positions[n][1])
                visited_positions.add((knot_positions[-1][0], knot_positions[-1][1]))

    # put together
    result = len(visited_positions)

    return result

print(positions_visited_by_tail(L, 10))

# 6026