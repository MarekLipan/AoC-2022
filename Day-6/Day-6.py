# read the input into a list
file = open('Day-6/day6_input1.txt', 'r')
L = file.read().splitlines()

def find_unique(l: list, n) -> int:
    """
    Returns the index after which the first n unique consecutive numbers are obtained in the sequence.
    """

    text = l[0]

    window = {}

    k = n

    for i in text[:n]:
        window[i] = 1 + window.get(i, 0)

    while len(window.keys()) < n:
        # add at the end
        window[text[k]] = 1 + window.get(text[k], 0)

        # remove at the beginning
        if window[text[k-n]] > 1:
            window[text[k-n]] -= 1
        else:
            window.pop(text[k-n])

        k += 1

    return k

print(find_unique(L, 4))
print(find_unique(L, 14))






    
    

