# part 1
with open('day10.txt','r') as f:
    f = [0] + [int(x) for x in f.read().split('\n')]
    f.append(max(f)+3)
    f.sort()
cnt_1 = [i for i in range(len(f)-1) if f[i+1] == (f[i]+1)]
cnt_3= [i for i in range(len(f)-1) if f[i+1] == (f[i]+3)]
print(len(cnt_3)*len(cnt_1))

# part 2
l = [1] + [0]*(len(f)-1)
for i in range(1,len(f)):
    l[i] = sum((l[j] for j in range(i-3,i) if f[i] <= (f[j]+3)))
print(l[-1])