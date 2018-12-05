delta = input("Please Input Allowable Error: ")
delta = float(delta)
i = 2
j = 1
pi = 2
while True:
    before = pi
    pi *= i / j
    if i < j:
        i += 2
    else:
        j += 2
    if before - pi < delta and pi - before < delta:
        break   
print(pi)
