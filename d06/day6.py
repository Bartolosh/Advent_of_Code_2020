# part 1
with open('day6.txt','r') as f:
    f = f.read().split('\n\n')
print(sum([len(set(x.replace('\n',''))) for x in f]))

# part 2
import functools
with open('day6.txt','r') as f:
    f = f.read().split('\n\n')
    answers = [[set(i) for i in x.split('\n')] for x in f]
    print(sum([len(functools.reduce(lambda x,y: x.intersection(y),i)) for i in answers]))
