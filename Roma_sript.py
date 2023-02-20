import optparse
import os
import sys

from settings import *
from map import world_map
from ray_casting import mapping
import math
from map import empty_map
import drawing



def ray_casting_npc_player(npc_x, npc_y, world_map, player_pos):
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    delta_x, delta_y = ox - npc_x, oy - npc_y
    cur_angle = math.atan2(delta_y, delta_x)
    cur_angle += math.pi

    sin_a = math.sin(cur_angle)
    sin_a = sin_a if sin_a else 0.000001
    cos_a = math.cos(cur_angle)
    cos_a = cos_a if cos_a else 0.000001

    # verticals
    x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
    for i in range(0, int(abs(delta_x)) // TILE):
        depth_v = (x - ox) / cos_a
        yv = oy + depth_v * sin_a
        tile_v = mapping(x + dx, yv)
        if tile_v in world_map:
            return False
        x += dx * TILE

    # horizontals
    y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
    for i in range(0, int(abs(delta_y)) // TILE):
        depth_h = (y - oy) / sin_a
        xh = ox + depth_h * cos_a
        tile_h = mapping(xh, y + dy)
        if tile_h in world_map:
            return False
        y += dy * TILE
    return True


class Interaction:
    def __init__(self, player, sprites, drawing):
        self.player = player
        self.sprites = sprites
        self.drawing = drawing

    def npc_action(self, tick):
        for obj in self.sprites.list_of_objects:
            if obj.flag == 'npc':
                if ray_casting_npc_player(obj.x, obj.y,
                                          world_map, self.player.pos):
                    obj.npc_action_trigger = True
                    self.npc_move(obj, tick)
                else:
                    obj.npc_action_trigger = False

    def npc_move(self, obj, tick):
        if abs(obj.distance_to_sprite) > 50:
            dx = obj.x - self.player.pos[0]
            dy = obj.y - self.player.pos[1]
            obj.x = obj.x + roma_speed if dx < 0 else obj.x - roma_speed
            obj.y = obj.y + roma_speed if dy < 0 else obj.y - roma_speed
        elif abs(obj.distance_to_sprite) < 50:
            obj.x = int(empty_map[8][0]) * TILE
            obj.y = int(empty_map[8][1]) * TILE
            self.player.x, self.player.y = player_pos
            with open("record.txt", "a") as file:
                file.write(f" {tick}")
            file.close()
            os.system("main.py")
            exit()
            sys.exit()
