from collections import deque
f = open('input.txt').read().split('\n')
garden = list(map(list, f))


n = len(garden)

def print_garden():
    for i in range(n):
        print(*garden[i])
    print() 


# print_garden()


S = (5,5)
S = (65, 65)
steps = 64
new_nodes_to_visit = deque()
new_nodes_to_visit.append(S)
count = 0
round = []
for rounds in range(steps):
    nodes_to_visit = deque(set(new_nodes_to_visit))
    new_nodes_to_visit = deque()
    visited = set()
    while nodes_to_visit:
        count += 1
        i,j = nodes_to_visit.pop()
        if (i,j) in visited:
            continue
        adj = []
        if i > 0:
            adj.append((i-1,j))
        if i < n-1:
            adj.append((i+1,j))
        if j < n - 1: 
            adj.append((i,j+1))
        if j > 0:
            adj.append((i,j-1))
        visited.add((i,j))
        garden[i][j] = '.'
        # print(adj, (i,j))
        for k,l in adj:
            if garden[k][l] in '.0' and not (k,l) in visited:
                garden[k][l] = '0'
                new_nodes_to_visit.append((k,l))
                visited.add((k,l))

    

print_garden()
print(len(new_nodes_to_visit))
print(len(set(new_nodes_to_visit)))

    

