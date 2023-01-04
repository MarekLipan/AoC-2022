# read the input into a list
file = open('Day-25/input.txt', 'r')
L = file.read().splitlines()

snafu_numbers = []
for l in L:
    snafu_numbers.append(l)

figure_mapping = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2
}

figure_back_mapping = {
    2: "2",
    1: "1",
    0: "0",
    4: "-",
    3: "="
}

def snafu2decimal(n: str) -> int:
    n = n[::-1]
    
    additions = []
    for i, f in enumerate(n):
        additions.append(figure_mapping[f]*5**i)
    n_decimal = sum(additions)

    return n_decimal

def decimal2snafu(n: int) -> str:
    n_snafu = []

    while n > 0:
        remainder = n % 5
        n = int(n / 5)

        n_snafu.append(figure_back_mapping[remainder])

        if figure_back_mapping[remainder] == "-" or figure_back_mapping[remainder] == "=":
            n += 1

    n_snafu.reverse()

    n_snafu = "".join(n_snafu)

    return n_snafu


total = 0
for n in snafu_numbers:
    total += snafu2decimal(n)


print(f"Result: {decimal2snafu(total)}")

