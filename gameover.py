import pygame
from constants import *

def display_game_over(screen):
    game_over = pygame.image.load('/home/rgugler/workspace/asteroids/images/gameover.jpg')
    game_over_rect = game_over.get_rect()
    game_over_rect.center = screen.get_rect().center
    
    screen.fill(color="white")
    screen.blit(game_over, game_over_rect)
    pygame.display.flip()
    pygame.time.wait(2500)

    pygame.quit()
    exit()