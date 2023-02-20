import random
from settings import *
import pygame
from numba.core import types
from numba.typed import Dict
from numba import int64, float64

matrix_map = [[0 for j in range(24)] for i in range(16)]
empty_map = []
for i in range(24): matrix_map[0][i] = 1
for i in range(24): matrix_map[15][i] = 1
for i in range(16): matrix_map[i][0] = 1
for i in range(16): matrix_map[i][23] = 1
for i in range(0, 16):
    for j in range(0, 24):
        if matrix_map[i][j] == 0:
            empty_map.append((i + random.randint(0, 9) * 0.1, j + random.randint(0, 9) * 0.1))

random.shuffle(empty_map)

for i in range(50):
    matrix_map[random.randint(1, 15)][random.randint(1, 23)] = 1
for i in range(len(matrix_map)):    #генерация разных стен
    for j in range(len(matrix_map[i])):
        if matrix_map[i][j] == 2 or matrix_map[i][j] == 1:
            matrix_map[i][j] = random.randint(2, 4)
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
