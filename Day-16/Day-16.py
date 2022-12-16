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
vaults_visited = set()

def make_action(minute, current_release, current_vault, valves, open_valves, vaults_visited):
    if (minute == 30) or (open_valves == non_zero_flow_vaults_num) or (current_vault in vaults_visited):
        global max_release
        max_release = max(max_release, current_release)
        return

    vaults_visited.add(current_vault)

    # make actions
    if open_valves < num_valves:
        # action: open
        if valves[current_vault]["open"] == False:
            valves[current_vault]["open"] = True
            minute += 1
            current_release +=  valves[current_vault]["flow"] * (30 - minute)
            open_valves += 1
            vaults_visited = set()  # reset with action
            make_action(minute, current_release, current_vault, valves, open_valves, vaults_visited)
            open_valves -= 1
            valves[current_vault]["open"] = False
            current_release -=  valves[current_vault]["flow"] * (30 - minute)
            minute -= 1
        # action: move
        for t in valves[current_vault]["tunnels"]:
            prev_vault = current_vault
            current_vault = t
            minute += 1
            make_action(minute, current_release, current_vault, valves, open_valves, vaults_visited)
            current_vault = prev_vault
            minute -= 1
    else:
        # action: wait
        minute += 1
        make_action(minute, current_release, current_vault, valves, open_valves, vaults_visited)

make_action(minute, current_release, current_vault, valves, open_valves, vaults_visited)
print(f"Results task 1: {max_release}")


    

    

    