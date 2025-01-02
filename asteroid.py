import pygame
import random
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, asteroids):
        super().__init__(x, y, radius)
        self.asteroids = asteroids

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.color.Color("white"), self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            # self.kill()
            return
        
        rnd_angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(rnd_angle) * 1.2
        velocity2 = self.velocity.rotate(-rnd_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius, self.asteroids)
        asteroid1.velocity = velocity1
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius, self.asteroids)
        asteroid2.velocity = velocity2
        self.asteroids.add(asteroid1)
        self.asteroids.add(asteroid2)