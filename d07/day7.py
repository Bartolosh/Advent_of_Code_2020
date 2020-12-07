def get_input(line):
    line = line.strip()[:-1].replace(" bags", "").replace(" bag", "").split(" contain ")
    line[1] = line[1].split(", ")

    for i, bag in enumerate(line[1]):
        if bag != "no other":
            line[1][i] = bag.split(" ", 1)
            line[1][i][0] = int(line[1][i][0])
        else:
            line[1] = None

    return line

with open("day7.txt") as f:
    inputs = [get_input(line) for line in f.readlines()]

# part 1
contained = {}
for bag,contains in inputs:
    if contains is not None:
        for x,y in contains:
            try:
                contained[y].append(bag)
            except KeyError:
                contained[y] = [bag]
answer = set()
queue = ['shiny gold']

while queue != []:
    try:
        answer.add(queue[0])
        queue += contained[queue[0]]
    except KeyError:
        pass
    finally:
        del(queue[0])
print(len(answer)-1)

# part 2

bags = {key: value for key, value in inputs}
l = [("shiny gold", 1)]
answer = 0

while l != []:
    try:
        for bag in bags[l[0][0]]:
            answer += bag[0] * l[0][1]
            l.append((bag[1], bag[0] * l[0][1]))
    except TypeError:
        pass
    finally:
        del l[0]

print(answer)