import re

f = open("input.txt", 'r')

def getAdjacent(i, j, number_positions):
    count = 0
    nums = []
    for number in number_positions:
        if number[0] - 1 <= j <= number[1]:
            nums.append(number)
            count += 1
        if count > 2:
            break

    if count != 2:
        return None, None

    return nums[0], nums[1]


sum = 0
engine = []
n_positions = []
count = 0
gears = []
for line in f:
    line = line.strip()
    engine.append(line)
    n_positions.append([(m.start(), m.end(), int(m.group())) for m in re.finditer(r'\d+', line)])
    gears += [(count, m.start()) for m in re.finditer(r'\*', line)]
    count += 1

print(len(gears), " gears")
# print("number_positions", n_positions)
print("numbers", len(n_positions))

for g in gears:
    i = g[0]
    # list of numbers
    number_positions = n_positions[i] + n_positions[i - 1] + n_positions[i + 1]
    p, q = getAdjacent(i, g[1], number_positions)
    if p is not None and q is not None:
        sum += p[2] * q[2]

print(sum)
