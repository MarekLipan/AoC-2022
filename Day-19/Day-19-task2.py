import re
import time
import math

# read the input into a list
file = open('Day-19/input.txt', 'r')
L = file.read().splitlines()

blueprints = {}
max_geodes = {}
debug_count = 0

for l in L[:3]:
    i =[int(n) for n in re.findall('[-+]?\d+', l)]
    blueprints[i[0]] = {
        "geode": {"ore": i[5], "obsidian": i[6]},
        "obsidian": {"ore": i[3], "clay": i[4]},
        "clay": {"ore": i[2]},
        "ore": {"ore": i[1]},
    }
    max_geodes[i[0]] = 0

# if I buy something that I could buy earlier, it is a problem and the way is suboptimal

def round(i, minute, robots, resources, path):

    global max_geodes
    global debug_count

    #if debug_count >= 5:
    #    exit()

    minutes_until_end = 32 - minute

    # what to build next
    decisions = list(robots)

    # remove impossible options
    if robots["clay"] == 0:
        decisions.remove("obsidian")
        decisions.remove("geode")
    elif robots["obsidian"] == 0:
        decisions.remove("geode")

    # remove unreasonable options
    for r in ["ore", "clay", "obsidian"]:
        if robots[r] == max_robots[r]:
            decisions.remove(r)
    
    # already have enough of clay to build obsidian robots
    obs_robot_need = (max_robots["obsidian"] - robots["obsidian"])
    clay_need = obs_robot_need * blueprints[i]["obsidian"]["clay"]
    clay_dispose = resources["clay"] + (obs_robot_need - 1) * robots["clay"]

    if clay_dispose >= clay_need and "clay" in decisions:
        decisions.remove("clay")

    # already have enough obsidian to build geode robots until the end
    obs_need = minutes_until_end * blueprints[i]["geode"]["obsidian"]
    obs_dispose = resources["obsidian"] + (minutes_until_end - 1) * robots["obsidian"]

    if obs_dispose >= obs_need and "obsidian" in decisions:
        decisions.remove("obsidian")

    # take decision
    for d in decisions:
        # compute how many time it will take (+ 1 minute for building)
        minutes_need = 0
        for r in blueprints[i][d]:
            minutes_need = max(
                minutes_need, 
                math.ceil(max(blueprints[i][d][r] - resources[r], 0) / robots[r]) + 1
                )
        
        if minutes_until_end <= minutes_need:
            max_geodes[i] = max(max_geodes[i], resources["geode"] + (minutes_until_end * robots["geode"]))
            debug_count += 1
            return
        else:
            minute += minutes_need

            # resource gathering
            for r in robots:
                resources[r] += minutes_need * robots[r]

            # robot construction
            robots[d] += 1
            for r in blueprints[i][d]:
                resources[r] -= blueprints[i][d][r]

            path.append(d)
            round(i, minute, robots, resources, path)
            path.pop()

            # reverse robot construction
            robots[d] -= 1
            for r in blueprints[i][d]:
                resources[r] += blueprints[i][d][r]

            # reverse resource gathering
            for r in robots:
               resources[r] -= minutes_need * robots[r]

            minute -= minutes_need

    return

debug_count = 0

result = 1
print("Starting")
for i in blueprints:
    print(f"Blueprint: {i}")
    robots = {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0}
    resources = {"ore": 0, "clay": 0, "obsidian": 0, "geode": 0}
    # no need than to have more, because then you can produce a robot per round without waiting
    max_robots = {
        "ore": max([blueprints[i]["clay"]["ore"], blueprints[i]["obsidian"]["ore"], blueprints[i]["geode"]["ore"]]),
        "clay": blueprints[i]["obsidian"]["clay"],
        "obsidian": blueprints[i]["geode"]["obsidian"]
        }

    start = time.time()
    round(i, minute=0, robots=robots, resources=resources, path=[])
    end = time.time()
    print(end - start)

    result *= max_geodes[i]

print(max_geodes)

print(f"Result of task 2: {result}")
