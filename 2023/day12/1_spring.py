import re
import itertools
f = open("input_init.txt", 'r')
count = 0

def findAll(line, report):
    groups = re.split('\s', line.replace('.', ' '))
    values = [len(member) for member in groups if len(member) > 0]
    return report == values


result = 0
result2 = 0
for line in f:
    line = line.strip()
    line, report = line.split()
    report  = list(map(int, report.split(',')))
    #print("Line: ", line, "Report:" ,report)
    unknowns = set([j.start() for j in re.finditer('\?', line)])
    #print("Unknowns Positions: ", unknowns)
    if len(unknowns) == 0:
        continue
    old_line = line
    number_of_damaged = sum(report)
    for k in range(len(unknowns) + 1):
        for damaged in itertools.combinations(unknowns, k):
            oks = unknowns - set(damaged)

            #print("Damaged: ", damaged, "Oks:", oks, "unknowns:", unknowns)

            new_line = list(line)
            for i in range(len(line)):
                if i in oks:
                    new_line[i] = '.'
                elif i in damaged:
                    new_line[i] = '#'
            # print(old_line)
            line = ''.join(new_line)
            #print(line)
        
            if line.count('#') == number_of_damaged and findAll(''.join(new_line), report):
                result2 += 1
                if count % 50 == 0:
                    print(line, report)
            #print(report)

    count += 1
    if count == -1:
        break
# Damaged:  {8, 10, 12} Oks: {0, 2, 4, 6, 14}

print(result2)
line = '.?.?#.#???#????'
report = [1,1,1,4]


