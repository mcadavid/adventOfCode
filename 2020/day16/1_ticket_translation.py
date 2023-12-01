f = open('input1', 'r')
s = set()
summe = 0
n_ticket = False
my_ticket = False
for line in f:
    line = line[:-1]
    print(line)
    if len(line) == 0:
        continue
    if line == 'your ticket:':
        my_ticket = True
    elif line == 'nearby tickets:':
        n_ticket = True
    elif not (my_ticket or n_ticket):
        c, rg = line.split(": ")
        r1, r2 = rg.split(' or ')
        r11, r12 = map(int, r1.split("-"))
        r21, r22 = map(int, r2.split("-"))
        for i in range(r11, r12 + 1):
            s.add(i)
        for i in range(r21, r22 + 1):
            s.add(i)
    elif my_ticket:
        my_ticket = False
    elif n_ticket:
        l = list(map(int, line.split(',')))
        for n in l:
            if not n in s:
                summe += n


print(summe)
