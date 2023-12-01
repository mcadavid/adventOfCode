
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priority = dict()
counter = 1;
for letter in alpha:
    priority[letter] = counter
    counter += 1

f = open("input.txt",'r')
total = 0
for line in f:
    print(line)
    line = line[:-1]
    len_line = len(line)
    middle = len_line // 2 # find the middle of string
    print(middle)
    first = set(list(line[0:middle])) # first compartement
    second = set(list(line[middle:len_line])) # second compartement
    # print(first)
    # print(second)
    inter = first.intersection(second).pop() # get the intersection and get the common value (assume it is just 1)
    total += priority[inter] # add to total

print(total)



