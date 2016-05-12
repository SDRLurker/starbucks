#!/usr/bin/python
# -*- coding: utf-8 -*-

def get_max_product(grid, tox, toy, plusx, plusy, fromx = 0):
    max_product = -1
    for y in range(toy):
        for x in range(tox):
            p = 1
            for i in range(4):
                p *= grid[y+(plusy*i)][x+(plusx*i)]
            max_product = max(p, max_product)
    return max_product

def largest_product(grid):
    max_product = -1
    max_product = max(max_product, get_max_product(grid, 20-3, 20, 1, 0))
    max_product = max(max_product, get_max_product(grid, 20, 20-3, 0, 1))
    max_product = max(max_product, get_max_product(grid, 20-3, 20-3, 1, 1))
    max_product = max(max_product, get_max_product(grid, 20, 20-3, -1, 1, 3))
    return max_product

grid = []
for _ in range(20):
    row_str = raw_input()
    row = [int(x) for x in row_str.split()]
    row = row[:20]
    grid.append(row)
print largest_product(grid)