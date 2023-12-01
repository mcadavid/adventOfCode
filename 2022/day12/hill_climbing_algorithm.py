import numpy as np
from collections import defaultdict

# Python implementation to find the
# shortest path in the graph using
# dictionaries

# Function to find the shortest
# path between two nodes of a graph
def BFS_SP(graph, start, goal):
    explored = []

    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]

    # If the desired node is
    # reached
    if start == goal:
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
                if neighbour == goal:
                    print("len =", len(new_path) - 1, "Shortest path =", *new_path)
                    return
            explored.append(node)

    # Condition when the nodes
    # are not connected
    print("So sorry, but a connecting" \
          "path doesn't exist :(")
    return



f = open('input.txt')

heatmap = []
for line in f:
    heatmap.append(list(line[:-1]))

heatmap = np.array(heatmap)

rowsNr =  len(heatmap)
columnNr = len(heatmap[0])
print(rowsNr * columnNr)


def check(source,  dest):
    if dest == 'E':
        dest = 'z'
    elif dest == 'S':
        dest = 'a'
    return ord(dest) <= ord(source) + 1


goal = 0
start = 0
graph = defaultdict(list)
count = 0
for i in range(rowsNr):
    for j in range(columnNr):
        current = heatmap[i][j]
        if current == 'S':
            start = count
            current = 'a'
            heatmap[i][j] = current
            print('S', heatmap[i][j])
        elif current == 'E':
            goal = count
            current = 'z'
            heatmap[i][j] = current
            print('E', heatmap[i][j])

        for (a,b,c) in [(i, j+1, count + 1), (i,j-1, count - 1), (i+1,j, count + columnNr), (i-1,j, count - columnNr)]:
            if a < 0 or a >= rowsNr or b < 0 or b >= columnNr:
                continue
            if check(current, heatmap[a,b]):
                graph[count].append(c)

        # if j < columnNr - 1 and check(current, heatmap[i][j+1]):
        #     graph[count].append(count + 1)
        # if j > 0 and check(current, heatmap[i][j-1]):
        #     graph[count].append(count - 1)
        # if i < rowsNr - 1 and check(current, heatmap[i+1][j]):
        #     if count == 13: print(current, heatmap[i+1][j])
        #     graph[count].append(count + columnNr)
        # if i > 0 and check(current, heatmap[i-1][j]):
        #     graph[count].append(count - columnNr)

        count += 1

print(count)
print(len(graph), graph)
print(start, '->', goal)

BFS_SP(graph, start, goal)








