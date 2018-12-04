delta = input("Please Input Allowable Error: ")
delta = float(delta)
i = 0
pi = 0
while True:
    before = pi
    if i % 2 == 0:
        pi += 4 / (2 * i + 1) 
    else:
        pi -= 4 / (2 * i + 1)
    if before - pi < delta and pi - before < delta:
        break
    i += 1
print(pi)
