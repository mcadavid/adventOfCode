import numpy as np

gas = []
for line in open('input'):
    gas = list(line)

gas = [1 if g == '>' else -1 for g in gas]
# width, height
rocks = range(5)
tower_height = 0
current_height = 0


def get_start(rock, s, g):
    if rock == 0:
        if g == 1 and s + 4 < 7:
            return s + 1
        elif g == -1 and s - 1 >= 0:
            return s - 1
    elif rock == 3:
        if g == 1 and s + 1 < 7:
            return s + 1
        elif g == -1 and s - 1 >= 0:
            return s - 1
    elif rock == 4:
        if g == 1 and s + 2 < 7:
            return s + 1
        elif g == -1 and s - 1 >= 0:
            return s - 1
    return s


def down(r, s):
    if current_height == END - 1:
        return False
    if r == 0:
        for i in range(4):
            if cave[current_height + 1, s + i] > 0:
                return False
    elif r == 3:
        if current_height + 4 >= END:
            return False
        if cave[current_height + 4, s] > 0:
            return False
    elif r == 4:
        if current_height + 2 >= END:
            return False
        if cave[current_height + 2,s] > 0 and cave[current_height + 2, s + 1] > 0:
            return False

    return True


def blown(r, s, g):
    if r == 0:
        if g == 1:
            if s + 4 + g > 7:
                return False
            if cave[current_height, s + 3 + g] > 0:
                return False
        elif g == -1:
            if s + g < 0:
                return False
            if cave[current_height, s + g] > 0:
                return False
    elif r == 3:
        if g == 1:
            if s + g >= 7:
                return False
            for i in range(4):
                if cave[current_height + i, s + g] > 0:
                    return False
        elif g == -1:
            if s + g < 0:
                return False
            for i in range(4):
                if cave[current_height + i, s + g] > 0:
                    return False
    elif r == 4:
        if g == 1:
            if s + g + 2 > 7:
                return False
            if cave[current_height, s + 2] > 0 or cave[current_height + 1, s + 2] > 0:
                return False
        if g == -1:
            if s - 1 < 0:
                return False
            if cave[current_height, s - 1] > 0 or cave[current_height + 1, s - 1] > 0:
                return False

    else:
        return False

    return True


END = 100
ROCKS = 15
g_i = 0
print("len of gas", len(gas))
count = 1
cave = np.array([[0 for _ in range(7)] for _ in range(END)])
for r_nr in range(ROCKS):
    rock = rocks[r_nr % 5]
    start = 1

    done = False
    current_height = 0
    g = gas[0]
    while True:
        # if count == 7 and current_height == 70:
        #     print(cave)
        if rock in (0,3,4):
            g = gas[g_i % len(gas)]
            blown_allowed = blown(rock, start, g)
            # if count == 3:
            #     print("row =", current_height,"blown allowed",blown_allowed,"wind direction", g, "old->", start, "new ->", get_start(rock, start, g))
            if blown_allowed:
                start = get_start(rock, start, g)
            down_allowed = down(rock, start)
            if down_allowed:
                current_height += 1
                g_i += 1
                if count == 9:
                    cave[current_height, start] = -1
                    cave[current_height, start + 1] = -1
                    cave[current_height + 1, start] = -1
                    cave[current_height + 1, start + 1] = -1
            else:
                break
        else:
            break

    print("rock ", rock, "::: current_height", current_height)
    if rock == 0:
        for i in range(4):
            print(current_height, start + i)
            cave[current_height, start + i] = count
        tower_height = max(END - current_height, tower_height)
        count += 1
    elif rock == 3:
        for h in range(4):
            cave[current_height + h, start] = count
        tower_height = max(tower_height, (END - current_height))
        count += 1
    elif rock == 4:
        print(cave)
        cave[current_height, start] = count
        cave[current_height, start + 1] = count
        cave[current_height + 1, start] = count
        cave[current_height + 1, start + 1] = count
        tower_height = max(tower_height, (END - current_height))
        count += 1

        # print(cave)
    # elif rock == 4:
    #     for h in range(2):
    #         cave[current_height - h, start] = 1
    #         cave[current_height, start + h] = 1
    #     tower_height = max(tower_height, (END - current_height) + 2)
    print("Finishing: current height:", current_height, "tower_height:", tower_height)

print(cave)
print(tower_height)
for i in range(END):
    if sum(cave[i])>0:
        print(i, END - i)
        break
