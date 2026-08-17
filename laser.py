import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, position, speed, screen_height):
        super().__init__()
        self.image = pygame.Surface((4, 15))
        self.image.fill((0, 255, 0))
        self.speed = speed
        self.screen_height = screen_height
        self.rect = self.image.get_rect(center = position)


    def update(self):
        self.rect.y -= self.speed

        if self.rect.y > self.screen_height + 15 or self.rect.y < 0:
            self.kill()
