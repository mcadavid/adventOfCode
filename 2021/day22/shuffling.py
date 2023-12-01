import math, sys


def mod_inverse(a, N):
    m0 = N
    y = 0
    x = 1

    if (N == 1):
        return 0

    while (a > 1):
        # q is quotient
        q = a // N

        t = N

        # m is remainder now, process
        # same as Euclid's algo
        N = a % N
        a = t
        t = y

        # Update x and y
        y = x - q * y
        x = t

        # Make x positive
    if (x < 0):
        x = x + m0

    return x


def mod_divide(a, b, N):
    a = a % N
    inv = mod_inverse(b, N)
    return (inv * a) % N


def increment(n, index_searched):
    return mod_divide(index_searched, n, N)


def deal_new(index_searched):
    return (N - index_searched + 1) % N


def cut(n, index_searched):
    if n >= 0:
        return (index_searched + n) % N
    else:
        v = N + n + index_searched
        return v % N


instructions = ['deal with increment 7',
                'deal into new stack',
                'deal into new stack']

# 3 0 7 4 1 8 5 2 9 6

instructions = ['deal with increment 7',
                'deal with increment 9',
                'cut -2']

instructions = ['cut -4']

instructions = ['cut -4']

instructions = ['cut 6',
                'deal with increment 7',
                'deal into new stack']

instructions = ['deal with increment 7',
                'deal with increment 9',
                'cut -2']

instructions = ['cut -4']

instructions = ['deal with increment 3']

instructions = ['cut 3']

instructions = ['deal with increment 7',
                'deal with increment 9',
                'cut -2']


instructions = ['cut -2']

INCREMENT_INSTR = 'deal with increment '
DEAL_WITH_NEW_INSTR = 'deal into new stack'
CUT_INSTR = 'cut '

N = 10


# 6 7 8 9 0 1 2 3 4 5
def compute(index_searched):
    for line in instructions:
        if line.startswith(INCREMENT_INSTR):
            index_searched = increment(int(line[len(INCREMENT_INSTR): len(line)]), index_searched)
        elif line.startswith(DEAL_WITH_NEW_INSTR):
            index_searched = deal_new(index_searched)
        elif line.startswith(CUT_INSTR):
            index_searched = cut(int(line[len(CUT_INSTR): len(line)]), index_searched)
    return index_searched


print(*range(10))
for i in range(10):
    print(compute(i), end=' ')
print()

print('0 3 6 9 2 5 8 1 4 7')
print('0 7 4 1 8 5 2 9 6 3')




print('6 3 0 7 4 1 8 5 2 9')


for i in [0, 7, 4, 1, 8, 5, 2, 9, 6, 3]:
    print(compute(i), end=' ')
print()
