import pygame, random
from spaceship import Spaceship
from obstacle import Obstacle
from obstacle import grid
from alien import Alien
from laser import Laser
from alien import MysteryShip

class Game:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.spaceship_group = pygame.sprite.GroupSingle()
        self.spaceship_group.add(Spaceship(self.screen_width, self.screen_height))
        spaceship = self.spaceship_group.sprite
        spaceship.image = pygame.transform.scale(spaceship.image, (45, 35))
        spaceship.rect = spaceship.image.get_rect(center=spaceship.rect.center)
        self.obstacles = self.create_obstacles()
        self.alien_group = pygame.sprite.Group()
        self.create_aliens()
        self.aliens_direction = 1
        self.alien_lasers_group = pygame.sprite.Group()
        self.mystery_ship_group = pygame.sprite.GroupSingle()

    def create_obstacles(self):
        obstacle_width = len(grid[0]) * 3
        gap = (self.screen_width - (4 * obstacle_width)) / 5
        obstacles = []

        for i in range(4):
            offset_x = (i + 1)  * gap + i * obstacle_width
            obstacle = Obstacle(offset_x, self.screen_height - 100)
            obstacles.append(obstacle)
        return obstacles
    
    def create_aliens(self):
        for row in range(5):
            for column in range(11):
                x = 75 + column * 50
                y = 110 + row * 50

                if row == 0:
                    alien_type = 3

                elif row in (1,2):
                    alien_type = 2

                else:
                    alien_type = 1

                alien = Alien(alien_type, x, y)
   

                alien.image = pygame.transform.scale(alien.image, (40, 40))
                alien.rect = alien.image.get_rect(center=alien.rect.center)

                self.alien_group.add(alien)


    def move_aliens(self):
        self.alien_group.update(self.aliens_direction)

        alien_sprites = self.alien_group.sprites()

        for alien in alien_sprites:
            if alien.rect.right >= self.screen_width:
                self.aliens_direction = -1
                self.alien_move_down(2)

            elif alien.rect.left <= 0:
                self.aliens_direction = 1
                self.alien_move_down(2)


    def alien_move_down(self, distance):
        if self.alien_group:
            for alien in self.alien_group.sprites():
                alien.rect.y += distance

    def alien_shoot(self):
        if self.alien_group.sprites():
            random_alien = random.choice(self.alien_group.sprites())
            laser_sprite = Laser(random_alien.rect.center, -6, self.screen_height)
            self.alien_lasers_group.add(laser_sprite)

    
    def create_mystery(self):
        self.mystery_ship_group.add(MysteryShip(self.screen_width))
        mystery_ship = self.mystery_ship_group.sprite
        mystery_ship.image = pygame.transform.scale(mystery_ship.image, (50, 30))
        mystery_ship.rect = mystery_ship.image.get_rect(center=mystery_ship.rect.center)


