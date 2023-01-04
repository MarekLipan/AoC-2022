import numpy as np
from math import lcm

# read the input into a list
file = open('Day-11/input.txt', 'r')
L = file.read().splitlines()

LCM = lcm(11, 5, 7, 2, 17, 13, 3, 19)

M = 8  # monkeys
R = 10000  # rounds

class Monkey():
    def __init__(self, starting_items: list, operation: str, test: int, throw_true: int, throw_false: int) -> None:
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.throw_true = throw_true
        self.throw_false = throw_false
        self.inspections = 0
        return

    def turn(self):
        for i in self.items:
            self.inspections += 1
            old = i
            new = int(eval(self.operation) % LCM)
            # throw
            if new % self.test == 0:
                monkey_list[self.throw_true].items.append(new)
            else:
                monkey_list[self.throw_false].items.append(new)
        self.items = []
            

        return


monkey_list = []

for i in range(M):
    parsed_input = []

    parsed_input.append([int(x) for x in L[(i + (i)*6) + 1][18:].split(",")])
    parsed_input.append(L[(i + (i)*6) + 2][19:])
    parsed_input.append(int(L[(i + (i)*6) + 3][21:]))
    parsed_input.append(int(L[(i + (i)*6) + 4][29:]))
    parsed_input.append(int(L[(i + (i)*6) + 5][29:]))

    monkey_list.append(Monkey(*parsed_input))

for r in range(R):
    for m in range(M):
        monkey_list[m].turn()

for m in range(M):
    print(f"Monkey {m}: {monkey_list[m].items} and inspections: {monkey_list[m].inspections}")

total_inspections = []
for m in range(M):
    total_inspections.append(monkey_list[m].inspections)

# calculate monkey business
total_inspections.sort()
result = total_inspections[-2] * total_inspections[-1]
print(result)