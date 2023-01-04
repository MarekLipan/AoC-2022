import re
import time

# read the input into a list
file = open('Day-19/sample_input.txt', 'r')
L = file.read().splitlines()

blueprints = {}
max_geodes = {}

for l in L:
    i =[int(n) for n in re.findall('[-+]?\d+', l)]
    blueprints[i[0]] = {
        "geode": {"ore": i[5], "obsidian": i[6]},
        "obsidian": {"ore": i[3], "clay": i[4]},
        "clay": {"ore": i[2]},
        "ore": {"ore": i[1]},
    }
    max_geodes[i[0]] = 0


# if I buy something that I could buy earlier, it is a problem and the way is suboptimal

def round(i, minute, robots, resources, actions_not_taken, debug_path):
    global debug_count

    if debug_count == 1:
        return

    if minute == 24:
        max_geodes[i] = max(max_geodes[i], resources["geode"])
        if max_geodes[i] == 9:
            print(debug_path)
            debug_count += 1

        return 

    # availability for construction check
    decisions = ["idle"]
    for r in blueprints[i]:
        available = True
        for res in blueprints[i][r]:
            available *= resources[res] >= blueprints[i][r][res]
        if available:
            decisions.append(r)


    # pruning
    if "ore" in decisions:
        if "clay" in decisions:
            if "obsidian" in decisions:
                if "geode" in decisions:
                    decisions.remove("idle")
                elif robots["obsidian"] == 0:
                    decisions.remove("idle")
            elif robots["clay"] == 0:
                decisions.remove("idle")

    for a in actions_not_taken:
        decisions.remove(a)

    # decision
    for d in decisions:
        if d == "idle":
            for r in robots:
                resources[r] += robots[r]
            minute += 1

            for a in decisions:
                if a != "idle":
                    actions_not_taken.add(a)

            debug_path.append(d)

            round(i, minute, robots, resources, actions_not_taken, debug_path)

            debug_path.pop()

            minute -= 1
            for r in robots:
                resources[r] -= robots[r]
        else:
            for r in robots:
                resources[r] += robots[r]
            for res in blueprints[i][d]:
                resources[res] -= blueprints[i][d][res]
            robots[d] += 1
            minute += 1
            actions_not_taken = set()
            debug_path.append(d)

            round(i, minute, robots, resources, actions_not_taken, debug_path)

            debug_path.pop()

            minute -= 1
            robots[d] -= 1
            for res in blueprints[i][d]:
                resources[res] += blueprints[i][d][res]
            for r in robots:
                resources[r] -= robots[r]

    return

debug_count = 0

result = 0
print("Starting")
for i in blueprints:
    print(f"Blueprint: {i}")
    robots = {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0}
    resources = {"ore": 0, "clay": 0, "obsidian": 0, "geode": 0}
    start = time.time()
    round(i, minute=0, robots=robots, resources=resources, actions_not_taken=set(), debug_path=[])
    end = time.time()
    print(end - start)
    result += i * max_geodes[i]
    break

print(max_geodes)

print(f"Result of task 1: {result}")
