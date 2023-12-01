import sys


class Monkey:
    def __init__(self, items, div_test, true_monkey, false_monkey, op):
        self.items = items
        self.div_test = div_test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.op = op
        self.count = 0

    def print(self):
        return str(self.items) + ", c = " + str(self.count)

LOG = True
def print_monkeys():
    if not LOG: return
    print("************************************")
    for i in range(MONKEYS_NR):
        print("Monkey", i, "->", monkeys[i].print())

MONKEYS_NR = 4
monkeys = [None] * 4
monkeys[0] = Monkey([79,98], 23, 2, 3, lambda x: x * 19)
monkeys[1] = Monkey([54, 65, 75, 74], 19, 2, 0, lambda x: x + 6)
monkeys[2] = Monkey([79,60,97], 13, 1, 3, lambda x: x * x)
monkeys[3] = Monkey([74], 17, 0, 1, lambda x: x + 3)

print(monkeys)

def process_monkey(m):
    for item in m.items:
        m.count += 1
        item_orig = item
        item = m.op(item) // 3
        if  item == 0 or item > sys.maxsize:
            print("hello too big", item, '----')
            print(item + 1,'-----')
        if item % m.div_test == 0:
            print(item_orig, '->', item, m.true_monkey)
            monkeys[m.true_monkey].items.append(item)
        else:
            print(item_orig, '->', item, m.false_monkey)
            monkeys[m.false_monkey].items.append(item)
    m.items = []

print_monkeys()
for r in range(25):
    for i in range(MONKEYS_NR):
        print("Monkey ", i)
        process_monkey(monkeys[i])
        print_monkeys()

print_monkeys()
counts = []
for m in monkeys:
    counts.append(m.count)

print(counts)

counts = sorted(counts)
print(counts[-1] * counts[-2])


