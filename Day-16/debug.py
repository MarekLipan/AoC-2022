debug_path = ['DD', 'open', 'CC', 'open', 'DD', 'CC', 'DD', 'CC', 'DD', 'CC', 'DD', 'CC', 'DD', 'CC', 'DD', 'CC', 'DD', 'EE']
print(debug_path)

# find out if we are visiting twice the same vault since the last opening - condition for stopping
last_open_index = len(debug_path)
open_not_found = True

print(last_open_index)

while open_not_found and last_open_index > 0:
    last_open_index -= 1
    open_not_found = "open" != debug_path[last_open_index]

print(debug_path[last_open_index:])

repeated_visit = len(debug_path[last_open_index:]) > len(set(debug_path[last_open_index:]))

print(repeated_visit)