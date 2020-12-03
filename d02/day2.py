# part 1
with open('day2.txt', 'r') as f:
    data = [x.strip('\n') for x in f.readlines()]

count = 0
for entry in data:
    lowbound = int(entry.split('-')[0])
    upperbound = int(entry.split('-')[1].split(' ')[0])
    lett = entry.split(':')[0].split(' ')[1]
    psw = [x for x in entry.split(':')[1].split(' ')[1]]
    if psw.count(lett) <= upperbound and psw.count(lett) >= lowbound:
        count += 1

print(count)

# part 2
count2 = 0
for entry in data:
    lowbound = int(entry.split('-')[0])
    upperbound = int(entry.split('-')[1].split(' ')[0])
    lett = entry.split(':')[0].split(' ')[1]
    psw = [x for x in entry.split(':')[1].split(' ')[1]]
    if (psw[lowbound-1] == lett and psw[upperbound-1] != lett) or (psw[lowbound-1] != lett and psw[upperbound-1] == lett) :
        count2 += 1

print(count2)