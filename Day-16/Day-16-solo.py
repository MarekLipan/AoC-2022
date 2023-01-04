import numpy as np
import re
from dijkstar import Graph, find_path
import itertools
import time
import tqdm
from multiprocessing import Pool

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


def potential_max_gain(minute, valves, vaults_yet_to_be_opened):
    """
    Computes what is the maximum possible gain if all the remaining nonzero valves were to be opened in the upcoming minutes
    """
    
    remaining_flows = []
    for v in valves:
        if v in vaults_yet_to_be_opened and valves[v]["flow"] > 0:
            remaining_flows.append(valves[v]["flow"])
        
    remaining_flows.sort(reverse=True)
    result = 0
    for f in remaining_flows:
        minute += 1
        result += (26 - minute) * f

    return result


# backtracking to check all possible actions to find the maximal release
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

# sort to have the biggest flow valves in the beginning
flows = []
for v in non_zero_flow_vaults:
    flows.append(valves[v]["flow"])
sort_indices = np.argsort(flows)[::-1]
unopened_non_zero_flow_vaults = np.array(non_zero_flow_vaults)[sort_indices].tolist()


def make_action(minute, target_vaults, current_release, path, current_dst_valve, valves):

    global max_release

    vaults_yet_to_be_opened = []
    for v in target_vaults:
        if not(valves[v]["open"]):
            vaults_yet_to_be_opened.append(v)

    # find out if there is even potential to reach better solution than so far
    potential_release = potential_max_gain(minute, valves, vaults_yet_to_be_opened) + current_release

    if minute == 26 or len(vaults_yet_to_be_opened)==0 or (potential_release <= max_release):
        if current_release > max_release:
            max_release = current_release
        return

    # open if just arrived to destination
    if len(path) == 1:
        v = path.pop()
        valves[v]["open"] = True
        current_release +=  valves[v]["flow"] * (26 - minute -1)
        minute += 1
        make_action(minute, target_vaults, current_release, path, current_dst_valve, valves)
        minute -= 1
        current_release -=  valves[v]["flow"] * (26 - minute -1)
        valves[v]["open"] = False
        path = [v]

    # choose path to next destination valve and start moving
    if path == []:
        for dst in vaults_yet_to_be_opened:
            prev_path = path
            path = find_path(graph, current_dst_valve, dst).nodes[1:]  # already move one step
            prev_dst_valve = current_dst_valve
            current_dst_valve = path[-1]
            minute += 1
            make_action(minute, target_vaults, current_release, path, current_dst_valve, valves)
            minute -= 1
            current_dst_valve=prev_dst_valve
            path = prev_path

    # continue moving
    if len(path) > 1:
        prev_path = path
        path = path[1:]
        minute += 1
        make_action(minute, target_vaults, current_release, path, current_dst_valve, valves)
        minute -= 1
        path = prev_path


def elephant_search(my_list, e_list):

    global max_release

    # my turn
    minute = 0
    max_release = 0
    current_release = 0
    path = []
    target_list = my_list
    current_dst_valve = "AA"

    make_action(minute, my_list, current_release, path, current_dst_valve, valves)

    my_max_release = max_release

    # elephant turn
    minute = 0
    max_release = 0
    current_release = 0
    path = []
    unopened_non_zero_flow_vaults = e_list
    current_dst_valve = "AA"

    make_action(minute, unopened_non_zero_flow_vaults, current_release, path, current_dst_valve, valves)

    e_max_release = max_release

    return (my_max_release + e_max_release)

# entry point for the program
if __name__ == '__main__':
    with Pool() as pool:
        all_combinations = []
        for n in range(int(len(non_zero_flow_vaults)/2)+1):
            for comb in itertools.combinations(non_zero_flow_vaults, n):
                my_list = list(comb)
                e_list = [i for i in non_zero_flow_vaults if i not in my_list]
                all_combinations.append((my_list, e_list))
        # call the same function with different data in parallel
        total_max_release = 0
        for result in tqdm.tqdm(pool.starmap(elephant_search, all_combinations)):
            if result > total_max_release:
                total_max_release = result
                print(total_max_release)

    

    

    