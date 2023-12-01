PREAMBLE = 25
f = open("input2.txt", 'r')

l = []
count = 0
for line in f:
    l.append(int(line))

valids = []
for i in range(PREAMBLE):
    for j in range(PREAMBLE):
        if i != j:
            valids.append(l[i] + l[j])
print(valids)

count = PREAMBLE
other_count = 1
valids_set = set(valids)
invalid = 0
while True:
    if not l[count] in valids_set:
        invalid = l[count]
        break
    valids = []
    for i in range(other_count, other_count + PREAMBLE):
        for j in range(other_count, other_count + PREAMBLE):
            if i != j:
                valids.append(l[i] + l[j])
    # print(count, valids, len(valids))

    valids_set = set(valids)
    count += 1
    other_count += 1

print(invalid)
