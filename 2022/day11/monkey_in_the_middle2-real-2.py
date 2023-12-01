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

MONKEYS_NR = 8
monkeys = [None] * MONKEYS_NR
monkeys[0] = Monkey([57, 58], 7, 2, 3, lambda x: (x * 19))
monkeys[1] = Monkey([66, 52, 59, 79, 94, 73], 19, 4, 6, lambda x: (x + 1))
monkeys[2] = Monkey([80], 5, 7, 5, lambda x: x+6)
monkeys[3] = Monkey([82, 81, 68, 66, 71, 83, 75, 97], 11, 5, 2, lambda x: (x + 5))
monkeys[4] = Monkey([55, 52, 67, 70, 69, 94, 90], 17, 0, 3, lambda x: (x * x))
monkeys[5] = Monkey([69, 85, 89, 91], 13, 1, 7, lambda x: (x + 7))
monkeys[6] = Monkey([75, 53, 73, 52, 75], 2, 0, 4, lambda x: (x * 7))
monkeys[7] = Monkey([94, 60, 79], 3, 1, 6, lambda x: (x + 2))


mod = 1
for m in monkeys:
    mod *= m.div_test

print(monkeys)
absolute_counter = 0
def process_monkey(m):
    global absolute_counter
    for item in m.items:
        m.count += 1
        absolute_counter += 1
        item = m.op(item)
        # print("before", item)
        item %= mod
        # print("after", item)
        if item == 0:
            print("ERROR ..................")
        if item % m.div_test == 0:
            monkeys[m.true_monkey].items.append(item)
        else:
            monkeys[m.false_monkey].items.append(item)
        # print(item, end='::')
    # print()
    #print("True monkey :", m.true_monkey, monkeys[m.true_monkey].items)
    #print("False monkey :", m.false_monkey, monkeys[m.false_monkey].items)
    m.items = []

print_monkeys()
for r in range(10000):
    # print("************************************")
    # print('round', r, ':')
    for i in range(MONKEYS_NR):
        # print('Monkey', i, ':')
        process_monkey(monkeys[i])
    # print_monkeys()
    #if r == 1: break

counts = []
for m in monkeys:
    counts.append(m.count)

print_monkeys()
counts = sorted(counts)
print(counts, sum(counts), absolute_counter)
print(counts[-1] * counts[-2])


