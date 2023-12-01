f = open('input1.txt', 'r')

bags = set()


result = 0
def dfs(node):
    global result
    if not visited[node]:
        visited[node] = True
        for nd in graph[node]:
            result += nd[1] * (1 + dfs(nd[0]))
    print(result)
    return result



#def count_children(bag: str) -> int:
#    return sum(child_count * (1 + count_children(child)) for child_count, child in child_map[bag])


def count_children(node):
    for n in graph[node]:
        return sum(n[1] * (1 + count_children(n[0])))


deadends = []
graph = dict()
visited = dict()
for line in f:
    source, goal = line.split(" contain ")
    source = source.split()[0] + source.split()[1]
    goals = goal.split(", ")
    if not source in graph.keys():
        graph[source] = []
    visited[source] = False
    bags_no = 0
    if goals[0][:-1] != "no other bags.":
        for g in goals:
            graph[source].append((g.split()[1] + g.split()[2], int(g.split()[0])))
    else:
        deadends.append(source)

print(graph)
print(visited)
print(deadends)

# for sn in graph.keys():
# if sn != "shinygold":
#   printAllPathsUtil(sn, "shinygold", [])

r = dfs("shinygold")
print(r)
print(count_children("shinygold"))

print(bags)
print(len(bags))
