from circleshape import CircleShape
import pygame
from constants import *
import random

pygame.mixer.init()
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    def draw(self, screen):
        pygame.draw.circle(screen, (221, 71, 255), self.position, self.radius, 2)
    def update(self, dt):
        if self.position.x > SCREEN_WIDTH + 65:
            self.position.x = 0
        if self.position.y > SCREEN_HEIGHT + 65:
            self.position.y = 0
        if self.position.x < 0 - 65:
            self.position.x = SCREEN_WIDTH
        if self.position.y < 0 - 65:
            self.position.y = SCREEN_HEIGHT
        self.position += self.velocity * dt
    def split(self):
        BANG.play()
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            new_velocity1 = self.velocity.rotate(angle)
            new_velocity2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = new_velocity1 * 1.5
            new_asteroid2.velocity = new_velocity2 * 1.5