import re
import sys
from copy import deepcopy


def mask_val(number, m):
    value = str(bin(number)).replace('b', '0')
    value = value.rjust(36, '0')
    value_list = list(value)
    for i in range(len(m)):
        if m[i] == 'X':
            value_list[i] = 'X'
        elif m[i] == '1':
            value_list[i] = '1'

    indices1 = []
    n = value_list.count('X')
    print(n)
    for i in range(1<<n):
        vals = deepcopy(value_list)
        count = 0
        m2 = str(bin(i)).replace('0b','').rjust(n,'0')
        for k in range(len(vals)):
            if vals[k] == 'X':
                vals[k] = m2[count]
                count += 1
        s = ''
        indices1.append(int(s.join(vals),2))

    return indices1


memory = dict()
f = open("input", 'r')
mask = ""
for line in f:
    label, eq, val = line.strip().split()
    if label == 'mask':
        mask = val
        continue
    p = re.compile(r'\d+')
    index = int(p.findall(label)[0])
    val = int(val)
    indices = mask_val(index, mask)
    print(indices)
    for i in indices:
        memory[i] = val
        print(i, val)


print(sum(memory.values()))
