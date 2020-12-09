import numpy as np

def check(n,l):
    tot = l[:,None] + l[None,:]
    return True if n in tot else False

def find(target,n,l):
    for i in range(len(l)):
        if target == sum(np.array(l[i:n+i])):
            return max(l[i:i+n])+min(l[i:i+n])
    return False

# part 1

with open('day9.txt','r') as f:
    f = [int(x) for x in f.read().split('\n')]

for i in range(25,len(f)):
    if not check(f[i],np.array(f[i-25:i])):
        n = f[i]
        print(n)

# part 2

for i in range(2,len(f)):
    weakness = find(n,i,f)
    if weakness:
        print(weakness)
        break