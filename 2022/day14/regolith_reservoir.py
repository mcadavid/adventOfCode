import  numpy as np
lines = list(open('input.txt').readlines())

def draw(path, sand):
    scenery = np.array([['.' for i in range(15)] for j in range(20)])
    for p in path:
        pos = (p[1], p[0]-490)
        scenery[pos] = '#'
    for g in sand:
        pos = (g[1], g[0]-490)
        scenery[pos] = 'o'
    print(scenery)


print(lines)
rock = set()
for path in lines:
    path =  path[:-1].split('->')
    s = eval(path[0])
    # print(path)
    rock.add(s)
    for i in range(1, len(path)):
        x, y = eval(path[i])
        # print(x,y, s)
        if s[0] < x: # going right
            count = s[0] + 1
            while count <= x:
                rock.add((count,y))
                count += 1
        elif s[0] > x: # going left
            count = s[0] - 1
            while count >= x:
                rock.add((count, y))
                count -= 1
        elif s[1] < y: # going down down is increasing value (problemstellung)
            count = s[1] + 1
            while count <= y:
                rock.add((x, count))
                count += 1
        elif s[1] > y: # going up
            count = s[1] - 1
            while count >= y:
                rock.add((x, count))
                count -= 1
        s = (x, y)

sand = set()
#draw(rock, sand)
print(len(rock))


grain = (500,0)
stop = False
count = 0
step = 0
for _ in range(1000):
    grain = (500, 0)
    stop = False
    step = 0
    while not stop and step < 100:
        step += 1
        down = (grain[0], grain[1] + 1)
        if down not in rock and down not in sand:
            grain = down
            continue
        down_left = (grain[0] - 1, grain[1] + 1)
        if down_left not in rock and down_left not in sand:
            grain = down_left
            continue
        down_right = (grain[0] + 1, grain[1] + 1)
        if down_right not in rock and down_right not in sand:
            grain = down_right
            continue
        if ((grain[0], grain[1] + 1) in rock or (grain[0], grain[1] + 1) in sand) \
                and ((grain[0] - 1 , grain[1] + 1) in rock or (grain[0] - 1, grain[1] + 1) in sand)\
                and ((grain[0] + 1, grain[1] + 1) in rock or (grain[0] + 1, grain[1] + 1) in sand):
            sand.add(grain)
            stop = True

    #draw(rock, sand)

print(sand)
print(len(sand))





