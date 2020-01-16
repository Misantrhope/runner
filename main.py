import pygame
import os
import sys
from data.objects.player import Player
from data.objects.saw import Saw
from data.objects.spike import Spike
import random

sys.path.append('data/objects')

# Начало программы
pygame.init()

w, h = 800, 447
win = pygame.display.set_mode((w, h))
pygame.display.set_caption('Runner')
hit_sound = pygame.mixer.Sound('data\sounds\hit.wav')
bg = pygame.image.load('data\images\loop.png').convert()
music = pygame.mixer.music.load('data\sounds\music.wav')

bg_x1 = 0
bg_x2 = bg.get_width()

clock = pygame.time.Clock()


def update_scores():
    f = open('data/scores.txt', 'r')
    file = f.readlines()
    last_score = int(file[0])

    if last_score < int(score):
        f.close()
        file = open('data/scores.txt', 'w')
        file.write(str(score))
        file.close()

        return score

    return last_score


def redraw_window():
    win.blit(bg, (bg_x1, 0))
    win.blit(bg, (bg_x2, 0))
    runner.draw(win)
    for i in objects:
        i.draw(win)
    font = pygame.font.SysFont('comicsans', 30)
    text = font.render('Счёт:' + str(score), 1, (255, 255, 255))
    win.blit(text, (700, 10))
    pygame.display.update()


def end():
    pygame.mixer.music.stop()
    global pause, objects, speed, score
    pause = 0
    objects = []
    speed = 100
    run = True
    while run:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if keys[pygame.K_RETURN]:
                pygame.mixer.music.play(-1)
                hit_sound.play()
                run = False
        win.blit(bg, (0, 0))
        font_2 = pygame.font.SysFont('comicsans', 80)
        font_3 = pygame.font.SysFont('comicsans', 30)
        previous_score = font_2.render('Рекорд:' + str(update_scores()), 1, (255, 255, 255))
        win.blit(previous_score, (w / 2 - previous_score.get_width() / 2, 100))
        new_score = font_2.render('Счёт:' + str(score), 1, (255, 255, 255))
        win.blit(new_score, (w / 2 - new_score.get_width() / 2, 220))
        continue_text = font_3.render('Нажмите Enter чтобы начать новую игру', 1, (255, 255, 255))
        win.blit(continue_text, (w / 2 - new_score.get_width() / 2, 340))
        pygame.display.update()

    score = 0
    runner.game_over = False


def start():
    a = True
    intro_text = ["",
                  "Spacebar - прыжок",
                  "S - проскользить",
                  'Нажмите на Enter чтобы начать игру']
    fon = pygame.image.load(os.path.join('data\images', 'loop.png'))
    win.blit(fon, (0, 0))
    font = pygame.font.SysFont('comicsans', 30)
    text_coord = 170
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        win.blit(string_rendered, intro_rect)
    global running
    while a:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                pygame.mixer.music.play(-1)
                hit_sound.play()
                running = True
                a = False
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()


# main
start()
runner = Player(200, 313, 64, 64)
pygame.time.set_timer(pygame.USEREVENT + 1, 500)
pygame.time.set_timer(pygame.USEREVENT + 2, random.randrange(1500, 1750))
# Диапазон генерации
speed = 100

pause = 0
fall_speed = 0

objects = []
while running:
    score = speed // 5 - 20
    # Т.к изначально speed = 100 , а 100/5 = 20 , то счёт начнётся с 20, поэтому вычтем 20 изначально.
    if pause > 0:
        pause += 1
        if pause > fall_speed // 2:
            end()

    for i in objects:
        if i.collide(runner.hitbox):
            runner.game_over = True
            if pause == 0:
                fall_speed = speed
                pause = 1

        i.x -= 1.4
        if i.x < -i.width * -1:
            objects.pop(objects.index(i))
            # Удаление обьектов с экрана
    bg_x1 -= 1.4
    bg_x2 -= 1.4
    if bg_x1 < bg.get_width() * - 1:
        bg_x1 = bg.get_width()
    if bg_x2 < bg.get_width() * - 1:
        bg_x2 = bg.get_width()
        # Прокрутка экрана

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.USEREVENT + 1:
            speed += 1
        if event.type == pygame.USEREVENT + 2:
            r = random.randrange(0, 2)
            if r == 0:
                objects.append(Saw(810, 326, 48, 48))
            else:
                objects.append(Spike(810, 0, 48, 320))
            # Генератор обьектов

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        if not runner.jumping:
            runner.jumping = True
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        if not runner.sliding:
            runner.sliding = True
    clock.tick(speed)
    redraw_window()
