import pygame
import os

class Saw():
    img = [pygame.image.load(os.path.join('data\images', 'SAW0.png')),
           pygame.image.load(os.path.join('data\images', 'SAW1.png')),
           pygame.image.load(os.path.join('data\images', 'SAW2.png')),
           pygame.image.load(os.path.join('data\images', 'SAW3.png'))]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (x, y, width, height)
        self.count = 0

    def draw(self, win):
        self.hitbox = (self.x + 5, self.y + 5, self.width - 12, self.height - 5)
        if self.count >= 8:
            self.count = 0
        win.blit(pygame.transform.scale(self.img[self.count // 2], (64, 64)), (self.x, self.y))
        self.count += 1
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
    def collide(self, rect):
        # Проверяем если x координата игрока сталкиваеться с чем либо.
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            # Проверяем если y координата игрока сталкиваеться с чем либо.
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
            return False