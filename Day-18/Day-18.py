# read the input into a list
file = open('Day-18/input.txt', 'r')
L = file.read().splitlines()

input = []
for l in L:
    input.append([int(i) for i in l.split(",")])

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

print(f"Result for task 1: {len(unique_sides)}")
