PREAMBLE = 25
f = open("input2.txt", 'r')

l = []
count = 0
for line in f:
    l.append(int(line))

goal_number = 1721308972
print(l)
n = 0
start_index = 0
end_index = 0
for i in range(len(l)):
    n += l[i]
    end_index = i
    while n > goal_number:
        n = n - l[start_index]
        start_index += 1
    if n == goal_number:
        break


col = sorted(l[start_index: end_index + 1])
print(col)
print(sum(col))
print(col[0] + col[len(col) - 1])

