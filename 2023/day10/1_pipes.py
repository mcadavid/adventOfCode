import sys
import os
sys.setrecursionlimit(10000)


pipes = open('input.txt', 'r')

graph = [[]]

adj_S =  [(0,1), (1, 0)] # F

types = {'|':[(1,0), (-1,0)], '-': [(0,1), (0,-1)], 'L':[(0,1), (-1,0)], 'J':[(0, -1), (-1,0)], '7':[(0,-1), (1,0)], 'F': [(0,1), (1, 0)], '.':[(0,0), (0,0)], 'S':adj_S}



def findCycleWithDFS(s, visited, adj):
        count = 0
        stack = [] 
        stack.append(s) 
 
        while (len(stack)): 
            s = stack[-1] 
            stack.pop()
            if (not visited[s]): 
                visited[s] = True
                count += 1
            else:
                return True, count
                
            for node in adj[s]: 
                if (not visited[node]): 
                    stack.append(node) 

    
        return False, count

i = 0
start = None
adj = dict()
for line in pipes:
    for j in range(len(line.strip())):
        if line[j] == 'S': 
            start = (i,j)
        neighbours = [(i + k, j + l) for k, l in types[line[j]]]
        adj[(i,j)] = neighbours
    i += 1

visited = dict([(key, False) for key in adj.keys()])
print(start)
_, count = findCycleWithDFS(start, visited, adj)
print( count // 2)
