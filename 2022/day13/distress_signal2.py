import numpy as np
import queue

f = open("input")

#x = list(map(str.splitlines, open('input').read().strip().split("\n\n")))
#print(np.array(x))

array = list(map(eval, open('input.txt').read().split()))



def compare(x, y):
    if type(x) == int:
        if type(y) == int:
            return x - y
        else:
            return compare([x], y)
    else:
        if type(y) == int:
            return compare(x, [y])

    for a, b in zip(x, y):
        v = compare(a, b)
        if v:
            return v

    return len(x) - len(y)

i1 = 1
i2 = 2

for e in array:
    if compare(e,[[2]]) < 0:
        i1 += 1
        i2 += 1
    elif compare(e, [[6]]) < 0:
        i2 += 1

print(i1, i2, i1*i2)

