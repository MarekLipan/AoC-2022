import numpy as np
from dijkstar import Graph, find_path

# read the input into a list
file = open('Day-12/input.txt', 'r')
L = file.read().splitlines()

# translate to numpy matrix
to_be_array = []
for l in L:
    to_be_row = []
    for k in l:
        to_be_row.append(k)
    to_be_array.append(to_be_row)

array = np.array(to_be_array)

# positions of start and end
start = np.where(array== "S")
start = (start[0][0], start[1][0])
end = np.where(array== "E")
end = (end[0][0], end[1][0])

# replace start and end with appropriate levels
array[start] = "a"
array[end] = "z"

# write the graph
graph = Graph()

for i in range(array.shape[0]):
    for j in range(array.shape[1]):
        # add all valid edges
        viable_level = (ord(array[(i, j)]) + 1)
        # left
        if ((j-1) >= 0) and (ord(array[(i, j-1)]) <= viable_level):
            graph.add_edge((i, j), (i, j-1), 1)
        if ((j+1) < array.shape[1]) and (ord(array[(i, j+1)]) <= viable_level):
            graph.add_edge((i, j), (i, j+1), 1)
        if ((i-1) >= 0) and (ord(array[(i-1, j)]) <= viable_level):
            graph.add_edge((i, j), (i-1, j), 1)
        if ((i+1) < array.shape[0]) and (ord(array[(i+1, j)]) <= viable_level):
            graph.add_edge((i, j), (i+1, j), 1)

best_path = find_path(graph, start, end)
print(best_path.total_cost)