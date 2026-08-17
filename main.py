import pygame
from spaceship import Spaceship
from laser import Laser
from obstacle import Obstacle
pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")



BG_COLOR = (0,0,0)



spaceship = Spaceship(700, 800)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

obstacle = Obstacle()


clock = pygame.time.Clock()
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update Spacship
    spaceship_group.update()


    # Drawing
    screen.fill(BG_COLOR)
    spaceship_group.draw(screen)
    spaceship_group.sprite.laser_group.draw(screen)
    obstacle.block_group.draw(screen)

    pygame.display.update()
    clock.tick(60)


