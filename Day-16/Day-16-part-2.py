import numpy as np
import re
from dijkstar import Graph, find_path
import itertools

# read the input into a list
file = open('Day-16/input.txt', 'r')
L = file.read().splitlines()

valves = {}

# parse input
for l in L:
    input = re.sub("Valve ", "", l)
    input = re.sub(" has flow rate=", ",", input)
    input = re.sub("; tunnels lead to valves ", ",", input)
    input = re.sub("; tunnel leads to valve ", ",", input)
    input = re.sub(" ", "", input)
    input = input.split(",")

    valves[input[0]] = {"flow": int(input[1]), "open": False, "tunnels": input[2:]}


num_valves = len(valves)


# backtracking to check all possible actions to find the maximal release
max_release = 0
minute = 0
current_release = 0
non_zero_flow_vaults = []
for v in valves:
    if valves[v]["flow"] > 0:
        non_zero_flow_vaults.append(v)

open_valves = 0
current_vault = "AA"

debug_path = []
e_debug_path = []
my_turn = True
e_current_vault = "AA"

# build graph
graph = Graph()
for v in valves:
    for t in valves[v]["tunnels"]:
        graph.add_edge(v, t, 1)

optimal_paths = {}

for comb in itertools.product(non_zero_flow_vaults, non_zero_flow_vaults):
    optimal_paths[comb] = best_path = find_path(graph, comb[0], comb[1]).nodes[1:]

def potential_max_gain(minute, valves):
    """
    Computes what is the maximum possible gain if all the remaining nonzero valves were to be opened in the upcoming minutes
    """
    
    remaining_flows = []
    for v in valves:
        if valves[v]["open"] == False and valves[v]["flow"] > 0:
            remaining_flows.append(valves[v]["flow"])
        
    remaining_flows.sort(reverse=True)
    result = 0
    for f in remaining_flows:
        #minute += 1
        result += (26 - minute) * f

    return result


def check_optimal_path(debug_path):
    """
    Check if the path between the last two openings was optimal, if not, then the solution is not optimal
    """

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

    path_for_check = debug_path[first_index+1:second_index]

    if first_index > 0:
        src = debug_path[first_index-1] 
        dst = debug_path[second_index-1] 
        optimal_path = optimal_paths[(src, dst)] == path_for_check
    else:
        optimal_path = True
    
    return optimal_path



def make_action(minute, current_release, current_vault, valves, debug_path, my_turn, e_current_vault, e_debug_path):

    global max_release

    # find out if we are visiting twice the same vault since the last opening - condition for stopping
    last_open_index = len(debug_path)
    open_not_found = True

    while open_not_found and last_open_index > 0:
        last_open_index -= 1
        open_not_found = "open" != debug_path[last_open_index]

    repeated_visit = len(debug_path[last_open_index:]) > len(set(debug_path[last_open_index:]))

    # same for elephant
    last_open_index = len(e_debug_path)
    open_not_found = True

    while open_not_found and last_open_index > 0:
        last_open_index -= 1
        open_not_found = "open" != e_debug_path[last_open_index]

    e_repeated_visit = len(e_debug_path[last_open_index:]) > len(set(e_debug_path[last_open_index:]))

    # check if the path was optimal between the openings
    optimal_path = check_optimal_path(debug_path)
    e_optimal_path = check_optimal_path(e_debug_path)


    # find out if there is even potential to reach better solution than so far
    potential_release = potential_max_gain(minute, valves) + current_release

    #  or not(optimal_path) or not(e_optimal_path)
    if (minute == 26) or repeated_visit or e_repeated_visit or (potential_release <= max_release):
        if current_release > max_release:
            max_release = current_release
            print(current_release)

        return 


    if my_turn:
        # make actions
        # action: open
        # open only valves with positive flow
        if valves[current_vault]["open"] == False and valves[current_vault]["flow"] > 0:
            valves[current_vault]["open"] = True
            current_release +=  valves[current_vault]["flow"] * (26 - minute-1)

            debug_path.append(f"open")

            make_action(minute, current_release, current_vault, valves, debug_path, not(my_turn), e_current_vault, e_debug_path)

            debug_path.pop()

            valves[current_vault]["open"] = False
            current_release -=  valves[current_vault]["flow"] * (26 - minute -1)

        # action: move
        for t in valves[current_vault]["tunnels"]:
            prev_vault = current_vault
            current_vault = t

            debug_path.append(f"{current_vault}")

            make_action(minute, current_release, current_vault, valves, debug_path, not(my_turn), e_current_vault, e_debug_path)

            debug_path.pop()

            current_vault = prev_vault
    else:
        # make actions
        # action: open
        # open only valves with positive flow
        if valves[e_current_vault]["open"] == False and valves[e_current_vault]["flow"] > 0:
            valves[e_current_vault]["open"] = True
            minute += 1
            current_release +=  valves[e_current_vault]["flow"] * (26 - minute)

            e_debug_path.append(f"open")

            make_action(minute, current_release, current_vault, valves, debug_path, not(my_turn), e_current_vault, e_debug_path)

            e_debug_path.pop()

            valves[e_current_vault]["open"] = False
            current_release -=  valves[e_current_vault]["flow"] * (26 - minute)
            minute -= 1
        # action: move
        for t in valves[e_current_vault]["tunnels"]:
            prev_vault = e_current_vault
            e_current_vault = t
            minute += 1

            e_debug_path.append(f"{e_current_vault}")

            make_action(minute, current_release, current_vault, valves, debug_path, not(my_turn), e_current_vault, e_debug_path)

            e_debug_path.pop()

            e_current_vault = prev_vault
            minute -= 1

make_action(minute, current_release, current_vault, valves, debug_path, my_turn, e_current_vault, e_debug_path)
print(f"Results task 1: {max_release}")



    

    

    