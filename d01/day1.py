import numpy as np

# part 1
with open("day1.txt", "r") as f:
    data = f.readlines()
    inputs = np.array([int(x) for x in data])

tot = inputs[:,None] + inputs[None,:]
idx = np.argwhere(tot == 2020)[0]
print(inputs[idx[0]]*inputs[idx[1]])

# part 2
tot2 = tot[:,:,None]+ inputs[None,:]
idx = np.argwhere(tot2 == 2020)[0]
print(inputs[idx[0]]*inputs[idx[1]]*inputs[idx[2]])


