import pygame
from settings import *
from player import Player
from sprite_objects import *
from ray_casting import ray_casting_walls
from drawing import Drawing, Time
from Roma_sript import *

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mouse.set_visible(False)
sc_map = pygame.Surface(MINIMAP_RES)

sprites = Sprites()
clock = pygame.time.Clock()
player = Player(sprites)
drawing = Drawing(sc, clock)
interaction = Interaction(player, sprites, drawing)
drawing.menu()
starttick = pygame.time.get_ticks()
tiime = Time(sprites, player, interaction, drawing, sc)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    sc.fill(BLACK)
    tick = (pygame.time.get_ticks() - starttick) / 1000


    drawing.background(player.angle)
    walls = ray_casting_walls(player, drawing.textures)
    drawing.world(walls + [obj.object_locate(player) for obj in sprites.list_of_objects])
    drawing.fps(clock)
    interaction.npc_action(tick)
    tiime.time(tick)

    pygame.display.flip()
    clock.tick(FPS)