def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n -1)
e = 0
i = 0
while(True):
    before = e
    e += 1 / factorial(i) 
    i += 1
    if before - e < 1e-100 and e - before < 1e-100:
        break
print(e)