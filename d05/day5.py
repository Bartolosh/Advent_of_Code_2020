import numpy as np
import math as mt

#part 1

def compute_seat(line):
    seat_row = [0,127]
    seat_col = [0,7]
    for c in range(len(line)):
        if c < 7:
            offset = mt.ceil((seat_row[1] - seat_row[0]) / 2)
            if line[c] == 'F':
                seat_row[1] -= offset
            if line[c] == 'B':
                seat_row[0] += offset
        else:
            offset = mt.ceil((seat_col[1] - seat_col[0]) / 2)
            if line[c] == 'L':
                seat_col[1] -= offset
            if line[c] == 'R':
                seat_col[0] += offset

    return seat_row[0]*8+seat_col[0],[seat_row[0],seat_col[0]]

with open('day5.txt','r') as f:
    l_val = []
    l_seat = []
    for line in f.readlines():
        line = line.rstrip()
        val,seat = compute_seat(line)
        l_val.append(val)
        l_seat.append(seat)
    f.close()
    print(max(l_val))

# part 2

airplane = np.zeros((127,8))
for seat in l_seat:
    airplane[seat[0],seat[1]] = 1

my_seat_id = [r*8+c for [r,c] in np.argwhere(airplane == 0) if airplane[r,c-1]==1 and airplane[r,c+1]==1].pop()
print(my_seat_id)