f = open("input")

all_jolts = []
for line in f:
    all_jolts.append(int(line))

all_jolts = sorted(all_jolts)
all_jolts.append(all_jolts[-1] + 3)
n = len(all_jolts)
first = all_jolts[0]
ones = 0
threes = 0
if first == 1:
    ones += 1
elif first == 3:
    threes += 1
for i in range(1, n):
    diff = all_jolts[i] - all_jolts[i - 1]
    if diff == 1:
        ones += 1
    elif diff == 3:
        threes += 1


print(ones * threes)
