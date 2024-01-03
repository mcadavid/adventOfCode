from collections import defaultdict
import random
import copy

f = open("input.txt").read().split('\n')



def getGraph():
    g = defaultdict(set)
    vertices = set()
    for line in f:
        # print(line)
        v1, adj = line.split(': ')
        adj = adj.split()
        for v in adj:
            g[v1].add(v)
            g[v].add(v1)
            vertices.add(v)
            vertices.add(v1)
    # print(g)
    # print(vertices, len(vertices))
    

    for v in g:
        # print(v, ":", g[v])
        g[v] = list(g[v])
    return g, vertices

orig_g, orig_vertices = getGraph()




def get_edges(graph):
    return [(v1, v2) for v1 in graph for v2 in graph[v1]]
        
solved = False

count = 0
while count < 100:
    g, vertices = copy.deepcopy(orig_g), copy.deepcopy(orig_vertices)
    # print("Next", count, len(vertices))
    count += 1

    while len(vertices) > 2:
        edges = get_edges(g)
        secure_random = random.SystemRandom()
        random_edge = secure_random.choice(edges)
        # print(random_edge, end=' -> ')
        # print(random_edge)
        v1, v2 = random_edge
        new_vertex = v1 + '_' + v2
        g[new_vertex] = []
        ch_edges = g[v1] + g[v2]
        g.pop(v1, None)
        g.pop(v2, None)
        vertices.remove(v1)
        vertices.remove(v2)
        vertices.add(new_vertex)
        for v in ch_edges:
            if v == v2 or v == v1:
                continue
            g[new_vertex].append(v)
            g[v].append(new_vertex)
            
            if v1 in g[v]:
                g[v].remove(v1)
            if v2 in g[v]:
                g[v].remove(v2)

    for i in g:
        print("Current lenght", len(g[i]), count)
        def_len = len(g[i])
        break
    
    if def_len == 3:
        print("youuhui")
        break

        


        # print(v1, v2, new_vertex, vertices)
    # for i in g:
    #     #print(len(g[i]))
    #     if len(g[i]) == 3:
    #         solved = True
    #         print("solved")
    #         break
    # if solved:
    #     break
    

for k in g:
    # print(k, ":", len(g[k]))
    for l in g[k]:
        print(l.count('_') + 1)
        break


# jqt: rhn xhk nvd
# rsh: frs pzl lsr
# xhk: hfx
# cmg: qnr nvd lhk bvb
# rhn: xhk bvb hfx
# bvb: xhk hfx
# pzl: lsr hfx nvd
# qnr: nvd
# ntq: jqt hfx bvb xhk
# nvd: lhk
# lsr: lhk
# rzs: qnr cmg lsr rsh
# frs: qnr lhk lsr