f = open("input.txt", 'r')

temp_cal = 0

all_calories =  []

for line in f:
    if line != '\n' and line != '\r':
        temp_cal += int(line)
    else:
        all_calories.append(temp_cal)
        temp_cal = 0

if temp_cal != 0:
    all_calories.append(temp_cal)
all_calories.sort(reverse=True)
print(all_calories)
print(all_calories[0] + all_calories[1] +  all_calories[2])
