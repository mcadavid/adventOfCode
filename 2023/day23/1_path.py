from collections import defaultdict
import sys

sys. setrecursionlimit(2**20)

paths = set()
class Graph:
    verts = {}
  
    def __init__(self, vertices):
        # No.  vertices
        self.V = vertices 
         
        # default dictionary to store graph
        self.graph = defaultdict(set) 
  
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].add(v)
  
def find_all_paths(graph, start, end):
    stack = [(start, [start])]
    paths = []

    while stack:
        current, path = stack.pop()

        for neighbor in graph.graph[current]:
            if neighbor not in path:
                if neighbor == end:
                    paths.append(len(path + [neighbor]))
                else:
                    stack.append((neighbor, path + [neighbor]))

    return paths

def find_all_paths_better(graph, start, end):
    distances = {}
    stack = [(start, 0, set())]
    paths = 0
    count = 0

    while stack:
        current, d, path = stack.pop()
        # print(current, d, path)
        if current in path:
            continue
        count += 1
        
        # if current in distances and distances[current] > d:
        #     print(len(stack), len(distances), current)
        #     continue
        # distances[current] = d

        if current == end and d > paths:
            paths = d
            print(paths, len(stack), count)
            if paths > 7000:
                return

        for neighbor in graph.graph[current]:
            new_path = path | {current}
            stack.append((neighbor, d + 1, new_path))
      
    return paths



f = open('input.txt').read().strip()
woods = f.split('\n')
n = len(woods)
m = len(woods[0])



S = (0,1)
g = Graph(5)
vert = set()
task = 2
for i in range(n):
    for j in range(m):
        if woods[i][j] == '#':
            continue
        vert.add((i, j))
        for k,l in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]: #neighbours
            if (i,j) == (5,4):
                print((i,j), '->', woods[i][j], (k,l), '->', woods[k][l])
            if k < 0 or l < 0 or k > n-1 or l > m-1:
                continue
            if woods[k][l] == '#':
                continue
            slide = woods[i][j]
            if task == 1:
                if slide in '><^v' and ((slide == '>' and (k,l) !=  (i, j+1)) or (slide == '<' and (k,l) != (i, j-1)) or (slide == '^' and (k,l) != (i-1, j)) or (slide == 'v' and (k,l) != (i+1, j))):
                    if (i,j) == (5,4): print("i was here", )
                    continue
            
            g.addEdge((i,j), (k,l))



g.V = len(vert)
g.verts = vert
paths = find_all_paths_better(g, (0,1), (n-1, m-2))
print(n-1, m-2, woods[n-1][m-2])
print(paths)


# for e in g.graph:
#     print(e, g.graph[e])




    