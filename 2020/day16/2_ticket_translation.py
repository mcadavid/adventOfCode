f = open('input1', 'r')
all_sets = [set() for i in range(6)]
counter = [[0] * 20 for i in range(6)]
n_ticket = False
my_ticket = False
curr_set = 0
n_rows = 0
for line in f:
    line = line[:-1]
    print(line)
    if len(line) == 0:
        continue
    if line == 'your ticket:':
        my_ticket = True
    elif line == 'nearby tickets:':
        n_ticket = True
    elif not (my_ticket or n_ticket) and curr_set < 6:
        c, rg = line.split(": ")
        if c[0:9] != 'departure':
            continue
        r1, r2 = rg.split(' or ')
        r11, r12 = map(int, r1.split("-"))
        r21, r22 = map(int, r2.split("-"))
        for i in range(r11, r12 + 1):
            all_sets[curr_set].add(i)
        for i in range(r21, r22 + 1):
            all_sets[curr_set].add(i)
        curr_set += 1
    elif my_ticket:
        my_ticket = False
    elif n_ticket:
        l = list(map(int, line.split(',')))
        n_rows += 1
        br = False
        for i in range(6):
            for j in range(20):
                if l[j] in all_sets[i]:
                    counter[i][j] += 1

print("there are n_rows", n_rows)

for i in range(6):
    for j in range(20):
        print(counter[i][j], end='  ')
    print()


for i in range(6):
    for j in range(20):
        if counter[i][j] == 244:
            print(i, j)
    print()




