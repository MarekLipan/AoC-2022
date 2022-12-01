import heapq

# read the input into a list
file = open('Day-1\day1_input1.txt', 'r')
L = file.read().splitlines()

def most_calories(l: list, x: int) -> int:
    """
    Outputs the total of calories carried by x elves carrying most calories
    """

    sum_calories = []
    single_elf_calories = 0

    for i in l:

        if i == "":
            sum_calories.append(single_elf_calories)
            single_elf_calories = 0
        else:
            single_elf_calories += int(i)

    heapq._heapify_max(sum_calories)

    top_x_sum = 0
    for i in range(x):
        top_x_sum += heapq._heappop_max(sum_calories)

    return top_x_sum

print(most_calories(L, x=1))
print(most_calories(L, x=3))






    
    

