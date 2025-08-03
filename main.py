from constants import *
import pygame
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

lives = 3


def main():
    pygame.init()
    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (bullets, updatable, drawable)

    asteroid_field = AsteroidField()
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    pygame.display.set_caption("It's Party Time!!!")
    running = True
    death_timer = 0
    while running:
        if death_timer > 0:
            death_timer -= dt
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for each in asteroids:
            for bullet in bullets:
                if each.check_collision(bullet):
                    each.kill()
                    bullet.kill() 
            if each.check_collision(player1) and death_timer <= 0:
                death_timer = PLAYER_DEATH_TIMER
                running = player1.collide()
                player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        screen.fill("black")
        for each in drawable:
            each.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60) / 1000)


if __name__ == "__main__":
    main()
