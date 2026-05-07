import pygame
import os

BULLET_IMAGE = pygame.image.load(os.path.join('img', 'bullet_image.png'))

class Game:
    def __init__(self, font, FPS, lives, window, screen_width, screen_height, level, clock):
        self.font = font
        self.FPS = FPS
        self.lives = lives
        self.window = window
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.level = level
        self.clock = clock
        self.bullets = 0
        self.bullet_img = BULLET_IMAGE
        self.max_pun = 0
        
        registros = self.leer_registros("puntajes.txt")
        if len(registros) > 0:
            for registro in registros:
                try:
                    nombre, puntaje = registro.strip().split(',')
                    puntaje = int(puntaje)
                    if puntaje > self.max_pun:
                        self.max_pun = puntaje
                except:
                    pass

    def leer_registros(self, filename):
        try:
            with open(filename, "r") as f:
                return f.readlines()
        except FileNotFoundError:
            return []

    def over(self):
        if self.lives <= 0:
            return True
        return False

    def escape(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return True
            
        return False

    def reload_bullet(self, count):
        self.bullets = count

    def draw_HUD(self):
        lives_label = self.font.render(f"Vidas: {self.lives}", 1, (255,255,255))
        self.window.blit(lives_label, (10, 10))
        
        level_label = self.font.render(f"Nivel: {self.level}", 1, (255,255,255))
        self.window.blit(level_label, (self.screen_width - level_label.get_width() - 10, 10))
        
        bullets_label = self.font.render(f"Balas: {self.bullets}", 1, (255,255,255))
        self.window.blit(bullets_label, (10, 60))