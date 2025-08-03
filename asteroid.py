from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.x = x
        self.y = y
        self.radius = radius
    def draw(self, screen):
        pygame.draw.circle(screen, (221, 71, 255), self.position, self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt