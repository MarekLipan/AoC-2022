import numpy as np

debug_path = ['DD', 'CC', 'open']

# find out if we are visiting twice the same vault since the last opening - condition for stopping
last_open_index = len(debug_path)
open_not_found = True

while open_not_found and last_open_index > 0:
    last_open_index -= 1
    open_not_found = "open" != debug_path[last_open_index]

open_not_found = True
second_index = last_open_index

while open_not_found and last_open_index > 0:
    last_open_index -= 1
    open_not_found = "open" != debug_path[last_open_index]
first_index = last_open_index

print(first_index)
src = debug_path[first_index-1] 
dst = debug_path[second_index-1] 
path_for_check = debug_path[first_index+1:second_index]

print(first_index)
print(dst)

if len(path_for_check) > 0:
    optimal_path = optimal_paths[(src, dst)] == path_for_check