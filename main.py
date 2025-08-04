from constants import *
import pygame
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
lives = 3

def main():
    pygame.display.set_caption("It's Party Time!!!")
    running = True
    death_timer = 0
    score = 0
    dt = 0
    #initialize pygame and start music
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    pygame.mixer_music.load("./sounds/music.mp3")
    pygame.mixer_music.play(-1)
    #create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    #set object groups
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (bullets, updatable, drawable)
    #create objects
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    asteroid_field = AsteroidField()
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    #game loop
    while running:
        #when death timer is greater than 0 player is invinceble
        if death_timer > 0:
            death_timer -= dt
        #allows program to be closed regularly
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #checks each asteroid for collisions with bullets and/or the player
        for each in asteroids:
            for bullet in bullets:
                if each.check_collision(bullet):
                    score += 1
                    each.split()
                    bullet.kill() 
            if each.check_collision(player1) and death_timer <= 0:
                death_timer = PLAYER_DEATH_TIMER
                running = player1.collide()
                player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        updatable.update(dt)
        asteroid_field.increase_difficulty(score)
        screen.fill("black")
        #game border
        pygame.draw.rect(screen, (255, 54, 151), (0 + SCREEN_WIDTH * .001, 0 + SCREEN_HEIGHT * .002, SCREEN_WIDTH - SCREEN_WIDTH * .0015, SCREEN_HEIGHT - SCREEN_HEIGHT * .0035), 2)
        for each in drawable:
            each.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60) / 1000)
    #game over screen
    font = pygame.font.SysFont("Arial", 50)
    game_over = font.render("Game Over", False, (127, 59, 255))
    ending_score = font.render(str(score), False, (127, 59, 255))
    game_over_rect = game_over.get_rect()
    ending_score_rect = ending_score.get_rect()
    game_over_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2- 25)
    ending_score_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 25)
    waiting = True
    #waits for escape key before closing program
    while waiting:
        screen.blit(game_over, game_over_rect)
        screen.blit(ending_score, ending_score_rect)
        pygame.display.flip() 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:            
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:           
                    waiting = False
            if event.type == pygame.QUIT:
                waiting = False



if __name__ == "__main__":
    main()
