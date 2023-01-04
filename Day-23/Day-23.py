# read the input into a list
file = open('Day-23/input.txt', 'r')
L = file.read().splitlines()

elf_pos = []
field = []

i = j = 0
for l in L:
    row = []
    for k in range(10):
        row.append(".")
    for k in l:
        row.append(k)
        if k == "#":
            elf_pos.append([i+10, j+10])
        j += 1
    for k in range(10):
        row.append(".")
    field.append(row)
    i += 1
    j = 0

row = []
for i in range(len(field[0])):
    row.append(".")

for r in range(10):
    row = []
    for i in range(len(field[0])):
        row.append(".")
    field = [row] + field
    row = []
    for i in range(len(field[0])):
        row.append(".")
    field = field + [row]

moves_queue = ["N", "S", "W", "E"]

for round in range(10):
    proposed_pos = []

    for e in elf_pos:
        x, y = e

        if (
            (field[x][y-1] == ".") and
            (field[x-1][y-1] == ".") and
            (field[x-1][y] == ".") and
            (field[x-1][y+1] == ".") and
            (field[x][y+1] == ".") and
            (field[x+1][y+1] == ".") and
            (field[x+1][y] == ".") and
            (field[x+1][y-1] == ".")
        ):
            proposed_pos.append([x, y])
        else:
            for m in (moves_queue + ["stay"]):
                if m == "N":
                    if (field[x-1][y-1] == ".") and (field[x-1][y] == ".") and (field[x-1][y+1] == "."):
                        proposed_pos.append([x-1, y])
                        break
                elif m == "S":
                    if (field[x+1][y-1] == ".") and (field[x+1][y] == ".") and (field[x+1][y+1] == "."):
                        proposed_pos.append([x+1, y])
                        break
                elif m == "W":
                    if (field[x-1][y-1] == ".") and (field[x][y-1] == ".") and (field[x+1][y-1] == "."):
                        proposed_pos.append([x, y-1])
                        break
                elif m == "E":
                    if (field[x-1][y+1] == ".") and (field[x][y+1] == ".") and (field[x+1][y+1] == "."):
                        proposed_pos.append([x, y+1])
                        break
                elif m == "stay":
                    proposed_pos.append([x, y])

    proposed_pos_map = {}
    for p in proposed_pos:
        proposed_pos_map[tuple(p)] = 1 + proposed_pos_map.get(tuple(p), 0)

    # moving
    for e in range(len(elf_pos)):
        if proposed_pos_map[tuple(proposed_pos[e])] == 1:
            field[elf_pos[e][0]][elf_pos[e][1]] = "."
            elf_pos[e] = proposed_pos[e]
            field[elf_pos[e][0]][elf_pos[e][1]] = "#"

    # switch up moves queue
    m = moves_queue.pop(0)
    moves_queue.append(m)


# find minimal rectangle
x_min = x_max = elf_pos[0][0]
y_min = y_max = elf_pos[0][1]
for e in elf_pos:
    x_min = min(x_min, e[0])
    x_max = max(x_max, e[0])
    y_min = min(y_min, e[1])
    y_max = max(y_max, e[1])

print(f"Result of task 1:{(x_max-x_min+1)*(y_max-y_min+1)-len(elf_pos)}")

outpufile = open('Day-23/field.txt',"w")
output = []
for i in range(len(field)):
    for j in range(len(field[i])):
            output.append(field[i][j])
    output.append("\n")

outpufile.writelines(output)
outpufile.close()