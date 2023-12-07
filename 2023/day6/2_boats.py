import string

time, distance = open('input.txt', 'r').read().split('\n')

time =  int(time[5:].translate(str.maketrans("", "", string.whitespace)))
distance = int(distance[9:].translate(str.maketrans("", "", string.whitespace)))

print(time, distance)

win = 0
start_winning = False
for t in range(1, time):
    dist = (time - t) * t
    if dist > distance:
        start_winning = True
        win += 1
    elif start_winning:
        break
print(". Winning times:", win)

print(win)
