import pygame
from asteroidfield import AsteroidField
from player import Player
from asteroid import Asteroid
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(pygame.Color(0, 0, 0))
        update(updatable, dt)
        draw(drawable, screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000


def update(list, dt):
    for element in list:
        element.update(dt)

def draw(list, screen):
    for element in list:
        element.draw(screen)


if __name__ == "__main__":
    main()