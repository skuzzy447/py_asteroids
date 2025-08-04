import pygame
import random
from asteroid import Asteroid
from constants import *
import main


class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0
        self.starting_velocity = 10

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100) + self.starting_velocity
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
    def increase_difficulty(self, score):
        if score >= 5:
            self.starting_velocity = 10
            ASTEROID_SPAWN_RATE = 1
        if score >= 10:
            self.starting_velocity = 20
            ASTEROID_SPAWN_RATE = 1.2
        if score >= 15:
            self.starting_velocity = 30
            ASTEROID_SPAWN_RATE = 1.4
        if score >= 20:
            self.starting_velocity = 40
            ASTEROID_SPAWN_RATE = 1.6
        if score >= 25:
            self.starting_velocity = 50
            ASTEROID_SPAWN_RATE = 1.8
        if score >= 30:
            self.starting_velocity = 60
            ASTEROID_SPAWN_RATE = 2