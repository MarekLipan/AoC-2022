import re

# read the input into a list
file = open('Day-22/sample_input.txt', 'r')
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

def cube_side_cross(pos: list, dir: str) -> tuple:
    """
    Find new position and direction
    """

    i, j = pos

    if dir==0:
        if (0 <= i <= 3) and (j == 11):
            next_dir = 2
            pos = [11-i, 15]
        elif (4 <= i <= 7) and (j == 11):
            next_dir = 1
            pos = [8, 19-i]
        elif (8 <= i <= 11) and (j == 15):
            next_dir = 2
            pos = [11-i, 11]
    elif dir==1:  
        if (i==7) and (0 <= j <= 3):
            next_dir = 3
            pos = [11, 11-j]
        elif (i==7) and (4 <= j <= 7):
            next_dir = 0
            pos = [15-j, 8]
        elif (i==11) and (8 <= j <= 11):
            next_dir = 3
            pos = [7, 11-j]
        elif (i==11) and (12 <= j <= 15):
            next_dir = 0
            pos = [19-j, 0] 
    elif dir==2:   
        if (0 <= i <= 3) and (j == 8):
            next_dir = 1
            pos = [4, i + 4]
        elif (4 <= i <= 7) and (j == 0):
            next_dir = 3
            pos = [11, 19-i]
        elif (8 <= i <= 11) and (j == 8):
            next_dir = 3
            pos = [7, 19-i] 
    elif dir==3:   
        if (i == 4) and (0 <= j <= 3):
            next_dir = 1
            pos = [0, 11-j]
        elif (i == 4) and (4 <= j <= 7):
            next_dir = 0
            pos = [j-4, 8]
        elif (i == 0) and (8 <= j <= 11):
            next_dir = 1
            pos = [4, 11-j]
        elif (i == 8) and (12 <= j <= 15):
            next_dir = 2
            pos = [19-j, 11]      

    return pos, next_dir



def find_next_pos(pos: list, dir: int) -> tuple:
    """
    Given position and direction, find what is the next position to be stepped on and new direction
    """

    #right
    if dir == 0:
        if (pos[1] + 1) < J and map[pos[0]][pos[1]+1] != " ":
            next_pos = [pos[0], pos[1]+1]
            next_dir = dir
        else:
            next_pos, next_dir = cube_side_cross(pos, dir)
    # down
    elif dir == 1:
        if (pos[0] + 1) < len(map) and map[pos[0]+1][pos[1]] != " ":
            next_pos = [pos[0]+1, pos[1]]
            next_dir = dir
        else:
            next_pos, next_dir = cube_side_cross(pos, dir)
    #left
    elif dir == 2:
        if ((pos[1] - 1) >= 0) and map[pos[0]][pos[1]-1] != " ":
            next_pos = [pos[0], pos[1]-1]
            next_dir = dir
        else:
            next_pos, next_dir = cube_side_cross(pos, dir)
    # up
    elif dir == 3:
        if ((pos[0] - 1) >= 0) and map[pos[0]-1][pos[1]] != " ":
            next_pos = [pos[0]-1, pos[1]]
            next_dir = dir
        else:
            next_pos, next_dir = cube_side_cross(pos, dir)

    return next_pos, next_dir


def move(pos: list, dir: int, steps: int) -> tuple:
    """
    Takes initial position, direction and number of steps as input and return final position
    """

    next_pos, next_dir = find_next_pos(pos, dir)

    while map[next_pos[0]][next_pos[1]] == "." and steps > 0:
        pos = next_pos
        dir = next_dir
        steps -= 1
        next_pos, next_dir = find_next_pos(pos, dir)

    return pos, dir


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
pos, dir = move(pos, dir, instr_steps[0])
draw_map()

# all remaining moves
for i in range(len(instr_dir)):
    if instr_dir[i] == "R":
        dir = (dir + 1) % 4
    else:
        dir = (dir - 1) % 4

    print(f"dir: {dir}")
    print(f"steps: {instr_steps[i+1]}")
    print(f"start: {pos}")

    pos, dir = move(pos, dir, instr_steps[i+1])

    print(f"end: {pos}")

    draw_map()

result = (
    (1000*(pos[0]+1)) +
    (4*(pos[1]+1)) +
    (dir)
)
print(f"Task 2 result: {result}")

#end: [10, 10]

# 156184 too high
# 130204 too high
# 38465 too low