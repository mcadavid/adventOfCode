import numpy as np
import queue

f = open("input")

#x = list(map(str.splitlines, open('input').read().strip().split("\n\n")))
#print(np.array(x))

x = list(map(str.splitlines, open('input').read().strip().split("\n\n")))


def f(x, y):
    if type(x) == int:
        if type(y) == int:
            return x - y
        else:
            return f([x], y)
    else:
        if type(y) == int:
            return f(x, [y])

    for a, b in zip(x, y):
        v = f(a, b)
        print(v)
        if v != 0:
            print("returning")
            return v

    return len(x) - len(y)


t = 0

for i, (a, b) in enumerate(x):
    if f(eval(a), eval(b)) < 0:
        t += i + 1

print(t)


def compare(s1, s2):
    for i in range(max(len(s1)), max(len(s2))):
        print("comp")


# OFFSET = 48
# q = queue.Queue()
# print(ord('9') - OFFSET, 9)
# lines = f.readlines()
# i = 0
# count = 0
# print(lines)
# while i < len(lines):
#     if lines[i] == '\n':
#         i += 1
#         continue
#     l1 = lines[i][:-1]
#     l2 = lines[i+1][:-1]
#     if (compare(l1,l2)):
#         count += 1
#     i += 2
#     print(l1,l2)
