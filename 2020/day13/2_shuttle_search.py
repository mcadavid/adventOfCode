import sys
import numpy as np
from typing import Tuple

lines = dict()
lines[
   "17,x,x,x,x,x,x,41,x,x,x,37,x,x,x,x,x,367,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,23,x,x,x,x,x,29,x,613,x,x,x,x,x,x,x,x,x,x,x,x,13"]= 1068781
lines["7,13,x,x,59,x,31,19"] = 1068781
lines["17,x,13,19"] = 3417
lines["67,7,59,61"] = 754018
lines["67,x,7,59,61"] = 779210
lines["67,7,x,59,61"] = 1261476
lines["1789,37,47,1889"] = 1202161486


def test():
    for l in lines.keys():
        if lines[l] != calculate(l):
            print("Error!!!")
            break


# Extended Euclid
def extended_euclid(a: int, b: int) -> Tuple[int, int]:
    """
    >>> extended_euclid(10, 6)
    (-1, 2)
    >>> extended_euclid(7, 5)
    (-2, 3)
    """
    if b == 0:
        return (1, 0)
    (x, y) = extended_euclid(b, a % b)
    k = a // b
    return (y, x - k * y)


def invert_modulo(a: int, n: int) -> int:
    """
    >>> invert_modulo(2, 5)
    3
    >>> invert_modulo(8,7)
    1
    """
    (b, x) = extended_euclid(a, n)
    if b < 0:
        b = (b % n + n) % n
    return b


def print_col(a, col1, col2, col3, col4):
    for i in range(a):
        print(col1[i], col2[i], col2[i], col3[i])


def calculate(line):
    print("####################################")
    print(line)
    ns = line.split(',')
    ns = [0 if b == 'x' else int(b) for b in ns]
    print(ns)
    bs = [ns[i] - i for i in range(len(ns)) if ns[i] != 0]
    ns = [b for b in ns if b != 0]
    print(ns)
    print(bs)
    n = len(ns)
    N = 1
    for i in ns:
        N *= i
    print(N)
    N_is = [N // n_i for n_i in ns]
    print(N_is)
    xs = [invert_modulo(N_is[i], ns[i]) for i in range(n)]
    print(xs)
    #print_col(n, bs, ns, N_is, xs)
    result = 0
    for i in range(n):
        result += bs[i] * N_is[i] * xs[i]
    print(result)
    print(result % N)
    return result % N


test()
