

class Command:
    def __init__(self, number, start, end):
        self.number = number
        self.start = start
        self.end = end

    def exec(self):
        tmp = []
        for i in range(self.number):
            tmp.append(self.start.pop())

        for i in range(self.number):
            self.end.append(tmp.pop())


def reverse(sts):
    for col in sts:
        col.reverse()


no_stacks = 9
with open("input") as f:
    lines = f.readlines()

stacks = [[] for j in range(no_stacks)]
print(stacks)

done = False
reversed = False
for line in lines:
    line = line[:-1]
    if not done:
        i = 1
        j = 0
        while i <= len(line):
            value = line[i]
            if value == '1':
                done = True
                break
            if value != ' ':
                stacks[j].append(value)
            i += 4
            j += 1
    if (done and not reversed):
        reverse(stacks)
        reversed = True
    if line.startswith("move"):
        print(line)
        _,a,_,b,_,c = line.split()
        a, b, c = int(a), int(b), int(c)
        # print(a, b, c)
        Command(a,stacks[b-1], stacks[c-1]).exec()
    print(stacks)

result = ''
stacks.append([])
for s in stacks:
    if  len(s) > 0:
        result += s.pop()

print(result)






