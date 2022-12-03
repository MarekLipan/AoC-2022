# read the input into a list
file = open('Day-3/day3_input1.txt', 'r')
L = file.read().splitlines()

def priorities_sum(l: list) -> int:
    """
    Computes the sum of priorities of letter that is the same in both halves of string
    """

    total_priority_sum = 0

    for i in l:
        half_len = int(len(i)/2)
        a = set(i[:half_len])
        b = set(i[half_len:])
        inter = a.intersection(b).pop()

        if inter.islower():
            total_priority_sum += ord(inter) - ord("a") + 1
        else:
            total_priority_sum += ord(inter) - ord("A") + 27

    return total_priority_sum


print(priorities_sum(L))







    
    

