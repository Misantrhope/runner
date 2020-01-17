import pygame
import os


class Saw:
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
        # Счётчик фреймов, нужен чтобы определить какую картинку отображать на экране.
        self.death_sound = pygame.mixer.Sound('data\sounds\death.wav')

    def draw(self, win):
        self.hitbox = (self.x + 5, self.y + 5, self.width - 12, self.height - 5)
        # Hitbox спрайта
        if self.count >= 8:
            self.count = 0
            # Обнуляем счётчик
        win.blit(pygame.transform.scale(self.img[self.count // 2], (48, 48)), (self.x, self.y))
        # На каждую картинку по 2 фрейма,
        self.count += 1
        # Обновляем счётчик
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        # Отображает на экране hitbox спрайта

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            # Проверяем если x координата игрока сталкиваеться с чем либо.
            if rect[1] + rect[3] > self.hitbox[1]:
                # Проверяем если y координата игрока сталкиваеться с чем либо.
                self.death_sound.play()
                return True
            return False
