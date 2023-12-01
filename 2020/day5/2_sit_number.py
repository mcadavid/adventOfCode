f = open('input2.txt', 'r')
max_value = 0
ids = [0]*800
rows = [0]*800
counter = 0
for line in f:
    line = line.replace('F', '0').replace('B', '1').replace('R','1').replace('L','0')
    row = int(line[0:7], base=2)
    result = row * 8 + int(line[7:10], base=2)
    print(row,int(line[7:10], base=2), result)
    max_value = max(result, max_value)
    rows[counter] = row
    ids[counter] = result
    counter += 1

ids_set = set(ids)
for i in range(1, 800 * 8 + 7):
    if i - 1 in ids_set and i + 1 in ids_set and i not in ids_set:
        print(i)
print(max_value)
