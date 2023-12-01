def print_tile(tile):
    for line in tile:
        print(line)
    print()


def append(k, v):
    re_k = k[::-1]
    if k in borders.keys():
        borders[k].append(v)
    elif re_k in borders.keys():
        borders[re_k].append(v)
    else:
        borders[k] = [v]


occurs = dict()
f = open("input1", 'r')
tiles = dict()
borders = dict()
current_key = 0
tile = []
first = True
last_line = ''
left = ''
right = ''
for line in f:
    line = line[0:-1]
    if line.startswith("Tile"):
        _, key = line[0:-1].split()
        current_key = int(key)
        occurs[current_key] = 0
    elif len(line) == 0:
        append(last_line, current_key)
        append(left, current_key)
        append(right, current_key)
        tiles[current_key] = tile
        left = ''
        right = ''
        tile = []
        first = True
    else:
        tile.append(line)
        left += line[0]
        right += line[len(line) - 1]
        last_line = line
        if first:
            append(line, current_key)
            first = False

append(last_line, current_key)
append(left, current_key)
append(right, current_key)
tiles[current_key] = tile

# for t in tiles.values():
#    print_tile(t)

for id in borders.values():
    if len(id) == 1:
        occurs[id[0]] += 1

print(occurs)
#print(borders)
result = 1
count = 0
for key in occurs.keys():
    if occurs[key] == 2:
        result *= key
        count += 1

print(result)
print(count)
