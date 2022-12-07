import re

# read the input into a list
file = open('Day-5/day5_input1.txt', 'r')
L = file.read().splitlines()

def top_of_stacks(l: list) -> int:
    """
    Returns crates which are on top of the stacks after the moving in the instructions.
    """

    stacks = [[],[],[],[],[],[],[],[],[]]

    # build stacks
    for i in range(7, -1, -1):
        for j in range(1, len(l[i]), 4):
            stack_index = int((j-1)/4)
            element = l[i][j]
            if element != " ":
                stacks[stack_index].append(element)

    # move stacks
    for i in l[10:]:
        n, stack_from, stack_to = [int(n) for n in re.findall(r'\d+', i)]

        stack_from -= 1
        stack_to -= 1

        for s in range(n):

            element = stacks[stack_from].pop()
            stacks[stack_to].append(element)


    # read top of stacks
    result = ""
    for s in stacks:
        result += s[-1]

    return result


def top_of_stacks2(l: list) -> int:
    """
    Returns crates which are on top of the stacks after the moving in the instructions.
    """

    stacks = [[],[],[],[],[],[],[],[],[]]

    # build stacks
    for i in range(7, -1, -1):
        for j in range(1, len(l[i]), 4):
            stack_index = int((j-1)/4)
            element = l[i][j]
            if element != " ":
                stacks[stack_index].append(element)

    # move stacks
    for i in l[10:]:
        n, stack_from, stack_to = [int(n) for n in re.findall(r'\d+', i)]

        stack_from -= 1
        stack_to -= 1

        element = stacks[stack_from][-n:]
        del stacks[stack_from][-n:]
        stacks[stack_to] += element


    # read top of stacks
    result = ""
    for s in stacks:
        result += s[-1]

    return result


#print(top_of_stacks(L))
print(top_of_stacks2(L))









    
    

