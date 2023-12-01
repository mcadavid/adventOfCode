f = open("input")

jolts = []
for line in f:
    jolts.append(int(line))

jolts.append(max(jolts) + 3)
jolts.append(0)
jolts = sorted(jolts, reverse=True)

count = 0
def printPostorder(root):
    global count
    if root != 0:
        for i in tree[root]:
            printPostorder(i)
            #print(tree[i])
    else:
        count += 1


n = len(jolts)
tree = dict()
counter = 0
for i in range(n - 3):
    connected = []
    node = jolts[i]
    if node - jolts[i + 1] <= 3:
        connected.append(jolts[i + 1])
    if node - jolts[i + 2] <= 3:
        connected.append(jolts[i + 2])
    if node - jolts[i + 3] <= 3:
        connected.append(jolts[i + 3])
    tree[node] = connected

connected = []
if jolts[n - 3] - jolts[n - 2] <= 3:
    connected.append(jolts[n - 2])
if jolts[n - 3] - jolts[n - 1] <= 3:
    connected.append(jolts[n - 1])
tree[jolts[n - 3]] = connected
connected = []
if jolts[n - 2] - jolts[n - 1] <= 3:
    connected.append(jolts[n - 1])
tree[jolts[n - 2]] = connected

print(jolts)
#print(tree)
printPostorder(jolts[0])
print(count)
