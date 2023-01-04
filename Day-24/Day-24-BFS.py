import math

# read the input into a list
file = open('Day-24/input.txt', 'r')
L = file.read().splitlines()

arrows_up = []
arrows_down = []
arrows_left = []
arrows_right = []

time_field_up = []
time_field_down = []
time_field_left = []
time_field_right = []
time_field_empty = []
time_field_visit = []
reverse_time_field_empty = []

i=0
for l in L:
    for j in range(len(l)):
        if l[j] == "^":
            arrows_up.append([i, j])
        elif l[j] == "v":
            arrows_down.append([i, j])
        elif l[j] == ">":
            arrows_right.append([i, j])
        elif l[j] == "<":
            arrows_left.append([i, j])
    i+=1

x_max = j
y_max = i - 1

def move_arrows_round(direction):
    if direction == "f":
        for i in range(len(arrows_up)):
            if arrows_up[i][0] > 1:
                arrows_up[i][0] -= 1
            else:
                arrows_up[i][0] = y_max - 1
        for i in range(len(arrows_down)):
            if arrows_down[i][0] < y_max - 1:
                arrows_down[i][0] += 1
            else:
                arrows_down[i][0] = 1
        for i in range(len(arrows_left)):
            if arrows_left[i][1] > 1:
                arrows_left[i][1] -= 1
            else:
                arrows_left[i][1] = x_max - 1
        for i in range(len(arrows_right)):
            if arrows_right[i][1] < x_max - 1:
                arrows_right[i][1] += 1
            else:
                arrows_right[i][1] = 1


n_row = len(L)
n_col = len(L[0])

start = [0, 1]
end = [len(L)-1, n_col-2]
in_front_of_end = [len(L)-2, n_col-2]

def lcm(a,b):
  return (a * b) // math.gcd(a,b)

period = lcm(n_row-2, n_col-2)

print(f"n_row-2: {n_row-2}")
print(f"n_col-2: {n_col-2}")
print(f"period: {period}")

for i in range(n_row):
    row = []
    for j in range(n_col):
        row.append(set())
    time_field_up.append(row)

for i in range(n_row):
    row = []
    for j in range(n_col):
        row.append(set())
    time_field_down.append(row)

for i in range(n_row):
    row = []
    for j in range(n_col):
        row.append(set())
    time_field_left.append(row)

for i in range(n_row):
    row = []
    for j in range(n_col):
        row.append(set())
    time_field_right.append(row)

for i in range(n_row):
    row = []
    for j in range(n_col):
        row.append(set())
    time_field_empty.append(row)

for i in range(n_row):
    row = []
    for j in range(n_col):
        row.append(set())
    reverse_time_field_empty.append(row)

for i in range(n_row):
    row = []
    for j in range(n_col):
        row.append(-1)
    time_field_visit.append(row)

for p in range(period):
    for a in arrows_up:
        time_field_up[a[0]][a[1]].add(p)
    for a in arrows_down:
        time_field_down[a[0]][a[1]].add(p)
    for a in arrows_left:
        time_field_left[a[0]][a[1]].add(p)
    for a in arrows_right:
        time_field_right[a[0]][a[1]].add(p)

    for i in range(n_row):
        for j in range(n_col):
            if (
                p not in time_field_up[i][j] and
                p not in time_field_down[i][j] and
                p not in time_field_left[i][j] and
                p not in time_field_right[i][j] and
                (i != 0) and
                (i != n_row-1) and
                (j != 0) and
                (j != n_col-1)
                ) or [i, j] == start  or [i, j] == end:
                time_field_empty[i][j].add(p)
                reverse_time_field_empty[n_row - i - 1][n_col - j - 1].add(p)
        

    move_arrows_round("f")


def BFS(minute):

    new_positions = []

    for i in range(len(time_field_visit)):
        for j in range(len(time_field_visit[i])):
            if time_field_visit[i][j] == minute:
                # down
                if (
                    ((minute+1) % period) in time_field_empty[i+1][j]
                ):
                    new_positions.append([i+1, j])
                # up
                if (
                    ((minute+1) % period) in time_field_empty[i-1][j]
                ):
                    new_positions.append([i-1, j])
                # left
                if (
                    ((minute+1) % period) in time_field_empty[i][j-1]
                ):
                    new_positions.append([i, j-1])
                # right
                if (
                    ((minute+1) % period) in time_field_empty[i][j+1]
                ):
                    new_positions.append([i, j+1])
                # wait
                if (
                    ((minute+1) % period) in time_field_empty[i][j]
                ):
                    new_positions.append([i, j])

    for i, j in new_positions:
        time_field_visit[i][j] = minute + 1
    return

reverse = False

if reverse == True:
    time_field_empty = reverse_time_field_empty

m = 477
time_field_visit[start[0]][start[1]] = m
while time_field_visit[end[0]][end[1]] == -1:
    BFS(m)
    m += 1

print(f"Result of task 1: {m}")

print(f"Result of task 2: {477}")

outpufile = open('Day-24/field.txt',"w")
output = []
for i in range(len(time_field_visit)):
    for j in range(len(time_field_visit[i])):
            if time_field_visit[i][j] == -1:
                output.append(" . ")
            else:
                output.append("{:03d}".format(time_field_visit[i][j]))
    output.append("\n")

outpufile.writelines(output)
outpufile.close()
