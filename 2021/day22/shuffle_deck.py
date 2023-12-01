import sys
import os
import os.path
import re

import collections
import functools
import heapq
import itertools
import math
import multiprocessing
import random
import string
import time

from collections import Counter
from collections import defaultdict
# from dataclasses import dataclass
from functools import lru_cache
from itertools import combinations
from itertools import product
from multiprocessing import Pool


DEBUG=False

def load():
    filename = "input.txt"

    result = []
    with open(filename) as f:
        data = f.readlines()
        data = [x.strip() for x in data]
        for line in data:
            tokens = line.split()
            if line.startswith('cut'):
                result.append( ('cut', int(tokens[-1])))
            elif line.startswith('deal with increment'):
                result.append(('deal-increment', int(tokens[-1])))
            elif line.startswith('deal into new stack'):
                result.append(('deal-new', None))


        return result



def shuffle_deck(data, deck):

    def reverse_deck(old_stack):
        old_stack.reverse()
        return old_stack

    def rotate_deck(stack, n):
        d = collections.deque(stack)
        d.rotate(-n)
        return list(d)

    def mul_mod_deck(stack, n):
        new_stack = [None] * len(stack)
        for i in range(len(stack)):
            other_i = (i*n)%len(stack)
            new_stack[other_i] = stack[i]
        return new_stack

    for cmd, n in data:
        if cmd == 'cut':
            deck = rotate_deck(deck, n)
        elif cmd == "deal-increment":
            deck = mul_mod_deck(deck, n)
        elif cmd == "deal-new":
            deck = reverse_deck(deck)

    return deck


def part_1(data):
    NUM_CARDS = 10007
    deck = list(range(NUM_CARDS))
    deck = shuffle_deck(data, deck)
    return deck.index(2019)


data = load()
v = part_1(data)
print(v)