import sys
f = open("input_init.txt", 'r')


def get_mapped_value(from_to_map, value):
    for key, range in from_to_map.keys():
        if key <= value < key + range:
            return from_to_map[(key, range)] + (value - key)

    return value


seeds = []
maps = []
for i in range(7):
    maps.append(dict())
map_number = 0
for line in f:
    line = line.strip()
    # print(line)
    if line.startswith('seeds:'):
        seeds = list(map(int, line[7:].split()))
    elif line == '':
        continue
    elif line == 'seed-to-soil map:':
        map_number = 0
    elif line == 'soil-to-fertilizer map:':
        map_number = 1
    elif line == 'fertilizer-to-water map:':
        map_number = 2
    elif line == 'water-to-light map:':
        map_number = 3
    elif line == 'light-to-temperature map:':
        map_number = 4
    elif line == 'temperature-to-humidity map:':
        map_number = 5
    elif line == 'humidity-to-location map:':
        map_number = 6
    else:
        destination, source, bereich = map(int, line.split())
        maps[map_number][(source, bereich)] = destination


print()
min_location = sys.maxsize
seed_pairs = []
for i in range(0, len(seeds), 2):
    seed_pairs.append((seeds[i], seeds[i+1]))

print(seed_pairs)

for seed_start, bereich in seed_pairs:
    print("next pair", seed_start, bereich)
    for seed in range(seed_start, seed_start + bereich):
        value = seed
        for m in maps:
            print(value, end=' ' )
            value = get_mapped_value(m, value)
        print()
        min_location = min(min_location, value)
        print("min_location", min_location)
    print(value)
print()
print("min_location", min_location)

     


