from collections import deque
f = open('input.txt')

process = {}
ff_states = {}
conj_memory = {}
conjunctions = []

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

# print("process", process)
# print("flip flops", ff_states)
# print("conjunctions memory", conj_memory)
# print("conjuctions", conjunctions)

steps = deque()
low = 0
high = 0
old_high, old_low = 0, 0


for k in range(1000):
    steps.append(("roadcaster", 'button', "low"))
    # print(ff_states, conj_memory, k)
    while steps:
        module, from_, pulse = steps.popleft()
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

    if all(not state for state in ff_states.values()):
        one_high = False
        for i in conj_memory:
            for j in conj_memory[i]:
                if conj_memory[i][j] == 'high':
                    one_high = True
                    break
            if one_high:
                break
        if not one_high:
            print(conj_memory)
            print(low - old_low, high - old_high)
            print("done", low, high, k)
            old_low = low
            old_high = high
            break


print(low, high, k)
low = (low) * (1000 // (k+1))
high = high * (1000 // (k+1))
print(low, high, low * high)
