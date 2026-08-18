import pygame
from laser import Laser

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.image.load("Images/Spaceship.png")
        self.rect = self.image.get_rect(midbottom = (self.screen_width / 2, self.screen_height + 10))
        self.speed = 6
        self.laser_group = pygame.sprite.Group()
        self.laser_ready = True
        self.laser_time = 0
        self.laser_delay = 300

    def get_user_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]: 
            self.rect.x += self.speed

        if keys[pygame.K_LEFT]: 
            self.rect.x -= self.speed

        if keys[pygame.K_SPACE] and self.laser_ready:
            self.laser_ready = False
            laser = Laser(self.rect.center, 5, self.screen_height)
            self.laser_group.add(laser)
            self.laser_time = pygame.time.get_ticks()

    def limits(self):
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width

        if self.rect.x < 0:
            self.rect.x = 0


    def laser_recharge(self):
        if not self.laser_ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_delay:
                self.laser_ready = True

    def update(self):
        self.get_user_input()
        self.limits()
        self.laser_group.update()
        self.laser_recharge()