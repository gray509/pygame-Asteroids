from constants import *
import pygame
def main():
    pygame.init()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while(True):
        screen.fill((0,0,0))
        pygame.display.flip()
    

if __name__ == "__main__":
    main()

