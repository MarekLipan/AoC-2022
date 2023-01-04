import re
from copy import copy

# read the input into a list
file = open('Day-22/input.txt', 'r')
L = file.read().splitlines()

J = 0
for l in L[:-2]:
    J = max(J, len(l))

map = []
for l in L[:-2]:
    map.append([i for i in (l + (J - len(l)) * " ")])

instr = L[-1]

instr_steps = [int(n) for n in re.findall('[-+]?\d+', instr)]
instr_dir = [c for c in re.findall('[A-Z]', instr)]


# find starting position and direction
j = 0
while map[0][j] != ".":
    j+=1

pos = [0, j]
dir = 0


def find_next_pos(pos: list, dir: int) -> list:
    """
    Given position and direction, find what is the next position to be stepped on
    """

    #right
    if dir == 0:
        if (pos[1] + 1) < J and map[pos[0]][pos[1]+1] != " ":
            next_pos = [pos[0], pos[1]+1]
        else:
            next_pos = copy(pos)
            while ((next_pos[1] - 1) >= 0) and map[next_pos[0]][next_pos[1]-1] != " ":
                next_pos[1] -= 1
    # down
    elif dir == 1:
        if (pos[0] + 1) < len(map) and map[pos[0]+1][pos[1]] != " ":
            next_pos = [pos[0]+1, pos[1]]
        else:
            next_pos = copy(pos)
            while ((next_pos[0] - 1) >= 0) and map[next_pos[0]-1][next_pos[1]] != " ":
                next_pos[0] -= 1
    #left
    if dir == 2:
        if ((pos[1] - 1) >= 0) and map[pos[0]][pos[1]-1] != " ":
            next_pos = [pos[0], pos[1]-1]
        else:
            next_pos = copy(pos)
            while (next_pos[1] + 1) < J and map[next_pos[0]][next_pos[1]+1] != " ":
                next_pos[1] += 1
    # up
    elif dir == 3:
        if ((pos[0] - 1) >= 0) and map[pos[0]-1][pos[1]] != " ":
            next_pos = [pos[0]-1, pos[1]]
        else:
            next_pos = copy(pos)
            while (next_pos[0] + 1) < len(map) and map[next_pos[0]+1][next_pos[1]] != " ":
                next_pos[0] += 1

    return next_pos


def move(pos: list, dir: int, steps: int) -> list:
    """
    Takes initial position, direction and number of steps as input and return final position
    """

    next_pos = find_next_pos(pos, dir)

    while map[next_pos[0]][next_pos[1]] == "." and steps > 0:
        pos = next_pos
        steps -= 1
        next_pos = find_next_pos(pos, dir)

    return pos


def draw_map():

    outpufile = open('Day-22/map.txt',"w")
    output = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if i==pos[0] and j==pos[1]:
                if dir == 0:
                    output.append(">")
                elif dir == 1:
                    output.append("v")
                elif dir == 2:
                    output.append("<")
                elif dir == 3:
                    output.append("^")
            else:
                output.append(map[i][j])
        output.append("\n")

    outpufile.writelines(output)
    outpufile.close()

# first move
pos = move(pos, dir, instr_steps[0])
draw_map()

# all remaining moves
for i in range(len(instr_dir)):
    if instr_dir[i] == "R":
        dir = (dir + 1) % 4
    else:
        dir = (dir - 1) % 4

    #print(f"dir: {dir}")
    #print(f"steps: {instr_steps[i+1]}")
    #print(f"start: {pos}")

    pos = move(pos, dir, instr_steps[i+1])

    #print(f"end: {pos}")

    #draw_map()

result = (
    (1000*(pos[0]+1)) +
    (4*(pos[1]+1)) +
    (dir)
)
print(f"Task 1 result: {result}")


#dir: 1
#steps: 40
#start: [146, 55]
#end: [2, 55]

#dir: 2
#steps: 33
#start: [2, 55]
#end: [2, 149]