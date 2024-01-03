
x, m, a, s = 0,0,0,0
first = 'in'

def build_workflow(line):
    line = line.strip()
    rule_start = line.index('{')
    rule = line[rule_start+1:-1]
    index = rule.rfind(',')
    rule = rule[:index] + ',True:' + rule[index+1:]
    yield line[:rule_start] 
    yield dict([(r.split(':')[0], r.split(':')[1]) for r in rule.split(',')])


def next(rule):
   
    for r in rule:
        if eval(r):
            return rule[r]
        
        
if __name__ == '__main__': 
    result = 0      
    workflow, ratings = open('c:/malu/programming/advent_of_code/adventOfCode/2023/day19/input.txt').read().split('\n\n')
    workflow = dict(map(build_workflow, workflow.split('\n')))
    # print(workflow)
    ratings = list(ratings.split('\n'))
    value = first
    for rating in ratings:
        rating = str(rating)
        rating = rating[1:-1].split(',')
        for e in rating:
            exec(e)
        # print(rating, end=': ')
        while value not in 'AR':
            # print(value, end='->')
            value = next(workflow[value])
        if value == 'A':
            result += sum([x, m, a, s])
        value = first
        
    if value == 'A':
        result += 1

print(result)