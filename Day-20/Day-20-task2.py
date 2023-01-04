import math

# read the input into a list
file = open('Day-20/input.txt', 'r')
L = file.read().splitlines()

numbers = []
for l in L:
    numbers.append(int(l) * 811589153)

orig2mix = {}
mix2orig = {}

N = len(numbers)
for n in range(N):
    orig2mix[n] = n
    mix2orig[n] = n

for r in range(10):
    for i in range(N):
        current_index = orig2mix[i]
        proposal_index = current_index + numbers[i]
        if proposal_index >= N:
            while proposal_index >= N:
                new_index = (proposal_index % (N-1))# + int(proposal_index/(N-1))
                proposal_index = new_index
        elif proposal_index < 0:
            while proposal_index < 0:
                new_index = (proposal_index % (N-1)) # + int(proposal_index/(N-1)) - 1
                proposal_index = new_index
        #elif proposal_index == 0:
        #    new_index = N - 1
        else:
            new_index = proposal_index

        if new_index > current_index:
            for j in range(current_index, new_index):
                mix2orig[j] = mix2orig[j+1]
                orig2mix[mix2orig[j]] = j
            mix2orig[new_index] = i
            orig2mix[i] = new_index

        elif new_index < current_index:
            for j in range(current_index, new_index, -1):
                mix2orig[j] = mix2orig[j-1]
                orig2mix[mix2orig[j]] = j
            mix2orig[new_index] = i
            orig2mix[i] = new_index

zero_pos = orig2mix[numbers.index(0)]
print(
    f"Result to task 2: {numbers[mix2orig[(zero_pos + 1000) % N]] + numbers[mix2orig[(zero_pos + 2000) % N]] + numbers[mix2orig[(zero_pos + 3000) % N]]}"
)

