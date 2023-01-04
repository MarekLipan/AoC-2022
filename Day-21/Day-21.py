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

while "root" not in solutions:
    solved_equations = []
    for e in equations:
        if equations[e]["l"] in solutions and equations[e]["r"] in solutions:
            solutions[e] = int(eval(f"{solutions[equations[e]['l']]}{equations[e]['o']}{solutions[equations[e]['r']]}"))

print(f"Task 1 solution: {solutions['root']}")