import networkx as nx

f = open('input.txt')

G = nx.DiGraph()
vertices = set()
for line in f:
    line = line.strip()
    v1, nodes = line.split(':')
    vertices.add(v1)
    nodes = nodes.split()
    for v in nodes:
        G.add_edge(v1, v, capacity=1.0)
        G.add_edge(v, v1, capacity=1.0)
        vertices.add(v)

v = vertices.pop()
for w in vertices:
    cut_value, partition = nx.minimum_cut(G, v, w)
    if cut_value == 3:
        print(len(partition[0]), len(partition[1]), len(partition[0]) * len(partition[1]))
        exit()
