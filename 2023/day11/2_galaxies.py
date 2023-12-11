import re
import itertools

lines = open('input.txt', 'r').read().split('\n')

RESIZE = 1000000

gaps = []
galaxies = []
for line in lines:
    line = line.strip()
    g_list = [x.start() for x in re.finditer('#', line)]
    gaps += g_list

gaps = [x for x in range(len(line)) if x not in gaps]
for g in gaps:
    lines = [line[:g]+ 'a' + line[g+1:] for line in lines]

print(gaps)

lines2 = list(lines)
lines2 = [line.replace('a', 'X'*RESIZE)for line in lines2]


i = 0
for line in lines2:
    js = [(i, j.start()) for j in re.finditer('#', line)]
    if len(js) == 0:
        i += (RESIZE - 1)
    else:
        galaxies += js
    i += 1


sum = 0
list_of_pairs = list(itertools.combinations(galaxies, 2))
for (i1, j1), (i2, j2) in list_of_pairs:
    sum += abs(i2-i1) + abs(j2-j1)

print(sum)
