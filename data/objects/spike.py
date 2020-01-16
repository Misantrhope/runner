import os
import pygame
import sys
from data.objects.saw import Saw

sys.path.append('data/objects')


class Spike(Saw):
    img = pygame.image.load(os.path.join('data\images', 'spike.png'))

    def draw(self, win):
        self.hitbox = (self.x + 10, self.y, 28, 315)
        win.blit(self.img, (self.x, self.y))
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def collide(self, rect):
        # Проверяем если x координата игрока сталкиваеться с чем либо.
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            # Проверяем если y координата игрока сталкиваеться с чем либо.
            if rect[1] < self.hitbox[3]:
                self.death_sound.play()
                return True

            return False
