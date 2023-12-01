#!/usr/bin/env python3

import math
import os
import pathlib
import sys

from typing import List, Set, Tuple

sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent / 'lib'))

class Tile:
  def __init__(self: 'Tile', tile_id: int, data: List[str]) -> None:
    self.id = tile_id
    self.data = data

    self.edges = [
      "".join(row[-1] for row in data),
      self.data[-1],
      "".join(row[0] for row in data),
      self.data[0]
    ]

    self.uniqueid = "".join(self.edges)

  def left(self: 'Tile') -> str:
    return self.edges[2]

  def right(self: 'Tile') -> str:
    return self.edges[0]

  def top(self: 'Tile') -> str:
    return self.edges[3]

  def bottom(self: 'Tile') -> str:
    return self.edges[1]

  def rotate(self: 'Tile') -> 'Tile':
    return Tile(self.id, ["".join(r) for r in zip(*self.data[::-1])])

  def mirror_horizontal(self: 'Tile') -> 'Tile':
    return Tile(self.id, [r[::-1] for r in self.data])

  def mirror_vertical(self: 'Tile') -> 'Tile':
    return Tile(self.id, self.data[::-1])

  def image(self: 'Tile') -> List[List[str]]:
    return [row[1:-1] for row in self.data[1:-1]]


def parse_tiles(input_file: str) -> List[Tile]:
  tiles = []

  tile_id = None
  tile_data = []

  for line in open(input_file):
    line = line.strip()

    if line == "":
      tiles.append(Tile(tile_id, tile_data))
      tile_id = None
      tile_data = []

    elif line.startswith("Tile "):
      tile_id = int(line[5:-1])

    else:
      tile_data.append(line)

  if tile_id is not None:
    tiles.append(Tile(tile_id, tile_data))

  return tiles


def map_grid(tiles: List[Tile], grid: List[List[Tile]], seen: Set[int], pos: Tuple[int, int] = (0, 0)) -> List[List[int]]:
  x, y = pos
  if y == len(grid):
    return grid

  for tile in tiles:
    if tile.id in seen:
      continue

    if x > 0 and grid[y][x - 1].right() != tile.left():
      continue

    if y > 0 and grid[y - 1][x].bottom() != tile.top():
      continue

    grid[y][x] = tile
    result = map_grid(tiles, grid, seen | {tile.id}, (x + 1, y) if x < len(grid[0]) - 1 else (0, y + 1))
    if result is not None:
      grid = result
      break

    grid[y][x] = None

  else:
    grid = None

  return grid


def generate_grid(tiles: List[Tile], size: int) -> List[Tile]:
  candidates = []

  for tile in tiles:
    for r in range(2):
      candidates.append(tile)
      candidates.append(tile.mirror_horizontal())
      candidates.append(tile.mirror_vertical())
      candidates.append(candidates[-1].mirror_horizontal())
      tile = tile.rotate()

  return map_grid(candidates, [[None for _ in range(size)] for _ in range(size)], set())


def generate_pixels(grid: List[List[Tile]]) -> List[List[str]]:
  pixels = []
  for row in grid:
     pixel_row = [[] for _ in range(len(row[0].left()) - 2)]
     for tile in row:
       for i, image_row in enumerate(tile.image()):
         pixel_row[i] += [c for c in image_row]
     pixels += pixel_row

  return pixels


def find_sea_monsters(grid: List[List[Tile]]) -> List[List[str]]:

  def rotate(pixels: List[List[str]]) -> List[List[str]]:
    return [list(row) for row in zip(*pixels[::-1])]

  def mirror_horizontal(pixels: List[List[str]]) -> List[List[str]]:
    return [r[::-1] for r in pixels]

  def mirror_vertical(pixels: List[List[str]]) -> List[List[str]]:
    return pixels[::-1]


  pixels = generate_pixels(grid)
  for _ in range(2):
    if tag_sea_monsters(pixels):
      break

    pixels = mirror_horizontal(pixels)
    if tag_sea_monsters(pixels):
      break

    pixels = mirror_vertical(pixels)
    if tag_sea_monsters(pixels):
      break

    pixels = mirror_horizontal(pixels)
    if tag_sea_monsters(pixels):
      break

    pixels = rotate(mirror_vertical(pixels))

  return pixels


def tag_sea_monsters(pixels: List[List[str]]) -> int:
  x, y = 0, 0
  sea_monsters = 0

  rows = len(pixels)
  cols = len(pixels[0])

  while y < rows - 3:
    while x < cols - 20:
      if pixels[y + 1][x] == '#' and \
         pixels[y + 2][x + 1] == '#' and \
         pixels[y + 2][x + 4] == '#' and \
         pixels[y + 1][x + 5] == '#' and \
         pixels[y + 1][x + 6] == '#' and \
         pixels[y + 2][x + 7] == '#' and \
         pixels[y + 2][x + 10] == '#' and \
         pixels[y + 1][x + 11] == '#' and \
         pixels[y + 1][x + 12] == '#' and \
         pixels[y + 2][x + 13] == '#' and \
         pixels[y + 2][x + 16] == '#' and \
         pixels[y + 1][x + 17] == '#' and \
         pixels[y][x + 18] == '#' and \
         pixels[y + 1][x + 18] == '#' and \
         pixels[y + 1][x + 19] == '#':

        sea_monsters += 1
        pixels[y + 1][x] = '0'
        pixels[y + 2][x + 1] = 'O'
        pixels[y + 2][x + 4] = 'O'
        pixels[y + 1][x + 5] = 'O'
        pixels[y + 1][x + 6] = 'O'
        pixels[y + 2][x + 7] = 'O'
        pixels[y + 2][x + 10] = 'O'
        pixels[y + 1][x + 11] = 'O'
        pixels[y + 1][x + 12] = 'O'
        pixels[y + 2][x + 13] = 'O'
        pixels[y + 2][x + 16] = 'O'
        pixels[y + 1][x + 17] = 'O'
        pixels[y][x + 18] = 'O'
        pixels[y + 1][x + 18] = 'O'
        pixels[y + 1][x + 19] = 'O'

        x += 20

      else:
        x += 1

    x, y = 0, y + 1

  return sea_monsters


def calc_choppiness(image: List[List[str]]) -> int:
  return sum(row.count('#') for row in image)


def run() -> None:
  #input_file = aoc.inputfile('input1')

  tiles = parse_tiles("input1")
  size = int(math.sqrt(len(tiles)))

  grid = generate_grid(tiles, size)
  corners = grid[0][0].id * grid[0][-1].id * grid[-1][0].id * grid[-1][-1].id
  print(f'Corner multiple: {corners}')

  image = find_sea_monsters(grid)
  print(f'Choppiness: {calc_choppiness(image)}')


if __name__ == '__main__':
  run()
  sys.exit(0)
