import re

f = open("input.txt", 'r')
#special_symbols = '+"*%&/=?@#§$-'

def isSymbolNearby(i, j_start, j_end, engine):
    # print(i, j_start, j_end)
    for k in [-1, 0, 1]:
        for l in range(j_start - 1, j_end + 1):
            if i + k < 0 or i + k >= n or l < 0 or l >= m:
                continue
            if engine[i + k][l] in special_symbols:
                return True

    return False


sum = 0
engine = []
n_positions = []
count = 0
special_symbols = ''
for line in f:
    line = line.strip()
    engine.append(line)
    n_positions += [(count, m.start(), m.end(), m.group()) for m in re.finditer(r'\d+', line)]
    count += 1
    special_symbols += re.sub(r'[0-9]+', '', line.replace('.',''))

print("symbols", special_symbols)

    
n = len(engine)
m = len(engine[0])
print("size of engine", n, m)
print("numbers", len(n_positions))

for i in range(len(n_positions)):
    p = n_positions[i]
    # print(p)
    if isSymbolNearby(p[0], p[1], p[2], engine):
        sum += int(p[3])

print(sum)
