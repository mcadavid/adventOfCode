from copy import deepcopy
from time import time
f = open('input.txt')
t = time()

all_bricks = []
for line in f:
    line = line.strip()
    start, end = line.split('~')
    sx, sy, sz = [int(s) for s in start.split(',')]
    ex, ey, ez = [int(s) for s in end.split(',')]
    
    b = []
    if sx == ex and sy == ey:
        for z in range(sz, ez + 1):
            b.append((sx, sy, z))

    elif sx == ex and sz == ez:
        for y in range(sy, ey + 1):
            b.append((sx, y, sz))

    elif sy == ey and sz == ez:
        for x in range(sx, ex + 1):
            b.append((x, sy, sz))
    all_bricks.append(b)
    #print(f"Start: {sx, sy, sz}. End: {ex, ey, ez}", b)

#print(min(z for x, y, z in all_bricks))

# stabilizing
visited = set()
for b in all_bricks:
    for x,y,z in b:
        visited.add((x,y,z))

# print(all_bricks)

while True:
    any_v = False
    for i,b in enumerate(all_bricks):
        still_falling = True
        for (x,y,z) in b:
            if z==1:
                still_falling = False
            if (x,y,z-1) in visited and (x,y,z-1) not in b:
                still_falling = False
        if still_falling:
            any_v = True
            for (x,y,z) in b:
                visited.discard((x,y,z))
                visited.add((x,y,z-1))
            all_bricks[i] = [(x,y,z-1) for (x,y,z) in b]
    if not any_v:
        break

# print(all_bricks)

# # number of bricks

old_visited = deepcopy(visited)
old_all_bricks = deepcopy(all_bricks)

p1 = 0
p2 = 0
# simulate falling without the brick b, for every brick b
for i,b in enumerate(all_bricks):
  visited = deepcopy(old_visited)
  all_bricks = deepcopy(old_all_bricks)
  for b1 in all_bricks:
    for (x,y,z) in b1:
      assert (x,y,z) in visited

  # remove block, check if nothing falls for part 1 (same as ) 
  for (x,y,z) in b:
    visited.discard((x,y,z))
  
  falling_bricks = set()
  while True:
    any_ = False
    for j,b1 in enumerate(all_bricks):
      if j==i:
        continue
      still_falling = True
      for (x,y,z) in b1:
        if z==1:
          still_falling = False
        if (x,y,z-1) in visited and (x,y,z-1) not in b1:
          still_falling = False
      if still_falling:
        falling_bricks.add(j)
        for (x,y,z) in b1:
          assert (x,y,z) in visited
          visited.discard((x,y,z))
          visited.add((x,y,z-1))
        all_bricks[j] = [(x,y,z-1) for (x,y,z) in b1]
        any_ = True
    if not any_:
      break
  if len(falling_bricks)==0:
    p1 += 1
  p2 += len(falling_bricks)
print(p1)
print(p2)
print(time() - t)



