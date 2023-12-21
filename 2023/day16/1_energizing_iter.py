
from functools import cache
import sys
sys.setrecursionlimit(100000)

UP = (-1,0)
DOWN = (1,0)
RIGHT = (0, 1)
LEFT = (0, -1)

positions = set()

def next(current, dir):
    while 0 <= current[0] < n and 0 <= current[1] < n and (current, dir) not in energized: 
        tile_symbol = tiles[current[0]][current[1]]
        energized.add((current, dir))

        if tile_symbol == '-' and (dir == UP or dir == DOWN):
            next((current[0] + LEFT[0], current[1] + LEFT[1]), LEFT)
            next((current[0] + RIGHT[0], current[1] + RIGHT[1]), RIGHT)
        elif tile_symbol == '|' and (dir == RIGHT or dir == LEFT):
            next((current[0] + UP[0], current[1] + UP[1]), UP)
            next((current[0] + DOWN[0], current[1] + DOWN[1]), DOWN)
        else:
            if tile_symbol == '\\':
                dir = (dir[1], dir[0])
            elif tile_symbol == '/':
                dir = ((-1)*dir[1], (-1)*dir[0])
            current = (current[0] + dir[0], current[1] + dir[1])






energized = set()
tiles = []
if __name__ == "__main__":
    tiles = open('input.txt', 'r').read().split('\n')
    # print(tiles)
    n = len(tiles)
    next((0,0), RIGHT)
    print(len(energized))
    result = len(set([x[0] for x in energized]))
    print(result)

