import pygame
import os

BULLET_IMAGE = pygame.image.load(os.path.join('img', 'bullet_image.png'))

class Game:
    def __init__(self,window, sceen_width, screen_height, bullets = 0, clock = pygame.time.Clock()):
        self.window = window
        self.screen_width = sceen_width
        self.screen_height = screen_height
        self.bullets = bullets
        self.clock = clock
        self.bullet_img = BULLET_IMAGE
        registros = self.leer_registros("puntajes.txt")
        if len(registros) == 0:
            self