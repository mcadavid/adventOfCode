import functools
history = open('input.txt').read().split('\n')
result = 0
for line in history:
    h = list(map(int, line.split()))
    first = []
    while h.count(0) != len(h):
        first.append(h[0])
        h = [x - y for x, y in zip(h[1:], h[:-1])]
        # print(h)

    first.reverse()
    result += functools.reduce(lambda x, y: y - x, first)

    print(first,  result)

print(result)
