import pygame
import os
from objects import Player, Spike, Saw
import random

# Начало программы
pygame.init()

W, H = 800, 447
win = pygame.display.set_mode((W, H))
pygame.display.set_caption('Side Scroller')

bg = pygame.image.load('data\images\loop.png').convert()
bg_x1 = 0
bg_x2 = bg.get_width()

clock = pygame.time.Clock()


def redraw_window():
    win.blit(bg, (bg_x1, 0))
    win.blit(bg, (bg_x2, 0))
    runner.draw(win)
    for i in objects:
        i.draw(win)
    pygame.display.update()


# main
runner = Player(200, 313, 64, 64)
pygame.time.set_timer(pygame.USEREVENT + 1, 500)
pygame.time.set_timer(pygame.USEREVENT + 2, random.randrange(2500, 4500))
speed = 30
run = True
objects = []
while run:
    redraw_window()
    for i in objects:
        i.x -= 1.4
        if i.x < -i.width * -1:
            objects.pop(objects.index(i))
    clock.tick(speed)
    bg_x1 -= 1.4
    bg_x2 -= 1.4
    if bg_x1 < bg.get_width() * - 1:
        bg_x1 = bg.get_width()
    if bg_x2 < bg.get_width() * - 1:
        bg_x2 = bg.get_width()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.USEREVENT + 1:
            speed += 1
        if event.type == pygame.USEREVENT + 2:
            r = random.randrange(0, 2)
            if r == 0:
                objects.append(Saw(810, 310, 64, 64))
            else:
                objects.append(Spike(810, 0, 48, 320))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        if not (runner.jumping):
            runner.jumping = True
    if keys[pygame.K_DOWN]:
        if not (runner.sliding):
            runner.sliding = True
