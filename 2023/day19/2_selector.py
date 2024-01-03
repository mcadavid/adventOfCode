
import functools

x, m, a, s = 0,0,0,0
first = 'in'

def build_workflow(line):
    line = line.strip()
    rule_start = line.index('{')
    rule = line[rule_start+1:-1]
    index = rule.rfind(',')
    rule = rule[:index] + ',True:' + rule[index+1:]
    yield line[:rule_start] 
    # yield {r.split(':')[1] for r in rule.split(',')}
    yield dict([(r.split(':')[0], r.split(':')[1]) for r in rule.split(',')])


def next(rule):
    for r in rule:
        if eval(r):
            return rule[r]


def find_all_paths(start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in workflow_simple:
        return []
    paths = []
    for node in workflow_simple[start]:
        if node not in path:
            newpaths = find_all_paths(node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths  

def inter(a, b):
    if (b[1] < a[0] or a[1] < b[0]):
        return [0,0]
    else:
        l = max(a[0], b[0])
        r = min(a[1], b[1])
    return [l, r]

def from_to(from_node, to_node):
    conditions = workflow[from_node]
    print(from_node, conditions, end='')
    
    for cond in conditions:
        if cond[0] == 'T':
            break
        variable = cond[0] # x m a or s
        r = ranges[variable]
        if to_node == conditions[cond]:
            if cond[1] == '<':
                ranges[variable] = inter(r, [1, int(cond[2:]) - 1])
            elif cond[1] == '>':
                ranges[variable] = inter(r, [int(cond[2:]) + 1, 4000])
        else:
            if cond[1] == '>':
                ranges[variable] = inter(r, [1, int(cond[2:])])
            elif cond[1] == '<':
                ranges[variable] = inter(r, [int(cond[2:]), 4000])
            
        if to_node == conditions[cond]:
            break

    print(ranges)

        
        
if __name__ == '__main__': 
    result = 0      
    workflow, ratings = open('c:/malu/programming/advent_of_code/adventOfCode/2023/day19/input_init.txt').read().split('\n\n')
    workflow = dict(map(build_workflow, workflow.split('\n')))
    workflow_simple = {}
    for node in workflow:
        workflow_simple[node] = workflow[node].values()
    #print(workflow)
    #print(workflow_simple)
    value = first
    paths = find_all_paths(first, 'A', [])
    print(len(paths))
    print(paths)
    paths = {tuple(x) for x in paths}
    print(len(paths))

    print(paths, type(paths))
    
    for p in paths:
        print("Path:", p)
        ranges = {'x': [1, 4000], 'm': [1, 4000], 'a':[1, 4000], 's': [1, 4000]}
        prev = p[0]
        for n in p[1:]:
            print(prev, n)
            from_to(prev, n)
            prev = n
        path_value = functools.reduce(lambda x, y: x * y, [b - a + 1 for a,b in ranges.values()])
        print(path_value)
        result += path_value
        print("************************************************************")

    print(result)
