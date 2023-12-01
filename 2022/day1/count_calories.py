f = open("input.txt", 'r')
max_cal = 0
temp_cal = 0
count = 0;
for line in f:
    if line != '\n':
        temp_cal += int(line)
    else:
        if (temp_cal > max_cal):
            print(count)
            count += 1
            max_cal = temp_cal
        temp_cal = 0

print(max_cal)
