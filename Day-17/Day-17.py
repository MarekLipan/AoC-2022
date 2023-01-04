# read the input into a list
file = open('Day-17/input.txt', 'r')
L = [l for l in file.read().splitlines()[0]]


def rock_0():
    """
    Simulates rock fall of the rock type 0
    """
    global field
    global l
    
    field.append([1, 0, 0, 0, 0, 0, 0, 0, 1])

    x0y0 = [3, len(field)-1]
    x1y0 = [4, len(field)-1]
    x2y0 = [5, len(field)-1]
    x3y0 = [6, len(field)-1]

    falling_in_progress = True

    while falling_in_progress:
        # side movement
        if L[l % len(L)] == ">":
            if field[x3y0[1]][x3y0[0] + 1] == 0:
                x0y0[0] += 1
                x1y0[0] += 1
                x2y0[0] += 1
                x3y0[0] += 1
        else:
            if field[x0y0[1]][x0y0[0] - 1] == 0:
                x0y0[0] -= 1
                x1y0[0] -= 1
                x2y0[0] -= 1
                x3y0[0] -= 1
        l += 1
        # down movement
        if (
            (field[x0y0[1]-1][x0y0[0]] == 0) and
            (field[x1y0[1]-1][x1y0[0]] == 0) and
            (field[x2y0[1]-1][x2y0[0]] == 0) and
            (field[x3y0[1]-1][x3y0[0]] == 0)
        ):
            x0y0[1] -= 1
            x1y0[1] -= 1
            x2y0[1] -= 1
            x3y0[1] -= 1     
        else:
            falling_in_progress = False

    # insert rock
    field[x0y0[1]][x0y0[0]] = 1
    field[x1y0[1]][x1y0[0]] = 1
    field[x2y0[1]][x2y0[0]] = 1
    field[x3y0[1]][x3y0[0]] = 1

    # delete blank lines
    while sum(field[-1]) == 2:
        field.pop()

    return

def rock_1():
    """
    Simulates rock fall of the rock type 1
    """
    global field
    global l
    
    field.append([1, 0, 0, 0, 0, 0, 0, 0, 1])
    field.append([1, 0, 0, 0, 0, 0, 0, 0, 1])
    field.append([1, 0, 0, 0, 0, 0, 0, 0, 1])

    x1y0 = [4, len(field)-3]
    x0y1 = [3, len(field)-2]
    x1y1 = [4, len(field)-2]
    x2y1 = [5, len(field)-2]
    x1y2 = [4, len(field)-1]

    falling_in_progress = True

    while falling_in_progress:
        # side movement
        if L[l % len(L)] == ">":
            if (
                (field[x1y2[1]][x1y2[0] + 1] == 0) and
                (field[x2y1[1]][x2y1[0] + 1] == 0) and
                (field[x1y0[1]][x1y0[0] + 1] == 0)
            ):
                x1y0[0] += 1
                x0y1[0] += 1
                x1y1[0] += 1
                x2y1[0] += 1
                x1y2[0] += 1

        else:
            if (
                (field[x1y2[1]][x1y2[0] - 1] == 0) and
                (field[x0y1[1]][x0y1[0] - 1] == 0) and
                (field[x1y0[1]][x1y0[0] - 1] == 0)
            ):
                x1y0[0] -= 1
                x0y1[0] -= 1
                x1y1[0] -= 1
                x2y1[0] -= 1
                x1y2[0] -= 1
        l += 1
        # down movement
        if (
            (field[x1y0[1]-1][x1y0[0]] == 0) and
            (field[x0y1[1]-1][x0y1[0]] == 0) and
            (field[x2y1[1]-1][x2y1[0]] == 0)
        ):
            x1y0[1] -= 1
            x0y1[1] -= 1
            x1y1[1] -= 1
            x2y1[1] -= 1
            x1y2[1] -= 1   
        else:
            falling_in_progress = False

    # insert rock
    field[x1y0[1]][x1y0[0]] = 1
    field[x0y1[1]][x0y1[0]] = 1
    field[x1y1[1]][x1y1[0]] = 1
    field[x2y1[1]][x2y1[0]] = 1
    field[x1y2[1]][x1y2[0]] = 1

    # delete blank lines
    while sum(field[-1]) == 2:
        field.pop()

    return

def rock_2():
    """
    Simulates rock fall of the rock type 2
    """
    global field
    global l
    
    field.append([1, 0, 0, 0, 0, 0, 0, 0, 1])
    field.append([1, 0, 0, 0, 0, 0, 0, 0, 1])
    field.append([1, 0, 0, 0, 0, 0, 0, 0, 1])

    x0y0 = [3, len(field)-3]
    x1y0 = [4, len(field)-3]
    x2y0 = [5, len(field)-3]
    x2y1 = [5, len(field)-2]
    x2y2 = [5, len(field)-1]

    falling_in_progress = True

    while falling_in_progress:
        # side movement
        if L[l % len(L)] == ">":
            if (
                (field[x2y0[1]][x2y0[0] + 1] == 0) and
                (field[x2y1[1]][x2y1[0] + 1] == 0) and
                (field[x2y2[1]][x2y2[0] + 1] == 0)
            ):
                x0y0[0] += 1
                x1y0[0] += 1
                x2y0[0] += 1
                x2y1[0] += 1
                x2y2[0] += 1
        else:
            if (
                (field[x0y0[1]][x0y0[0] - 1] == 0) and
                (field[x2y1[1]][x2y1[0] - 1] == 0) and
                (field[x2y2[1]][x2y2[0] - 1] == 0)
            ):
                x0y0[0] -= 1
                x1y0[0] -= 1
                x2y0[0] -= 1
                x2y1[0] -= 1
                x2y2[0] -= 1
        l += 1
        # down movement
        if (
            (field[x0y0[1]-1][x0y0[0]] == 0) and
            (field[x1y0[1]-1][x1y0[0]] == 0) and
            (field[x2y0[1]-1][x2y0[0]] == 0)
        ):
            x0y0[1] -= 1
            x1y0[1] -= 1
            x2y0[1] -= 1
            x2y1[1] -= 1
            x2y2[1] -= 1   
        else:
            falling_in_progress = False

    # insert rock
    field[x0y0[1]][x0y0[0]] = 1
    field[x1y0[1]][x1y0[0]] = 1
    field[x2y0[1]][x2y0[0]] = 1
    field[x2y1[1]][x2y1[0]] = 1
    field[x2y2[1]][x2y2[0]] = 1

    # delete blank lines
    while sum(field[-1]) == 2:
        field.pop()

    return

def rock_3():
    """
    Simulates rock fall of the rock type 3
    """
    global field
    global l
    
    field.append([1, 0, 0, 0, 0, 0, 0, 0, 1])
    field.append([1, 0, 0, 0, 0, 0, 0, 0, 1])
    field.append([1, 0, 0, 0, 0, 0, 0, 0, 1])
    field.append([1, 0, 0, 0, 0, 0, 0, 0, 1])

    x0y0 = [3, len(field)-4]
    x0y1 = [3, len(field)-3]
    x0y2 = [3, len(field)-2]
    x0y3 = [3, len(field)-1]

    falling_in_progress = True

    while falling_in_progress:
        # side movement
        if L[l % len(L)] == ">":
            if (
                (field[x0y0[1]][x0y0[0] + 1] == 0) and
                (field[x0y1[1]][x0y1[0] + 1] == 0) and
                (field[x0y2[1]][x0y2[0] + 1] == 0) and
                (field[x0y3[1]][x0y3[0] + 1] == 0)
            ):
                x0y0[0] += 1
                x0y1[0] += 1
                x0y2[0] += 1
                x0y3[0] += 1

        else:
            if (
                (field[x0y0[1]][x0y0[0] - 1] == 0) and
                (field[x0y1[1]][x0y1[0] - 1] == 0) and
                (field[x0y2[1]][x0y2[0] - 1] == 0) and
                (field[x0y3[1]][x0y3[0] - 1] == 0)
            ):
                x0y0[0] -= 1
                x0y1[0] -= 1
                x0y2[0] -= 1
                x0y3[0] -= 1
        l += 1
        # down movement
        if (
            (field[x0y0[1]-1][x0y0[0]] == 0)
        ):
            x0y0[1] -= 1
            x0y1[1] -= 1
            x0y2[1] -= 1
            x0y3[1] -= 1
        else:
            falling_in_progress = False

    # insert rock
    field[x0y0[1]][x0y0[0]] = 1
    field[x0y1[1]][x0y1[0]] = 1
    field[x0y2[1]][x0y2[0]] = 1
    field[x0y3[1]][x0y3[0]] = 1

    # delete blank lines
    while sum(field[-1]) == 2:
        field.pop()

    return

def rock_4():
    """
    Simulates rock fall of the rock type 4
    """
    global field
    global l
    
    field.append([1, 0, 0, 0, 0, 0, 0, 0, 1])
    field.append([1, 0, 0, 0, 0, 0, 0, 0, 1])

    x0y0 = [3, len(field)-2]
    x1y0 = [4, len(field)-2]
    x0y1 = [3, len(field)-1]
    x1y1 = [4, len(field)-1]

    falling_in_progress = True

    while falling_in_progress:
        # side movement
        if L[l % len(L)] == ">":
            if (
                (field[x1y0[1]][x1y0[0] + 1] == 0) and
                (field[x1y1[1]][x1y1[0] + 1] == 0) 
            ):
                x0y0[0] += 1
                x1y0[0] += 1
                x0y1[0] += 1
                x1y1[0] += 1

        else:
            if (
                (field[x0y0[1]][x0y0[0] - 1] == 0) and
                (field[x0y1[1]][x0y1[0] - 1] == 0) 
            ):
                x0y0[0] -= 1
                x1y0[0] -= 1
                x0y1[0] -= 1
                x1y1[0] -= 1
        l += 1
        # down movement
        if (
            (field[x0y0[1]-1][x0y0[0]] == 0) and
            (field[x1y0[1]-1][x1y0[0]] == 0)
        ):
            x0y0[1] -= 1
            x1y0[1] -= 1
            x0y1[1] -= 1
            x1y1[1] -= 1
        else:
            falling_in_progress = False

    # insert rock
    field[x0y0[1]][x0y0[0]] = 1
    field[x1y0[1]][x1y0[0]] = 1
    field[x0y1[1]][x0y1[0]] = 1
    field[x1y1[1]][x1y1[0]] = 1

    # delete blank lines
    while sum(field[-1]) == 2:
        field.pop()

    return

R = 2022

field = [[1, 1, 1, 1, 1, 1, 1, 1, 1]]
l = 0
r = 0

while r < R:

    rock_type = r % 5

    # new rock falling
    field.append([1, 0, 0, 0, 0, 0, 0, 0, 1])
    field.append([1, 0, 0, 0, 0, 0, 0, 0, 1])
    field.append([1, 0, 0, 0, 0, 0, 0, 0, 1])

    if rock_type == 0:
        rock_0()
    elif rock_type == 1:
        rock_1()
    elif rock_type == 2:
        rock_2()
    elif rock_type == 3:
        rock_3()
    elif rock_type == 4:
        rock_4()

    r += 1

print(f"Result task 1: {len(field)-1}")

outpufile = open('Day-17/debug_output.txt',"w")
output = []
for i in range(len(field)-1, -1, -1):
    for j in range(len(field[i])):
        if field[i][j] == 1:
            output.append("#")
        else:
            output.append(".")
    output.append("\n")

outpufile.writelines(output)
outpufile.close()
