from collections import deque, defaultdict
import sys
import math
f = open('input.txt')

process = {}
ff_states = {}
conj_memory = {}
conjunctions = []
sources = defaultdict(list)

for line in f:
    line = line.strip()
    source, dest = line.split(' ->')
    dest = dest.strip().split(', ')
    # print(source[1:], dest)
    process[source[1:]] = dest
    if source.startswith('%'):
        ff_states[source[1:]] = False
    elif source.startswith('&'):
        conjunctions.append(source[1:])
    for i in dest:
        if i not in conj_memory:
            conj_memory[i] = {}
        conj_memory[i][source[1:]] = 'low'
        sources[i].append(source[1:])

assert len(sources['rx']) == 1
print(sources['rx'][0])
sources_from_rx = sources[sources['rx'][0]]
# only cl reaches rx, the sources_from_rx reach cl
# if they are low then cl would be high and rx will be low
# ['js', 'qs', 'dt', 'ts']
print(sources_from_rx)
in_cycle = defaultdict(bool)


# print("process", process)
# print("flip flops", ff_states)
# print("conjunctions memory", conj_memory)
# print("conjuctions", conjunctions)

steps = deque()
low = 0
high = 0
old_high, old_low = 0, 0
cycle = {}
k = 0
candidates = []
while True:
    steps.append(("roadcaster", 'button', "low"))
    # print(ff_states, conj_memory, k)
    while steps:
        module, from_, pulse = steps.popleft()

        if pulse == 'low' and module in sources_from_rx:
            # starting now all modules will arrive at the same time at rx
            # we have four different starts: broadcaster -> ct, hr, ft, qm
            # only cl reaches rx, the sources_from_rx reach cl
            # if they are low then cl would be high and rx will be low
            # ['js', 'qs', 'dt', 'ts']
            # Analog to
            # we have four busses start ['js', 'qs', 'dt', 'ts'] at the same time, when will they meet again at rx?
            if module in cycle and in_cycle[module]:
                print(f'k={k} cycle={cycle[module] + 1} module={module}')
                candidates.append(cycle[module] + 1)

            in_cycle[module] = True
            cycle[module] = k

        if len(candidates) == len(sources_from_rx):
            print(candidates)
            print(math.lcm(*candidates))
            sys.exit(0)

        if pulse == 'low':
            low += 1
        else:
            high += 1
        if module == 'roadcaster':
            for m in process[module]:
                steps.append((m, module, pulse))
        elif module in ff_states:
            state = ff_states[module]
            if pulse == 'low':
                ff_states[module] = not state
                if state:
                    pulse = 'low'
                else:
                    pulse = 'high'
                for o in process[module]:
                    steps.append((o, module, pulse))
            else:
                continue
        elif module in conjunctions:
            conj_memory[module][from_] = pulse
            all_high = all(conj_memory[module][i] ==
                           'high' for i in conj_memory[module])
            if all_high:
                pulse = 'low'
            else:
                pulse = 'high'
            for o in process[module]:
                steps.append((o, module, pulse))

    k += 1
    # if k==999:
    #     break


print(low, high, k)
print(low, high, low * high)
