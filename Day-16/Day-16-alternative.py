import numpy as np
import re
from dijkstar import Graph, find_path
import itertools

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

    valves[input[0]] = {"flow": int(input[1]), "tunnels": input[2:]}


num_valves = len(valves)


# backtracking to check all possible actions to find the maximal release
max_release = 0
minute = 0
current_release = 0
non_zero_flow_vaults = []
for v in valves:
    if valves[v]["flow"] > 0:
        non_zero_flow_vaults.append(v)

# build graph
graph = Graph()
for v in valves:
    for t in valves[v]["tunnels"]:
        graph.add_edge(v, t, 1)

optimal_paths = {}

for comb in itertools.product(non_zero_flow_vaults, non_zero_flow_vaults):
    optimal_paths[comb] = best_path = find_path(graph, comb[0], comb[1]).nodes[1:]

minute = 0
max_release = 0
current_release = 0
path = []
unopened_non_zero_flow_vaults = non_zero_flow_vaults
my_turn = True
current_dst_valve = "AA"
e_path = []
e_current_dst_valve = "AA"

def make_action(minute, unopened_non_zero_flow_vaults, current_release, path, my_turn, current_dst_valve, valves, e_path, e_current_dst_valve):

    global max_release

    # find out if there is even potential to reach better solution than so far
    #potential_release = current_release
    #for v in unopened_non_zero_flow_vaults:
    #    potential_release += (26 - minute) * valves[v]["flow"]

    # or (potential_release <= max_release)


    if minute == 26 or unopened_non_zero_flow_vaults==[] :
        if current_release > max_release:
            max_release = current_release
        return

    if my_turn:

        

        # open if just arrived to destination
        if len(path) == 1:
            v = path.pop()
            if v in unopened_non_zero_flow_vaults:
                unopened_non_zero_flow_vaults.remove(v)
                current_release +=  valves[v]["flow"] * (26 - minute -1)
                minute += 1
                make_action(minute, unopened_non_zero_flow_vaults, current_release, path, not(my_turn), current_dst_valve, valves, e_path, e_current_dst_valve)
                minute -= 1
                current_release -=  valves[v]["flow"] * (26 - minute -1)
                unopened_non_zero_flow_vaults.append(v)
                path = [v]

        # choose path to next destination valve and start moving
        if path == []:
            for dst in unopened_non_zero_flow_vaults:
                prev_path = path
                path = find_path(graph, current_dst_valve, dst).nodes[1:]  # already move one step
                prev_dst_valve = current_dst_valve
                current_dst_valve = path[-1]
                minute += 1
                make_action(minute, unopened_non_zero_flow_vaults, current_release, path, not(my_turn), current_dst_valve, valves, e_path, e_current_dst_valve)
                minute -= 1
                current_dst_valve=prev_dst_valve
                path = prev_path

        # continue moving
        if len(path) > 1:
            prev_path = path
            path = path[1:]
            minute += 1
            make_action(minute, unopened_non_zero_flow_vaults, current_release, path, not(my_turn), current_dst_valve, valves, e_path, e_current_dst_valve)
            minute -= 1
            path = prev_path

    # elephant turn
    else:

         # open if just arrived to destination
        if len(e_path) == 1:
            v = e_path.pop()
            if v in unopened_non_zero_flow_vaults:
                unopened_non_zero_flow_vaults.remove(v)
                current_release +=  valves[v]["flow"] * (26 - minute -1)
                minute += 1
                make_action(minute, unopened_non_zero_flow_vaults, current_release, path, not(my_turn), current_dst_valve, valves, e_path, e_current_dst_valve)
                minute -= 1
                current_release -=  valves[v]["flow"] * (26 - minute -1)
                unopened_non_zero_flow_vaults.append(v)
                e_path = [v]

        # choose path to next destination valve and start moving
        if e_path == []:
            for dst in unopened_non_zero_flow_vaults:
                prev_e_path = e_path
                e_path = find_path(graph, e_current_dst_valve, dst).nodes[1:]  # already move one step
                prev_dst_valve = e_current_dst_valve
                e_current_dst_valve = e_path[-1]
                minute += 1
                make_action(minute, unopened_non_zero_flow_vaults, current_release, path, not(my_turn), current_dst_valve, valves, e_path, e_current_dst_valve)
                minute -= 1
                e_current_dst_valve=prev_dst_valve
                e_path = prev_e_path

        # continue moving
        if len(e_path) > 1:
            prev_path = e_path
            e_path = e_path[1:]
            minute += 1
            make_action(minute, unopened_non_zero_flow_vaults, current_release, path, not(my_turn), current_dst_valve, valves, e_path, e_current_dst_valve)
            minute -= 1
            e_path = prev_path

    

    

make_action(minute, unopened_non_zero_flow_vaults, current_release, path, my_turn, current_dst_valve, valves, e_path, e_current_dst_valve)


print(f"Results task 1: {max_release}")



    

    

    