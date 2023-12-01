import math, sys, copy, collections


# 3 0 7 4 1 8 5 2 9 6

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


instructions = ['deal with increment 7',
                'deal with increment 9',
                'cut -2']

instructions = ['cut -4']

instructions = ['cut -4']

instructions = ['deal with increment 3']

instructions = ['cut 3']

instructions = ['deal with increment 7',
                'deal with increment 9',
                'cut -2']

instructions = ['cut -2']

instructions = ['deal with increment 7',
                'deal into new stack',
                'deal into new stack']

instructions = ['cut -4']
instructions = ['cut 3']

instructions = ['cut 6',
                'deal with increment 7',
                'deal into new stack']

instructions = ['deal with increment 7',
                'deal with increment 9',
                'cut -2']

instructions = ['deal into new stack',
                'cut -2',
                'deal with increment 7',
                'cut 8',
                'cut -4',
                'deal with increment 7',
                'cut 3',
                'deal with increment 9',
                'deal with increment 3',
                'cut -1']

INCREMENT_INSTR = 'deal with increment '
DEAL_WITH_NEW_INSTR = 'deal into new stack'
CUT_INSTR = 'cut '

N = 10007
# N=10
with open("input.txt") as infile:
    lines = infile.read().split('\n')


instructions = list(lines)
# 6 7 8 9 0 1 2 3 4 5
def compute():
    col = list(range(N))
    for line in instructions:
        print(line)
        if line.startswith(INCREMENT_INSTR):
            offset = int(line[len(INCREMENT_INSTR): len(line)])
            # col2 = [0 for i in range(N)]
            # for i in range(len(col)):
            #     col2[(offset * i) % N] = col[i]
            # col = col2

            col2 = [0 for i in range(N)]
            for i in range(N):
                other_i = (i * offset) % N
                col2[other_i] = col[i]
            col = col2
        elif line.startswith(DEAL_WITH_NEW_INSTR):
            col.reverse()
        elif line.startswith(CUT_INSTR):
            col2 = [0 for i in range(N)]
            for i in range(len(col)):
                col2[(N - offset + i) % N] = col[i]
            col = col2
        # print(col)
        # print(col[2019])
    return col

# compute()
print(compute().index(2019))
# 3 0 7 4 1 8 5 2 9 6
