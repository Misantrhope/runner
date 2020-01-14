import os
import pygame
import sys
sys.path.append('data/objects')
from data.objects.saw import Saw


class Spike(Saw):
    img = pygame.image.load(os.path.join('data\images', 'spike.png'))

    def draw(self, win):
        self.hitbox = (self.x + 10, self.y, 28, 315)
        win.blit(self.img, (self.x, self.y))
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
