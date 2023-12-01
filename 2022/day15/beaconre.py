import re

pattern = re.compile(r"-?\d+")

lines = [list(map(int, pattern.findall(line))) for line in open('input')]

M = 4000000
M=20

def merge(intervals):
    if len(intervals) == 0 or len(intervals) == 1:
        return intervals
    intervals.sort(key=lambda x:x[0])
    result = [[intervals[0][0], intervals[0][1]]]
    for interval in intervals[1:]:
        if interval[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            result.append(interval)
    return result

for Y in range(M + 1):
    intervals = []

    for sx, sy, bx, by in lines:
        d = abs(sx - bx) + abs(sy - by)
        o = d - abs(sy - Y)

        if o < 0:
            continue

        lx = sx - o
        hx = sx + o

        intervals.append((lx, hx))

    intervals.sort()

    q = []
    print(Y, intervals)
    for lo, hi in intervals:

        if not q:
            q.append([lo, hi])
            continue

        qlo, qhi = q[-1]
        #print(q)
        # print("qlo and qhi2", qlo, qhi)
        if lo > qhi + 1:
            q.append([lo, hi])
            continue

        q[-1][1] = max(qhi, hi)

    x = 0
    print(q)
    #joined intervals
    # for lo, hi in q:
    #     if x < lo:
    #         print(x * 4000000 + Y)
    #         exit(0)
    #     x = max(x, hi + 1)
    #     if x > M:
    #         break
#56000011
