import circleshape
from constants import *
import pygame
import random

class Asteroid(circleshape.CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill() 
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            vector1 = self.velocity.rotate(angle)
            vector2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = vector1 * 1.2
            asteroid2.velocity = vector2 * 1.2
