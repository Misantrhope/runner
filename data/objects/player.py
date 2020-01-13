import pygame
import os
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
    jump_list = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4,
                 4,
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