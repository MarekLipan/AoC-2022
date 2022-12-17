import numpy as np
import re

# read the input into a list
file = open('Day-16/sample_input.txt', 'r')
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
non_zero_flow_vaults_num = 0
for v in valves:
    if valves[v]["flow"] > 0:
        non_zero_flow_vaults_num += 1

open_valves = 0
current_vault = "AA"

debug_path = []


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
        minute += 1
        result += (30 - minute) * f

    return result



def make_action(minute, current_release, current_vault, valves, debug_path):

    global max_release

    # find out if we are visiting twice the same vault since the last opening - condition for stopping
    last_open_index = len(debug_path)
    open_not_found = True

    while open_not_found and last_open_index > 0:
        last_open_index -= 1
        open_not_found = "open" != debug_path[last_open_index]

    repeated_visit = len(debug_path[last_open_index:]) > len(set(debug_path[last_open_index:]))


    # find out if there is even potential to reach better solution than so far
    potential_release = potential_max_gain(minute, valves) + current_release

    if (minute == 30) or repeated_visit or (potential_release <= max_release):
        max_release = max(max_release, current_release)
        return

    # make actions
    # action: open
    # open only valves with positive flow
    if valves[current_vault]["open"] == False and valves[current_vault]["flow"] > 0:
        valves[current_vault]["open"] = True
        minute += 1
        current_release +=  valves[current_vault]["flow"] * (30 - minute)

        debug_path.append(f"open")

        make_action(minute, current_release, current_vault, valves, debug_path)

        debug_path.pop()

        valves[current_vault]["open"] = False
        current_release -=  valves[current_vault]["flow"] * (30 - minute)
        minute -= 1
    # action: move
    for t in valves[current_vault]["tunnels"]:
        prev_vault = current_vault
        current_vault = t
        minute += 1

        debug_path.append(f"{current_vault}")

        make_action(minute, current_release, current_vault, valves, debug_path)

        debug_path.pop()

        current_vault = prev_vault
        minute -= 1

make_action(minute, current_release, current_vault, valves, debug_path)
print(f"Results task 1: {max_release}")




    

    

    