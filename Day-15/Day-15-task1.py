import numpy as np
import re

# read the input into a list
file = open('Day-15/input.txt', 'r')
L = file.read().splitlines()

coords = []
for l in L:
    coords.append([int(n) for n in re.findall('[-+]?\d+', l)])

coords = np.array(coords)

result_positions = set()

# query line index
Q = 2000000


for i in range(coords.shape[0]):
    distance = np.abs(coords[i, 0] - coords[i, 2]) + np.abs(coords[i, 1] - coords[i, 3])
    # can it even reach to line Q
    remaining_distance = distance - (np.abs(coords[i, 1] - Q))
    if remaining_distance >= 0:
        result_positions.add(coords[i, 0])
        for j in range(remaining_distance):
            result_positions.add(coords[i, 0] - (j+1))
            result_positions.add(coords[i, 0] + (j+1))


# remove sensors and beacons positions
for i in range(coords.shape[0]):
    if coords[i, 1] == Q:
        result_positions.discard(coords[i, 0])
    if coords[i, 3] == Q:
        result_positions.discard(coords[i, 2])

print(f"Task 1 result: {len(result_positions)}")

