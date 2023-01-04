from sympy import solve, Symbol

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

# find humn
def express_term(term: str) -> str:

    e = equations[term]

    if e["l"] in solutions:
        left_term = str(solutions[e["l"]])
    elif e["l"] == "humn":
        left_term = "humn"
    else:
        left_term = express_term(e["l"])

    if e["r"] in solutions:
        right_term = str(solutions[e["r"]])
    elif e["r"] == "humn":
        right_term = "humn"
    else:
        right_term = express_term(e["r"])

    if left_term.isnumeric() and right_term.isnumeric():
        expressed_term = str(int(eval(left_term + e["o"] + right_term)))
    else:
        expressed_term = "(" + left_term + e["o"] + right_term + ")"

    return expressed_term


main_equation = express_term("root").replace("==","-")

print(main_equation)

humn = Symbol("humn")

print(
    f"Task2 solution: {solve(main_equation, humn)[0]}"
)