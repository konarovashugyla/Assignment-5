
def solve(numheads, numlegs):
    chickens= 0
    r = 0
    for rabbits in range(numheads+1):
        while 2*chickens + 4*rabbits != numlegs:
            chickens= numheads- rabbits
            
        if 2*chickens + 4*rabbits == numlegs:
            r = rabbits
            break
    return chickens, r
a, b = 35, 94
print(solve(a, b))