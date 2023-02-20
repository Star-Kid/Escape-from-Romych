import random
from settings import *
import pygame
from numba.core import types
from numba.typed import Dict
from numba import int64, float64

_ = False
matrix_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #загрузка карты с помощью двух мерного массива
    [1, _, _, _, _, _, 2, _, _, _, _, _, _, _, _, _, _, 2, _, _, _, _, _, 1],
    [1, _, 2, 2, _, _, _, _, _, 2, 2, 2, _, _, _, 2, _, _, _, _, 2, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 2, 2, _, _, _, 2, _, _, _, _, _, _, 1],
    [1, _, 2, 2, _, _, _, _, _, _, _, _, 2, _, 2, _, _, 2, _, _, _, 2, _, 1],
    [1, _, _, _, _, _, 2, _, _, 2, 2, _, 2, _, _, _, _, _, _, 2, _, _, _, 1],
    [1, _, 2, _, _, _, 2, _, _, 2, _, _, 2, _, _, _, 2, _, _, _, _, 2, _, 1],
    [1, _, _, 2, _, _, 2, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, 2, _, _, _, _, _, _, _, 2, _, _, 2, 2, _, _, _, _, 2, 2, _, _, 1],
    [1, _, 2, _, _, _, 2, 2, _, 2, _, _, _, 2, 2, _, _, _, _, 2, 2, _, _, 1],
    [1, _, _, _, _, 1, _, 2, _, _, 2, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, 2, _, 2, _, _, _, _, 2, _, _, 2, _, _, _, _, _, _, _, _, 2, _, 1],
    [1, _, _, _, _, _, 2, _, _, _, _, _, 2, 2, _, _, _, _, _, _, 2, 2, _, 1],
    [1, _, _, 2, _, _, _, _, 2, _, _, _, _, 2, 2, 2, _, 2, 2, 2, 2, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, 2, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
for i in range(len(matrix_map)):    #генерация разных стен
    for j in range(len(matrix_map[i])):
        if matrix_map[i][j] == 2 or matrix_map[i][j] == 1:
            matrix_map[i][j] = random.randint(2, 4)

WORLD_WIDTH = len(matrix_map[0]) * TILE
WORLD_HEIGHT = len(matrix_map) * TILE
world_map = {}
collision_walls = []
for j, row in enumerate(matrix_map): #создания карты и загрузка стен в неё
    for i, char in enumerate(row):
        if char:
            collision_walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
            if char == 1:
                world_map[(i * TILE, j * TILE)] = 1
            elif char == 2:
                world_map[(i * TILE, j * TILE)] = 2
            elif char == 3:
                world_map[(i * TILE, j * TILE)] = 3
            elif char == 4:
                world_map[(i * TILE, j * TILE)] = 4
