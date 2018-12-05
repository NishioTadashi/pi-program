#delta = input("Please Input Allowable Error: ")
#delta = float(delta)
i = 0
pi = 0
delta = 1e-300
while True:
    before = pi
    pi += (4 / (8 * i + 1) - 2 / (8 * i + 4) - 1 / (8 * i + 5) - 1 / (8 * i + 6)) / ( 2 ** (4 * i))
    if before - pi < delta and pi - before < delta:
        break
    i += 1
print(pi)
