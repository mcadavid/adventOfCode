f = open('input1.txt', 'r')

bags = set()
def printAllPathsUtil(u, d, path):
    visited[u] = True
    path.append(u)
    if u == d:
        print(path)
        bags.add(path[0])
    else:
        for i in graph[u]:
            if not visited[i]:
                printAllPathsUtil(i, d, path)
    path.pop()
    visited[u] = False


graph = dict()
visited = dict()
for line in f:
    source, goal = line.split(" contain ")
    source = source.split()[0] + source.split()[1]
    goals = goal.split(", ")
    if not source in graph.keys():
        graph[source] = []
    print(goals[0])
    visited[source] = False
    if goals[0][:-1] != "no other bags.":
        for g in goals:
            graph[source].append(g.split()[1] + g.split()[2])





print(graph)
print(visited)

for sn in graph.keys():
    if sn != "shinygold":
        printAllPathsUtil(sn, "shinygold", [])

print(bags)
print(len(bags))
