pipes = open('input.txt', 'r')

adj_S = [(0, 1), (1, 0)]  # F


types = {'|': [(1, 0), (-1, 0)], '-': [(0, 1), (0, -1)], 'L': [(0, 1), (-1, 0)], 'J': [(0, -1),

                                                                                       (-1, 0)], '7': [(0, -1), (1, 0)], 'F': [(0, 1), (1, 0)], '.': [(0, 0), (0, 0)], 'S': adj_S}

def findCycleWithDFS(s, visited, adj):
    count = 0
    stack = []
    stack.append(s)
    old_node = None
    while (len(stack)):
        s = stack[-1]
        stack.pop()
        if (not visited[s]):
            visited[s] = True
            count += 1
            path.append(s)
        else:
            path.append(start)
            return True, count

        for node in adj[s]:
            if (not visited[node]):
                stack.append(node)

    return False, count


# Ray casting method: 
# https://stackoverflow.com/questions/16625507/checking-if-a-point-is-inside-a-polygon
# https://stackoverflow.com/questions/36399381/whats-the-fastest-way-of-checking-if-a-point-is-inside-a-polygon-in-python
def ray_tracing(x, y, poly):
    n = len(poly)
    inside = False
    p2x = 0.0
    p2y = 0.0
    xints = 0.0
    p1x, p1y = poly[0]
    for i in range(n+1):
        p2x, p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xints = (y-p1y)*(p2x-p1x)/(p2y-p1y) + p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
                        
        p1x, p1y = p2x, p2y

    return inside

i = 0
start = None
adj = dict()
path = []

for line in pipes:
    for j in range(len(line.strip())):
        if line[j] == 'S':
            start = (i, j)
        neighbours = [(i + k, j + l) for k, l in types[line[j]]]
        adj[(i, j)] = neighbours
    i += 1

visited = dict([(key, False) for key in adj.keys()])
print(start)
_, count = findCycleWithDFS(start, visited, adj)

print("Length of cycle", len(path)//2)
not_visited = [(i, j) for (i, j) in visited.keys() if not visited[(i, j)]]
numberOfInteriorNodes = 0
for (i, j) in not_visited:
    if (ray_tracing(i, j, path)):
        numberOfInteriorNodes += 1
print(numberOfInteriorNodes)


