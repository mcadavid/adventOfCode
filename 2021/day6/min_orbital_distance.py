import sys

sys.stdin = open("input.txt")


class Node:
    def __init__(self, name, value=sys.maxsize):
        self.name = name
        self.value = value
        self.neighbors = []


# visits all the nodes of a graph (connected component) using BFS

def bfs_connected_component(start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]
    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = node.neighbors  # graph[node]
            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
                neighbour.value = min(neighbour.value, node.value + 1)

    return explored



col = ["COM)B",
"B)C",
"C)D",
"D)E",
"E)F",
"B)G",
"G)H",
"D)I",
"E)J",
"J)K",
"K)L",
"K)YOU",
"I)SAN"]

root = Node("3LN", 0)
node_map = dict()
node_map["3LN"] = root

while True:
# for s in col:
    try:
        parent, child = input().split(")")
        # parent, child = s.split(")")
        if parent in node_map.keys():
            parent_node = node_map.get(parent)
        else:
            parent_node = Node(parent)
            node_map[parent] = parent_node
        if child in node_map.keys():
            child_node = node_map.get(child)
        else:
            child_node = Node(child)
            node_map[child] = child_node

        parent_node.neighbors.append(child_node)
        child_node.neighbors.append(parent_node)
    except EOFError:
        break


bfs_connected_component(root)
for node in node_map.values():
    print(node.name, ":", node.value)
    if node.name == 'Q8B':
        print("yeah")
        break
