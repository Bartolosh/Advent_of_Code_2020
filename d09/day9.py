import numpy as np

def check(n,l):
    tot = l[:,None] + l[None,:]
    return n in tot

# part 1

with open('day9.txt','r') as f:
    f = [int(x) for x in f.read().split('\n')]

for i in range(25,len(f)):
    if not check(f[i],np.array(f[i-25:i])):
        n = f[i]
        print(n)

# part 2
start = 0
end = 1
for i in range(len(f)):
    s = sum(f[start:end])
    start += s > n
    end += s < n
    if s == n:
        print(max(f[start:end]) + min(f[start:end]))
        break
