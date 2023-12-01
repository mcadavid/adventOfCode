import sys

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
                if len(new_path) > len_min:
                    return -1
                queue.append(new_path)

                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    # print("len =", len(new_path) - 1, "Shortest path =", *new_path)
                    return len(new_path) - 1
            explored.append(node)

    # Condition when the nodes
    # are not connected
    #print("So sorry, but a connecting path doesn't exist :(")
    return -1



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
a_pos = []
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

        if heatmap[i][j] == 'a':
            a_pos.append(count)

        for (a,b,c) in [(i, j+1, count + 1), (i,j-1, count - 1), (i+1,j, count + columnNr), (i-1,j, count - columnNr)]:
            if a < 0 or a >= rowsNr or b < 0 or b >= columnNr:
                continue
            if check(current, heatmap[a,b]):
                graph[count].append(c)

        count += 1

print(count)
print(len(graph), graph)
print(start, '->', goal)

len_min = 350
print("there are", len(a_pos), "a positions")
count = 0
for i in a_pos:
    result = BFS_SP(graph, i, goal)
    if count % 100 == 0: print('\n')
    print('.', end=' ')
    count += 1
    if -1 < result < len_min:
        len_min = result

print(len_min)










