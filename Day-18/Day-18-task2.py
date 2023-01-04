import sys
sys.setrecursionlimit(10000)

# read the input into a list
file = open('Day-18/input.txt', 'r')
L = file.read().splitlines()

input = []
for l in L:
    input.append([int(i) for i in l.split(",")])

def count_sides(input):
    """
    Count exposed sides
    """
    sides = []

    for i in input:
        x, y, z = i

        sides.append((x, y - 0.5, z - 0.5))
        sides.append((x - 1, y - 0.5, z - 0.5))

        sides.append((x - 0.5, y, z - 0.5))
        sides.append((x - 0.5, y - 1, z - 0.5))

        sides.append((x - 0.5, y - 0.5, z))
        sides.append((x - 0.5, y - 0.5, z - 1))

    unique_sides = set()
    for s in sides:
        if s in unique_sides:
            unique_sides.remove(s)
        else:
            unique_sides.add(s)

    return(len(unique_sides))

print(f"Result for task 1: {count_sides(input)}")

x_min, y_min, z_min = input[0]
x_max, y_max, z_max = input[0]

for i in input:
    x, y, z = i
    x_min = min(x_min, x)
    x_max = max(x_max, x)
    y_min = min(y_min, y)
    y_max = max(y_max, y)
    z_min = min(z_min, z)
    z_max = max(z_max, z)

x_min -= 1
x_max += 1
y_min -= 1
y_max += 1
z_min -= 1
z_max += 1

cubes = set([tuple(i) for i in input])

print((x_min, y_min, z_min) in cubes)

unique_sides_from_outside = set()

def walk_step(cc):
    """
    Fill in the the space with cubes, wherever you can get from "outside"
    """

    cubes.add(cc)

    x, y, z = cc

    next_steps = []

    if (x-1) >= x_min:
        next_steps.append((x-1, y, z))
    if (x+1) <= x_max:
        next_steps.append((x+1, y, z))
    if (y-1) >= y_min:  
        next_steps.append((x, y-1, z))
    if (y+1) <= y_max:
        next_steps.append((x, y+1, z))
    if (z-1) >= z_min: 
        next_steps.append((x, y, z-1))
    if (z+1) <= z_max: 
        next_steps.append((x, y, z+1))

    for s in next_steps:
        if s not in cubes:
            walk_step(s)
    
    return

walk_step((x_min, y_min, z_min))

X = (x_max - x_min + 1)
Y = (y_max - y_min + 1)
Z = (z_max - z_min + 1)

surface = (X * Y * 2) + (X * Z * 2) + (Y * Z * 2)

print(f"Result for task 2: {count_sides(input) - (count_sides(cubes) - surface)}")

