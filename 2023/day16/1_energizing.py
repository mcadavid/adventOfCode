
from functools import cache
import sys
sys.setrecursionlimit(100000)

UP = (-1,0)
DOWN = (1,0)
RIGHT = (0, 1)
LEFT = (0, -1)

positions = set()

@cache
def next(current, dir):
    if 0 <= current[0] < n and 0 <= current[1] < n and (current, dir) not in energized: 
        tile_symbol = tiles[current[0]][current[1]]
        energized.add((current, dir))
        
        if tile_symbol == '.':
            next_tile = (current[0] + dir[0], current[1] + dir[1])
            next(next_tile, dir)
        
        elif tile_symbol == '-':
            if dir == RIGHT or dir == LEFT:
                next_tile = (current[0] + dir[0], current[1] + dir[1])
                next(next_tile, dir)
            else:
                next((current[0] + LEFT[0], current[1] + LEFT[1]), LEFT)
                next((current[0] + RIGHT[0], current[1] + RIGHT[1]), RIGHT)

        elif tile_symbol == '|':
            if dir == UP or dir == DOWN:
                next_tile = (current[0] + dir[0], current[1] + dir[1])
                next(next_tile, dir)
            else:
                next((current[0] + UP[0], current[1] + UP[1]), UP)
                next((current[0] + DOWN[0], current[1] + DOWN[1]), DOWN)

        elif tile_symbol == '\\':
            if dir == UP:
                dir = LEFT
            elif dir == DOWN:
                dir = RIGHT
            elif dir == LEFT:
                dir = UP
            elif dir == RIGHT:
                dir = DOWN
            new_tile = (current[0] + dir[0], current[1] + dir[1])
            next(new_tile, dir)

        elif tile_symbol == '/':
            if dir == UP:
                dir = RIGHT
            elif dir == DOWN:
                dir = LEFT
            elif dir == LEFT:
                dir = DOWN
            elif dir == RIGHT:
                dir = UP
            new_tile = (current[0] + dir[0], current[1] + dir[1])
            next(new_tile, dir)


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

