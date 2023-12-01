import sys
from functools import reduce
f = open("input1", 'r')

time = 0
bus = []
count = 0
for line in f:
    if count == 0:
        time = int(line)
        count += 1
    else:
        bus = line[0:-1].split(',')


bus = [int(bl) for bl in bus if bl != 'x']
print(bus)

bus_id = 0
dep_time = 0
br = False
for i in range(time, sys.maxsize):
    for b in bus:
        if i % b == 0:
            bus_id = b
            dep_time = i
            br = True
            break
    if br:
        break
print(b, bus_id, (dep_time - time ) * bus_id)




