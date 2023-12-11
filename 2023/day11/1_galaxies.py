import re
import itertools

lines = open('input.txt', 'r').read().split('\n')

gaps = []
galaxies = []
i = 0
for line in lines:
    line = line.strip()
    g_list = [x.start() for x in re.finditer('#', line)]
    gaps += g_list

gaps = [x for x in range(len(line)) if x not in gaps]

lines2 = list(lines)
count = 0
for g in gaps:
    g += count
    lines2 = [line[:g]+ '.' + line[g:] for line in lines2]
    count += 1

for line in lines2:
    js = [(i, j.start()) for j in re.finditer('#', line)]
    if len(js) == 0:
        i += 1
    else:
        galaxies += js
    i += 1

sum = 0
list_of_pairs = list(itertools.combinations(galaxies, 2))
for (i1, j1), (i2, j2) in list_of_pairs:
    sum += abs(i2-i1) + abs(j2-j1)

print(sum)
