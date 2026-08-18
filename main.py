import pygame, random
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

SHOOT_LASER = pygame.USEREVENT
pygame.time.set_timer(SHOOT_LASER, 300)

MYSTERYSHIP = pygame.USEREVENT + 1
pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == SHOOT_LASER:
            game.alien_shoot()

        if event.type == MYSTERYSHIP:
            game.create_mystery()
            pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))

    # Updating
    game.spaceship_group.update()
    game.move_aliens()
    game.alien_lasers_group.update()
    game.mystery_ship_group.update()

    # Drawing
    screen.fill(BG_COLOR)
    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.laser_group.draw(screen)
    
    for obstacle in game.obstacles:
        obstacle.block_group.draw(screen)

    game.alien_group.draw(screen)
    game.alien_lasers_group.draw(screen)

    game.mystery_ship_group.draw(screen)

    pygame.display.update()
    clock.tick(60)


