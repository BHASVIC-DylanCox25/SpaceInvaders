import pygame, sys, random
from game import Game

pygame.init()

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700
OFFSET = 50
BG_COLOR = (0,0,0)

font = pygame.font.Font("FONT/CosmicAlien.ttf", 30)
level_surface = font.render("LEVEL 01", False, (255,255,255))
game_over_surface = font.render("GAME OVER", False, (255, 255, 255))
score_text_surface = font.render("SCORE", False, (255, 255, 255))
highscore_text_surface = font.render("HI-SCORE", False, (255, 255, 255 ))

screen = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + (OFFSET*2)))
pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)

SHOOT_LASER = pygame.USEREVENT
pygame.time.set_timer(SHOOT_LASER, 300)

MYSTERYSHIP = pygame.USEREVENT + 1
pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SHOOT_LASER and game.run:
            game.alien_shoot()

        if event.type == MYSTERYSHIP and game.run:
            game.create_mystery()
            pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and game.run == False:
            game.reset()

    # Updating
    if game.run:
        game.spaceship_group.update()
        game.move_aliens()
        game.alien_lasers_group.update()
        game.mystery_ship_group.update()
        game.check_for_collisions()

    # Drawing
    screen.fill(BG_COLOR)
    #pygame.draw.rect(screen, (0, 255, 0), (10, 10, 780, 780), 2, 0, 60, 60, 60, 60)
    pygame.draw.line(screen, (0, 255, 0), (25, 730), (775, 730), 3)

    if game.run:
        screen.blit(level_surface, (570, 750, 50, 50))

    else:
        screen.blit(game_over_surface, (550, 740, 50, 50))

    x = 50
    for lfie in range(game.lives):
        screen.blit(game.spaceship_group.sprite.image, (x, 745))
        x += 50

    screen.blit(score_text_surface, (50, 15, 50, 50))
    formatted_score = str(game.score).zfill(5)
    score_surface = font.render(str(formatted_score), False, (255, 255, 255))
    screen.blit(score_surface, (50, 40, 50, 50))

    screen.blit(highscore_text_surface, (190, 15, 50, 50))
    formatted_highscore = str(game.highscore).zfill(5)
    highscore_surface = font.render(formatted_highscore, False, (255, 255, 255))
    screen.blit(highscore_surface, (220, 40, 50, 50))

    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.laser_group.draw(screen)
    
    for obstacle in game.obstacles:
        obstacle.block_group.draw(screen)

    game.alien_group.draw(screen)
    game.alien_lasers_group.draw(screen)

    game.mystery_ship_group.draw(screen)

    pygame.display.update()
    clock.tick(60)


