import pygame
from game import Game

pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 800
BG_COLOR = (0,0,0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()
run = True

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Updating
    game.spaceship_group.update()


    # Drawing
    screen.fill(BG_COLOR)
    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.laser_group.draw(screen)
    
    for obstacle in game.obstacles:
        obstacle.block_group.draw(screen)

    game.alien_group.draw(screen)

    pygame.display.update()
    clock.tick(60)


