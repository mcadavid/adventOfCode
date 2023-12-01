f = open('input2.txt', 'r')
max_value = 0
for line in f:
    line = line.replace('F', '0').replace('B', '1').replace('R','1').replace('L','0')
    print(int(line[0:7], base=2),int(line[7:10], base=2))
    result = int(line[0:7], base=2) * 8 + int(line[7:10], base=2)
    max_value = max(result, max_value)

print(max_value)
