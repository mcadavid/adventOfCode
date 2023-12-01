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
results = [dict() for range in range(MONKEYS_NR)]
modulo = [dict() for  range in range(MONKEYS_NR)]
monkeys = [None] * 4
monkeys[0] = Monkey([79,98], 23, 2, 3, lambda x: x * 19)
monkeys[1] = Monkey([54, 65, 75, 74], 19, 2, 0, lambda x: x + 6)
monkeys[2] = Monkey([79,60,97], 13, 1, 3, lambda x: x * x)
monkeys[3] = Monkey([74], 17, 0, 1, lambda x: x + 3)

print(monkeys)

mod = 1
for m in monkeys:
    mod *= m.div_test

def process_monkey(i):
    m = monkeys[i]
    for item in m.items:
        m.count += 1
        if item in results[i].keys():
            res = results[i][item]
        else:
            res = m.op(item) % mod
            results[i][item] = res

        if res in modulo[i].keys():
            is_div = modulo[i][res]
        else:
            is_div = res % m.div_test == 0
            modulo[i][res] = is_div

        if is_div:
            monkeys[m.true_monkey].items.append(res)
        else:
            monkeys[m.false_monkey].items.append(res)

    m.items = []

for r in range(400):
    for i in range(MONKEYS_NR):
        process_monkey(i)
        # print(results)
        # print(modulo)
    # print_monkeys()

counts = []
for m in monkeys:
    counts.append(m.count)


counts = sorted(counts)
print(counts)
print(counts[-1] * counts[-2])


