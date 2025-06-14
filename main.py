import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    fps = pygame.time.Clock()
    dt  = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_fields = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    
    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        screen.fill((0,0,0))

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                exit("Game over")
            for bullet in shots:
                if bullet.check_collision(asteroid):
                    asteroid.split()

        for draw in drawable:
            draw.draw(screen)
        
        pygame.display.flip()
        
        dt = fps.tick(60) / 1000
    

if __name__ == "__main__":
    main()

