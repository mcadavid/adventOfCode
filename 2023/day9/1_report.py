history = open('input.txt').read().split('\n')
result = 0
for line in history:
    h = list(map(int, line.split()))
    last = []
    while h.count(0) != len(h):
        last.append(h[-1])
        h = [x - y for x, y in zip(h[1:], h[:-1])]
        # print(h)
    print(h)
    result += sum(last)
    print(last, result)

print(result)
