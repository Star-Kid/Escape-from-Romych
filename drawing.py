import time

from Roma_sript import Interaction
from map import empty_map
import pygame
from settings import *
from random import randrange
import sys
from sprite_objects import SpriteObject



class Drawing:
    def __init__(self, sc, clock): #тестуры стен
        self.sc = sc
        self.clock = clock
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.textures = {1: pygame.image.load('img/wall1.png').convert(),
                         2: pygame.image.load('img/wall2.png').convert(),
                         3: pygame.image.load('img/brick_wall.jpg').convert(),
                         4: pygame.image.load('img/stone_wall.jpg').convert(),
                         'S': pygame.image.load('img/sky.png').convert()
                         }
        self.menu_trigger = True
        file = open('record.txt').read()
        self.record = [float(i) for i in file.split()]
        self.reroc_trigger = False
        self.menu_picture = pygame.image.load('img/bg.jpg').convert()

    def background(self, angle): #загрузка заднего фона
        sky_offset = -10 * math.degrees(angle) % WIDTH
        self.sc.blit(self.textures['S'], (sky_offset, 0))
        self.sc.blit(self.textures['S'], (sky_offset - WIDTH, 0))
        self.sc.blit(self.textures['S'], (sky_offset + WIDTH, 0))
        pygame.draw.rect(self.sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, world_objects):
        for obj in sorted(world_objects, key=lambda n: n[0], reverse=True): #создание отоброджаемой карты карты
            if obj[0]:
                _, object, object_pos = obj
                self.sc.blit(object, object_pos)

    def fps(self, clock): #отоброжение фпс
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, DARKORANGE)
        self.sc.blit(render, FPS_POS)


    def menu(self): #менюха
        x = 0
        button_font = pygame.font.SysFont('arial', 72)
        label_font = pygame.font.SysFont('arial', 150)
        start = button_font.render('START', 1, pygame.Color('lightgray'))
        button_start = pygame.Rect(0, 0, 400, 150)
        button_start.center = HALF_WIDTH, HALF_HEIGHT
        exit = button_font.render('EXIT', 1, pygame.Color('lightgray'))
        button_exit = pygame.Rect(0, 0, 400, 150)
        button_exit.center = HALF_WIDTH, HALF_HEIGHT + 200

        while self.menu_trigger:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.sc.blit(self.menu_picture, (0, 0), (x % 1920, 0, 1920, 1080))
            x += 1

            pygame.draw.rect(self.sc, BLACK, button_start, border_radius=25, width=10)
            self.sc.blit(start, (button_start.centerx - 130, button_start.centery - 70))

            pygame.draw.rect(self.sc, BLACK, button_exit, border_radius=25, width=10)
            self.sc.blit(exit, (button_exit.centerx - 85, button_exit.centery - 70))

            color = randrange(160)
            label = label_font.render('Escape from Romych', 1, (color, color, color))
            Record = button_font.render(f"Record: {max(self.record)}", 1, pygame.Color('lightgray'))
            self.sc.blit(Record, (HALF_WIDTH - 100, HALF_HEIGHT + 300))
            self.sc.blit(label, (15, -30))

            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()
            if button_start.collidepoint(mouse_pos):
                pygame.draw.rect(self.sc, RED, button_start, border_radius=25)
                self.sc.blit(start, (button_start.centerx - 130, button_start.centery - 70))
                if mouse_click[0]:
                    self.menu_trigger = False
            elif button_exit.collidepoint(mouse_pos):
                pygame.draw.rect(self.sc, BLACK, button_exit, border_radius=25)
                self.sc.blit(exit, (button_exit.centerx - 85, button_exit.centery - 70))
                if mouse_click[0]:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
            self.clock.tick(20)
class Time:
    def __init__(self, sprite, player, initer, drw, sc):
        self.seconds = 0
        self.sprite = sprite
        self.player = player
        self.initer = initer
        self.draw = drw
        self.sc = sc
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.i = 10

    def time(self, tick):
        self.seconds = tick
        render = self.font.render(str(self.seconds), 0, SANDY)
        self.sc.blit(render, TIME_POS)
        if self.seconds % 2.00 == 0:
            self.sprite.list_of_objects.append(SpriteObject(self.sprite.sprite_parameters['roma'], (empty_map[self.i])))
            self.i += 1
