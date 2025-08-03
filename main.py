from constants import *
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)

    asteroid_field = AsteroidField()
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    pygame.display.set_caption("It's Party Time!!!")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        screen.fill("black")
        for each in drawable:
            each.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60) / 1000)


if __name__ == "__main__":
    main()
