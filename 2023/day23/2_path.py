from collections import defaultdict, deque
from time import time

t = time()


paths = set()
class Graph:
  
    def __init__(self):
        # No.  vertices
        self.vertices = set()
        # default dictionary to store graph
        self.edges = defaultdict(list) 
  
    # function to add an edge to graph
    def addEdge(self, u, v, weight):
        self.edges[u].append((v, weight))
        
    def addVertex(self, u):
        self.vertices.add((u))

# stack == dfs
def find_all_paths(graph, start, end):
    stack = [(start, 0, set())]
    max_distance = 0
    while stack:
        current, d, path = stack.pop()

        if current in path:
            continue
        if current == end and d > max_distance:
            max_distance = d
            continue

        for neighbour, weight in graph.edges[current]:
            new_path = path | {current}
            stack.append((neighbour, d + weight, new_path))

    return max_distance

f = open('input_init.txt').read().strip()
woods = f.split('\n')
n = len(woods)
m = len(woods[0])


# create a graph that contains only the intersections as vertices, start and end node
# and the weight of the edges is the distance between the vertices. It is a much smaller graph.
# The same alg as in part 1 to find the biggest distance can be used

S = (0,1)
g = Graph()
# calculate the nodes of the new graph (intersections)
for i in range(n):
    for j in range(m):
        if woods[i][j] == '#':
            continue
        count_neighbours = 0
        for k,l in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]: #neighbours
            if k < 0 or l < 0 or k > n-1 or l > m-1:
                continue
            if woods[k][l] == '#':
                continue
            count_neighbours += 1
        if count_neighbours > 2:
            g.addVertex((i, j))

g.addVertex((0,1))
g.addVertex((n-1, m-2))

# print(g.vertices)
# calculate the weights in the new graph
for v in g.vertices:
    q = deque([(v[0], v[1], 0)])
    visited = set()
    while q:
        i,j, d = q.popleft()
        if (i,j) in visited:
            continue
        if (i,j) in g.vertices and (i,j) != v and d>1:
            g.addEdge(v, (i,j), d)
            continue
        visited.add((i,j))
        for k,l in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]: #neighbours
            if k < 0 or l < 0 or k > n-1 or l > m-1:
                continue
            if woods[k][l] == '#':
                continue
            q.append((k,l, d+1))


no = find_all_paths(g, (0,1), (n-1, m-2))
print(no, max(0, time() - t))



    