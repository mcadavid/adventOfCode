from itertools import combinations

f = open('input_init.txt')
range_l = 200000000000000
range_r = 400000000000000
# range_l = 7
# range_r = 27

lines = []

for line in f:
    line = line.strip()
    pos, velocity = line.split('@')
    lines.append((list(map(int, pos.split(','))), list(map(int, velocity.split(',')))))




# print(lines)
result = 0

candidates = set()

def check_for_otherlines(x,y,z,dx,dy,dz):
    count = 0
    found = False
    for [x1, y1, z1], [vx1, vy1, vz1] in lines[1:]:
        if x != x1 and dx != vx1 and (x - x1) % (vx1 - dx) != 0:
            break
        if y != y1 and dy != vy1 and (y - y1) % (vy1 - dy) != 0:
            break
        if z != z1 and dz != vz1 and (z - z1) % (vz1 - dz) != 0:
            break
        
        if vx1 - dx != 0 and (vy1 - dy) != 0 and (vz1 - dz) != 0:
            t1 = (x - x1) // (vx1 - dx)
            t2 = (y - y1) // (vy1 - dy)
            t3 = (z - z1) // (vz1 - dz)
            
                          
            if t1 == t2 and t2 == t3:
                count += 1
            if count == len(lines) - 1:
                candidates.add(((x,y,z),(dx,dy,dz)))
                print((x,y,z),(dx,dy,dz), t1, t2, t3)
                found = True
    return found
       
rx = 557301378477177
rx_min = 2134756155381
rdx_min = -810
rdx = 605
count = 0
for x in range(rx_min, rx):
    for dx in range(rdx_min, rdx):
        count += 1
        [x1, y1, z1], [vx1, vy1, vz1] = lines[0]  
        if x != x1 and dx != vx1 and (x - x1) % (vx1 - dx) != 0:
            continue
        elif x != x1 and dx != vx1:
            t = (x - x1) // (vx1 - dx)
            if t < 0: 
                continue
            for y in range(rx_min, rx):
                for dy in range(rdx_min, rdx):
                    if y - y1 == t * (vy1 - dy):
                        for z in range(rx_min, rx):
                            for dz in range(rdx_min, rdx):
                                if z - z1 == t * (vz1 - dz):
                                    print(count, found, "checking for", (x,y,z),(dx,dy,dz))
                                    found = check_for_otherlines(x,y,z,dx,dy,dz)
                                    if found:
                                        print(candidates)
                                        exit(0)




print(candidates)



# Hailstone: 19, 13, 30 @ -2, 1, -2
# Collision time: 5
# Collision position: 9, 18, 20

# Hailstone: 18, 19, 22 @ -1, -1, -2
# Collision time: 3
# Collision position: 15, 16, 16

# Hailstone: 20, 25, 34 @ -2, -2, -4
# Collision time: 4
# Collision position: 12, 17, 18

# Hailstone: 12, 31, 28 @ -1, -2, -1
# Collision time: 6
# Collision position: 6, 19, 22

# Hailstone: 20, 19, 15 @ 1, -5, -3
# Collision time: 1
# Collision position: 21, 14, 12