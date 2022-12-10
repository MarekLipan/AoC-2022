import numpy as np
import re

# read the input into a list
file = open('Day-10/input.txt', 'r')
L = file.read().splitlines()

def signal_strength(l: list) -> int:
    """
    Return the singnal strength after the 20th, 60th, 100th, 140th, 180th, and 220th cycles
    """
    
    x_values = [1]

    for i in l:
        if i=="noop":
            x_values.append(x_values[-1])
        else:
            value = int(i[5:])
            x_values.append(x_values[-1])
            x_values.append(x_values[-1] + value)

    result = 0

    for i in [20, 60, 100, 140, 180, 220]:
        result += i * x_values[i-1]

    return result


def draw(l: list) -> int:
    """
    Render the CRT image
    """
    
    x_values = [1]

    for i in l:
        if i=="noop":
            x_values.append(x_values[-1])
        else:
            value = int(i[5:])
            x_values.append(x_values[-1])
            x_values.append(x_values[-1] + value)


    outpufile = open('Day-10/output.txt',"w")
    output = []

    for i in range(6):
        for j in range(40):

            if x_values[i*40+j] - 1 <= j <= x_values[i*40+j] + 1:
                output.append("#")
            else:
                output.append(".")


        output.append("\n")


    outpufile.writelines(output)
    outpufile.close()

    return


print(draw(L))

