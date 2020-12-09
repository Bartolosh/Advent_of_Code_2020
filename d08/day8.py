def process(instructions):
    acc,idx = 0,0
    idx_list = []
    for _ in range(len(instructions)):
        if idx == len(instructions):
            return acc,idx
        if idx in idx_list:
            break
        op, val = instructions[idx].split(' ')[0], int(instructions[idx].split(' ')[1])
        idx_list.append(idx)
        if op == 'acc':
            acc += val
        if op == 'jmp':
            idx += val
            continue
        idx += 1
    return acc,idx

# part 1
instructions = [op for op in open('day8.txt','r').read().strip().split('\n')]

print(process(instructions)[0])

# part 2

idx_list =[]
stop = False
while not stop:
    for i in range(len(instructions)):
        ins_cpy = instructions.copy()
        op,val = ins_cpy[i].split(' ')[0],ins_cpy[i].split(' ')[1]
        if (op == 'nop') and (i not in idx_list):
            idx_list.append(i)
            ins_cpy[i] = 'jmp '+val
        if (op == 'jmp') and (i not in idx_list):
            idx_list.append(i)
            ins_cpy[i] = 'nop '+val
        acc,idx = process(ins_cpy)
        if idx == len(instructions):
            print(acc)
            stop = True