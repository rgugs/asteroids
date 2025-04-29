import pygame
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        if Asteroid.containers:
            for container in Asteroid.containers:
                container.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        original_radius = self.radius
        if original_radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Spawn new asteroids
        random_angle = random.uniform(20,50)
        new_vector_1 = self.velocity.rotate(random_angle)
        new_vector_2 = self.velocity.rotate(-random_angle)
        new_radius = original_radius - ASTEROID_MIN_RADIUS

        split_1 = Asteroid(self.position.x, self.position.y, new_radius)
        split_2 = Asteroid(self.position.x, self.position.y, new_radius)

        split_1.velocity = new_vector_1 * 1.2
        split_2.velocity = new_vector_2 * 1.2