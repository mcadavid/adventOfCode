def contained_in(a, b, c, d):
    if (a >= c and b <= d):
        return True
    if (a <= c and b >= d):
        return True
    return False

def overlap(a, b, c, d):
    if (c < a and d < a) or (c > b and d > b):
        return False
    if (a < c and b < c) or (a > d and b > d):
        return False
    return True


f = open("input.txt", 'r')
count = 0
overlaps = 0
for line in f:
    line = line[0:-1]
    first, second = line.split(',')
    a, b = first.split('-')
    c, d = second.split('-')
    a, b, c, d = int(a), int(b), int(c), int(d)
    if contained_in(a, b, c, d):
        count += 1
    if overlap(a,b,c,d):
        overlaps += 1

print("contained ", count)
print("overlaps ", overlaps)
