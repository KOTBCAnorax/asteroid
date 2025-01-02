import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.color.Color("white"), self.position, 20)

    def update(self, dt):
        self.position += self.velocity * dt