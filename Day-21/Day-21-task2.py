from copy import deepcopy

# read the input into a list
file = open('Day-21/input.txt', 'r')
L = file.read().splitlines()

solutions = {}
equations = {}

for l in L:
    if l[6:].isnumeric():
        solutions[l[:4]] = int(l[6:])
    else:
        equations[l[:4]] = {"l": l[6:10], "o": l[10:13], "r": l[13:17]}


equations["root"]["o"] = " == "

# solve whatever can be solved without humn
solutions.pop("humn")

n = len(equations)
new_n = len(equations) - 1
while new_n < n:
    n = len(equations)
    solved_equations = []
    for e in equations:
        if equations[e]["l"] in solutions and equations[e]["r"] in solutions:
            solutions[e] = int(eval(f"{solutions[equations[e]['l']]}{equations[e]['o']}{solutions[equations[e]['r']]}"))
    new_n = len(equations)

orig_equations = deepcopy(equations)
orig_solutions = deepcopy(solutions)

# find humn
solution_found = False
s = -1

while solution_found == False:
    equations = deepcopy(orig_equations)
    solutions = deepcopy(orig_solutions)
    s += 1
    solutions["humn"] = s

    while "root" not in solutions:
        solved_equations = []
        for e in equations:
            if equations[e]["l"] in solutions and equations[e]["r"] in solutions:
                solutions[e] = int(eval(f"{solutions[equations[e]['l']]}{equations[e]['o']}{solutions[equations[e]['r']]}"))

    solution_found = bool(solutions["root"])

print(f"Task 2 solution: {solutions['humn']}")