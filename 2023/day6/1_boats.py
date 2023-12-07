time, distance = open('input.txt', 'r').read().split('\n')
print(distance, time)
time = list(map(int, time[5:].split()))
distance = list(map(int, distance[9:].split()))

result = 1
for i in range(len(time)):
    record = time[i]
    win = 0
    start_winning = False
    for t in range(1, time[i]):
        dist = (record - t) * t
        if dist > distance[i]:
            start_winning =  True
            win += 1
        elif start_winning:
            break
    print("Winning times:", win)
    result *= win
    print(result)

print(result)