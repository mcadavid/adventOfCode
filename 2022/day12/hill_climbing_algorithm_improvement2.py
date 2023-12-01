import numpy as np
from collections import defaultdict

# Python implementation to find the
# shortest path in the graph using
# dictionaries

# Function to find the shortest
# path between two nodes of a graph
def BFS_SP(graph, start):
    explored = []

    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]

    # If the desired node is
    # reached
    if heatmap[start] == 'a':
        print("Same Node")
        return

    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]

        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]

            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # Condition to check if the
                # neighbour node is the goal
                if heatmap[neighbour] == 'a':
                    print("len =", len(new_path) - 1, "Shortest path =", *new_path)
                    return len(new_path) - 1
            explored.append(node)

    # Condition when the nodes
    # are not connected
    #print("So sorry, but a connecting path doesn't exist :(")
    return -1


f = open('input')

heatmap = []
for line in f:
    heatmap.append(list(line[:-1]))

heatmap = np.array(heatmap)

rowsNr =  len(heatmap)
columnNr = len(heatmap[0])
print(rowsNr * columnNr)


def check(source,  dest):
    return ord(dest) <= ord(source) + 1


for i in range(rowsNr):
    for j in range(columnNr):
        if heatmap[i][j] == 'S':
            heatmap[i][j] = 'a'
        elif heatmap[i][j] == 'E':
            ei = i
            ej = j
            heatmap[i][j] = 'z'

end = (ei, ej)
graph = defaultdict(list)
for i in range(rowsNr):
    for j in range(columnNr):
        for (a,b) in [(i, j+1), (i,j-1), (i+1,j), (i-1,j)]:
            if a < 0 or a >= rowsNr or b < 0 or b >= columnNr:
                continue
            if check(heatmap[i][j], heatmap[a,b]):
                graph[(a,b)].append((i,j))

print(len(graph), graph)
print(BFS_SP(graph, (ei,ej)))










