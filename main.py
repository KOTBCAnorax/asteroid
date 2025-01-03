import pygame
from asteroidfield import AsteroidField
from player import Player
from asteroid import Asteroid
from shot import Shot
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS, shots)
    asteroidfield = AsteroidField(asteroids)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(pygame.Color(0, 0, 0))
        update(updatable, dt)
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("GAME OVER")
                return
            for shot in shots:
                if shot.is_colliding(asteroid):
                    shot.kill()
                    asteroid.split()

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