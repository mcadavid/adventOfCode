import re


def mask_val(number, m):
    value = str(bin(number)).replace('b', '0')
    value = value.rjust(36, '0')
    value_list = list(value)
    for i in range(len(m)):
        if m[i] != 'X':
            value_list[i] = m[i]
    s = ''
    return int(s.join(value_list), 2)


memory = [0] * 80000
f = open("input", 'r')
mask = ""
for line in f:
    label, eq, val = line.strip().split()
    if label == 'mask':
        mask = val
        continue
    p = re.compile(r'\d+')
    index = int(p.findall(label)[0])
    memory[index] = mask_val(int(val), mask)
    print(index, memory[index])

print(sum(memory))
