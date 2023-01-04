import numpy as np
import re

# read the input into a list
file = open('Day-14/input.txt', 'r')
L = file.read().splitlines()

# parse input
input = []
for l in L:
    input.append([int(n) for n in re.findall(r'\d+', l)])

paths = []
for i in input:
    for j in range(0, len(i)-2, 2):
        paths.append([i[j], i[j+1], i[j+2], i[j+3]])

paths = np.array(paths)

# initialize the field
x_min = 0
x_max = 1000

#x_min = np.min([np.min(paths[:, 0]), np.min(paths[:, 2])])
#x_max = np.max([np.max(paths[:, 0]), np.max(paths[:, 2])])
y_min = 0
y_max = np.max([np.max(paths[:, 1]), np.max(paths[:, 3])])

field = np.full(
    (y_max + 3, x_max - x_min + 1),
     "."
     )

# add floor for task 2
paths = np.vstack([paths, [x_min, y_max + 2, x_max, y_max + 2]])

# standardization
paths[:, 0] = paths[:, 0] - x_min
paths[:, 2] = paths[:, 2] - x_min

# order paths
x1 = np.min([paths[:, 0], paths[:, 2]], axis=0)
x2 = np.max([paths[:, 0], paths[:, 2]], axis=0)
y1 = np.min([paths[:, 1], paths[:, 3]], axis=0)
y2 = np.max([paths[:, 1], paths[:, 3]], axis=0)
paths = np.stack([x1, y1, x2, y2], axis=1)


# insert rock paths
for i in range(paths.shape[0]):
    field[paths[i, 1]:paths[i, 3]+1, paths[i, 0]:paths[i, 2]+1] = "#"


# fallin of the sand simulation
sand_placed = 0
no_fall = True
sp = [0, 500-x_min]

print(field[tuple(sp)])

while field[tuple([0, 500-x_min])] == ".":

    single_fall_in_progress = True
    sp = [0, 500-x_min]

    while single_fall_in_progress:
        if field[sp[0]+1, sp[1]] == ".":
            sp[0] += 1
        elif field[sp[0]+1, sp[1]-1] == ".":
            sp[0] += 1
            sp[1] -= 1
        elif field[sp[0]+1, sp[1]+1] == ".":
            sp[0] += 1
            sp[1] += 1
        # now it has to be already in place
        else: 
            single_fall_in_progress = False

    field[tuple(sp)] = "o"
    sand_placed += 1


print(f"Result task 2: {sand_placed}")

outpufile = open('Day-14/output.txt',"w")
output = []
for i in range(field.shape[0]):
    for j in range(field.shape[1]):
        output.append(field[i, j])
    output.append("\n")

outpufile.writelines(output)
outpufile.close()