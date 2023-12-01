
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priority = dict()
counter = 1;
for letter in alpha:
    priority[letter] = counter
    counter += 1

f = open("input.txt",'r')
all_rucksacks = []
for line in f:
    print(line[:-1])
    all_rucksacks.append(line[:-1])

count = 0
total = 0
while count < len(all_rucksacks):
    first = set(list(all_rucksacks[count]))  # first elf
    second =  set(list(all_rucksacks[count + 1]))  # second elf
    third  =  set(list(all_rucksacks[count + 2]))  # third elf

    inter = first & second & third

    total += priority[inter.pop()] # add to total
    count += 3

print(total)



