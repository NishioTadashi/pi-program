delta = input("Please Input Allowable Error: ")
delta = float(delta)
sqrpi = 0
i = 1
while True:
    before = sqrpi 
    sqrpi += 6 / (i * i)
    if(before - sqrpi < delta and sqrpi - before < delta):
        break
    i +=1
pi = sqrpi
while True:
    before = pi
    pi = pi - ((pi) * (pi) - sqrpi) / (2 * (pi))
    if(pi - before < delta and before - pi < delta ):
        break
print(pi)    
