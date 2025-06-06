import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
def main():
    pygame.init()
    fps = pygame.time.Clock()
    dt  = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids,updatable, drawable)
    AsteroidField.containers = (updatable)
    
    asteroids_fields = AsteroidField()
    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))
        
        updatable.update(dt)
        for draw in drawable:
            draw.draw(screen)
        
        pygame.display.flip()
        
        dt = fps.tick(60) / 1000
    

if __name__ == "__main__":
    main()

