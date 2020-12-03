import numpy as np

def find_tree(map,step_right,step_down):
    idx_line = idx_depth = count = 0
    while idx_depth < map.shape[0]-1:
        idx_line = (idx_line + step_right) % map.shape[1]
        idx_depth += step_down
        if inputs[idx_depth, idx_line] == '#':
            count += 1
    return count

with open('day3.txt','r') as f:
    tree_map = []
    for line in f.readlines():
         elem = [k for k in line.strip('\n')]
         tree_map.append(elem)

inputs = np.matrix(tree_map)

# part 1

print(find_tree(inputs,3,1))

#part 2

step_right_arr = [1,3,5,7,1]
step_down_arr = [1,1,1,1,2]
prod = 1
for i in range(len(step_right_arr)):
    prod *= find_tree(inputs,step_right_arr[i],step_down_arr[i])

print(prod)

