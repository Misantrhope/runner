import pygame
import os

# Начало программы
pygame.init()

W, H = 800, 447
win = pygame.display.set_mode((W, H))
pygame.display.set_caption('Side Scroller')

bg = pygame.image.load('data\images\loop.png').convert()
bg_x1 = 0
bg_x2 = bg.get_width()

clock = pygame.time.Clock()


class Player:
    run = [pygame.image.load(os.path.join('data\images', str(x) + '.png')) for x in range(8, 16)]
    jump = [pygame.image.load(os.path.join('data\images', str(x) + '.png')) for x in range(1, 8)]
    slide = [pygame.image.load(os.path.join('data\images', 'S1.png')),
             pygame.image.load(os.path.join('data\images', 'S2.png')),
             pygame.image.load(os.path.join('data\images', 'S2.png')),
             pygame.image.load(os.path.join('data\images', 'S2.png')),
             pygame.image.load(os.path.join('data\images', 'S2.png')),
             pygame.image.load(os.path.join('data\images', 'S2.png')),
             pygame.image.load(os.path.join('data\images', 'S2.png')),
             pygame.image.load(os.path.join('data\images', 'S2.png')),
             pygame.image.load(os.path.join('data\images', 'S3.png')),
             pygame.image.load(os.path.join('data\images', 'S4.png')),
             pygame.image.load(os.path.join('data\images', 'S5.png'))]
    jump_list = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4,
                4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1,
                -1, -1, -1, -1, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3,
                -3, -3, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4]

    # Массив для скорости прыжка

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.sliding = False
        self.slide_count = 0
        self.jump_count = 0
        self.run_count = 0
        self.slide_up = False

    def draw(self, win):
        if self.jumping:
            self.y -= self.jump_list[self.jump_count] * 1.2
            win.blit(self.jump[self.jump_count // 18], (self.x, self.y))
            self.jump_count += 1
            if self.jump_count > 108:
                self.jump_count = 0
                self.jumping = False
                self.runCount = 0
        elif self.sliding or self.slide_up:
            if self.slide_count < 20:
                self.y += 1
            elif self.slide_count == 80:
                self.y -= 19
                self.sliding = False
                self.slide_up = True
            if self.slide_count >= 110:
                self.slide_count = 0
                self.slide_up = False
                self.run_count = 0
            win.blit(self.slide[self.slide_count // 10], (self.x, self.y))
            self.slide_count += 1

        else:
            if self.run_count > 42:
                self.run_count = 0
            win.blit(self.run[self.run_count // 6], (self.x, self.y))
            self.run_count += 1


def redraw_window():
    win.blit(bg, (bg_x1, 0))
    win.blit(bg, (bg_x2, 0))
    runner.draw(win)
    pygame.display.update()


# main
runner = Player(200, 313, 64, 64)
pygame.time.set_timer(USEREVENT + 1, 500)
speed = 30
run = True
while run:
    redraw_window()
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
        if event.type == USEREVENT + 1:
            speed += 1

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        if not(runner.jumping):
            runner.jumping = True
    if keys[pygame.K_DOWN]:
        if not(runner.sliding):
            runner.sliding = True


