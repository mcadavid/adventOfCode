import random
import pylab
import cmath
from itertools import groupby

pts = [(random.randrange(-5, 5), random.randrange(-5, 5)) for _ in range(10)]

# for this problem complex numbers are just too good to pass up
pts = [(1, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (14, 0), (0, 1), (1, 1), (5, 1), (6, 1), (8, 1), (9, 1),
       (10, 1), (11, 1), (12, 1), (15, 1), (16, 1), (0, 2), (1, 2), (5, 2), (9, 2), (11, 2), (12, 2), (13, 2), (14, 2),
       (15, 2), (2, 3), (8, 3), (12, 3), (13, 3), (14, 3), (2, 4), (4, 4), (10, 4), (15, 4), (16, 4)]

z_pts = [i[0] + 1j * i[1] for i in pts if i != (0, 0)]

z_pts.sort(key=lambda x: abs(x))

gpts = [[*g] for _, g in groupby(z_pts, key=lambda x: abs(x))]
print(*gpts, sep='\n')

spts = [1j / 2]

for e in gpts:
    if len(e) > 1:
        se = sorted(e, key=lambda x: cmath.phase(-x / spts[-1]))
        spts += se
    else:
        spts += e

print(spts)
