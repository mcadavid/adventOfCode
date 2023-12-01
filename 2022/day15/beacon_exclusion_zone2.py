import sys

f = open("input.txt")

LINE = 10
LINE = 2000000



def read(string):
    sl = string.split()
    return int(sl[-2].strip(',').split('=')[1]), int(sl[-1].strip(',').split('=')[1])

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

sensors = []
for line in f:
    print(line.strip())
    s, b = line.strip().split(':')
    sx, sy = read(s)
    bx, by = read(b)
    sensors.append(((sx,sy), distance((sx,sy), (bx,by))))


def merge(intervals):
    if len(intervals) == 0 or len(intervals) == 1:
        return intervals
    intervals.sort(key=lambda x:x[0])
    res = [[intervals[0][0], intervals[0][1]]]
    for interval in intervals[1:]:
        if interval[0] - 1 <= res[-1][1]: # use the  -1 to merge intervales of the form [a, x-1][x,b] (not real intervals)
            res[-1][1] = max(res[-1][1], interval[1])
        else:
            res.append(interval)
    return res

count = 0
MAX_LINE = 4000000
for y in range(0,MAX_LINE):
    result = []
    for s, r in sensors:
        d = abs(y - s[1])
        # print(s, "r", r, "d", d)
        if d > r:
            # print(s, "does not reach line")
            continue
        diff = r - d
        result.append([s[0] - diff, s[0] + diff])

    result = merge(result)
    #print(result)
    if len(result) > 1:
        tuning_freq = (result[0][1] + 1) * MAX_LINE + y
        print(tuning_freq, (result[0][1] + 1), y)
        break



