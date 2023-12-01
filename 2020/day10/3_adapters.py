f = open("input1")

jolts = []
for line in f:
    jolts.append(int(line))

jolts.append(0)
jolts_sorted = sorted(jolts)
jolts_sorted.append(jolts_sorted[-1] + 3)

graph = {}
for jolt in jolts_sorted:
    diffs = [x for x in map(lambda x: jolt + x, (1, 2, 3))]
    diffs = [y for y in jolts_sorted if y in diffs]
    graph[jolt] = diffs

print(graph)

solution = {0: 1}
for key, value in graph.items():
    if value == []:
        break
    for val in value:
        if val in solution.keys():
            solution[val] += solution[key]
        else:
            solution[val] = solution[key]
        print(solution)

print(solution[jolts_sorted[-1]])
