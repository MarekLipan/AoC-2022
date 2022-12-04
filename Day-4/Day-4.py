import re

# read the input into a list
file = open('Day-4/day4_input1.txt', 'r')
L = file.read().splitlines()

def full_containment(l: list) -> int:
    """
    In how many pairs of elves are sections of one fully contained by the other
    """

    result = 0

    for i in l:
        a, b, c, d = [int(n) for n in re.findall(r'\d+', i)]

        if ((a >= c) and (b <= d)) or ((c >= a) and (d <= b)):
            result += 1

    return result

print(full_containment(L))









    
    

