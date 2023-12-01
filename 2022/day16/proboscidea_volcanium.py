import sys
from collections import defaultdict



class Node:
    def __init__(self, name, edges, value, is_open=False):
        self.name = name
        self.edges = edges
        self.rate = rate

    def __repr__(self):
        return ( f"name: {self.name}, rate: {self.rate}, edges:{self.edges}")

g = dict()

VAL = 0
NODES = 1
OPEN = 2

visited = defaultdict(int)
sum = 0
time = 30

max_value = 0
def depthFirst(name):
    global sum
    global time
    global uniqueSum

    # Marking the visited vertex as true
    visited[name] += 1

    # Updating the value of connection
    print(name, graph[name], time)
    if time <= 0:
        fi
        return
    if not graph[name][OPEN]:
        time -= 1
        sum += time * graph[name][VAL]
        graph[name][OPEN] = True

    # Traverse for all adjacent nodes
    for i in graph[name][NODES]:
        if i[0] not in visited.keys() or visited[i[0]] == False:
            # Recursive call to the
            # DFS algorithm
            time -= 1
            depthFirst(i[0])
            visited[i[0]] -= 1
            if not visited[i[0]]:
                uniqueSum -= graph[i[0]][VAL]
                del visited[i[0]]

maxTime = 30
def dfs(node, time):
        global uniqueSum
        global ans

        # terminate condition on time
        if time > maxTime:
            return;

        # if visiting this node for first time in the path, it is unique for that path ,
        # add this to store and uniqueSum otherwise just increase its visit count
        if node not in visited:
            visited[node] += 1
            uniqueSum += graph[node][VAL]
        else:
            visited[node] += 1

        if node == 'AA':
            ans = max(ans, uniqueSum)

        # visit neighbours with time increment
        for next in graph[node][NODES]:
            dfs(next[0], time + 1)

        # clean up visit for this node , if the node was visited only once so far, we remove this key from visits and
        # uniqueSum for further considerations otherwise just decrement
        visited[node] -= 1
        if not visited[node]:
            uniqueSum -= graph[node][VAL]
            del visited[node]


f = open('input')
for l in f:
    valve, tunnels = l.strip().split(';')
    valve = valve.split()
    name = valve[1]
    rate = int(valve[4].strip(';').split('=')[1])
    tunnels = tunnels.split()
    edges = []
    for i in range(4, len(tunnels)):
        edges.append(tunnels[i].strip(','))
    g[name] = Node(name, edges, rate)

graph = dict()
for n in g.keys():
    new_edges = []
    for e in g[n].edges:
        new_edges.append((e,g[e].rate))
    new_edges.sort(key=lambda x:-x[1])
    graph[n] = [g[n].rate, new_edges,  False]


print(graph)
uniqueSum = 0
depthFirst('AA')
print(sum, time)



