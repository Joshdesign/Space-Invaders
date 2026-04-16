import pygame

#Clase Bullets (balas)

class Bullet:
        def __init__(self, x, y, img):
                self.x = x
                self.y = y
                self.img = img
                self.mask = pygame.mask.from_surface(self.img)

        def draw(self, window):
                window.blit(self.img, (self.x, self.y))

        def move(self, speed):
                self.y += speed

        def collision(self, obj):
            offset = (int(obj.x - self.x), int(obj.y - self.y))
            return self.mask.overlap(obj.mask, offset)