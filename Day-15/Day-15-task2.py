import numpy as np
import re
from tqdm import tqdm

# read the input into a list
file = open('Day-15/input.txt', 'r')
L = file.read().splitlines()

coords = []
for l in L:
    coords.append([int(n) for n in re.findall('[-+]?\d+', l)])

coords = np.array(coords)

# max positios of the search area
X = Y = 4000000

for y in tqdm(range(Y+1)):

    # the solution must be unique
    # invalid_interval_borders
    intervals = []
    for i in range(coords.shape[0]):
        distance = np.abs(coords[i, 0] - coords[i, 2]) + np.abs(coords[i, 1] - coords[i, 3])
        remaining_distance = distance - (np.abs(coords[i, 1] - y))
        if remaining_distance >= 0:
            left_border = coords[i, 0] - remaining_distance
            right_border = coords[i, 0] + remaining_distance
            intervals.append([left_border, right_border])

    # check if there is the solution present in this row
    candidate_x = [0, X]
    for i in intervals:
        candidate_x.append(i[1]+1)

    for x in candidate_x:
        solution_found = True

        if not(0 <= x <= X):
            solution_found = False

        if solution_found:
            for i in intervals:
                if i[0] <= x <= i[1]:
                    solution_found = False
                    break
        if solution_found == True:
            break
    if solution_found:
        break

print(x)
print(y)
print((x*4000000 + y))

    
