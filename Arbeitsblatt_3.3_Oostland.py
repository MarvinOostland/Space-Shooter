import pygame
import os
import random

class Settings:
    window_width = 800
    window_height = 600
    window_border = 60
    asteriod_speed = 5

pygame.display.set_caption("Space Shooter")
# Hintergrund
background = pygame.image.load("images/background.jpg")
background = pygame.transform.scale(background, (Settings.window_width,Settings.window_height))

if __name__ == "__main__":
    os.environ['SDL_VIDEO_WINDOWS_POS'] = "10 ,50 "
    pygame.init()

    screen = pygame.display.set_mode((Settings.window_width,Settings.window_height))
    clock = pygame.time.Clock()
    clock.tick(60)
class Ship:
    ship = pygame.image.load("images/ship.png")
    ship = pygame.transform.scale(ship,(50,48))
    rect = ship.get_rect()
    rect.centerx= Settings.window_width // 2
    rect.bottom= Settings.window_height - Settings.window_border
class Asteriod:    
    asteroid = pygame.image.load("images/Asteroid Brown.png")
    asteroid = pygame.transform.scale(asteroid,(80,80))
    rect = asteroid.get_rect()
    

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background, (0,0))
        screen.blit(Ship.ship,(Ship.rect.centerx,Ship.rect.bottom))
        screen.blit(asteroid, (400,40))
        pygame.display.flip()

pygame.quit()
