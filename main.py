from sys import exit
import pygame
from gameover import *
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shots import Shots

def main():
    #Initialize game and objects
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Asteroids')
    clock = pygame.time.Clock()
    
    #Variables
    dt = 0
    running = True

    # Create Groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set class containers
    AsteroidField.containers = updateable
    Asteroid.containers = (asteroids, updateable, drawable)
    Player.containers = (updateable, drawable)
    Shots.containers = (shots, updateable, drawable)

    # Initialize player and asteroid objects
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    asfield = AsteroidField()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        screen.fill(color="black")
        updateable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                display_game_over(screen)
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()
        for item in drawable:
            item.draw(screen)
 
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
    
    pygame.quit()
    exit()

if __name__ == "__main__":
    main()