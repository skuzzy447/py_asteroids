from circleshape import *
from constants import *
import pygame
import main
pygame.mixer.init()

class Player(CircleShape):
    def __init__(self, x,y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.is_sprinting = False
        self.current_speed = 0
        self.is_moving_backwards = False
        self.shoot_timer = 0
    #create points for drawing player
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    #draw player
    def draw(self, screen):
        if main.lives > 0:
            pygame.draw.polygon(screen, (71, 197, 255), self.triangle(), 2)
    
    #rotate player
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED *dt
    
    #update player
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.rotate(dt,)
        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_w]:
            self.is_moving_backwards = False
            self.move(dt, True)
        if keys[pygame.K_s]:
            self.is_moving_backwards = True
            self.move(dt, True)
        if keys[pygame.K_SPACE] and self.shoot_timer <= 0:
            self.shoot()
        if keys[pygame.K_LSHIFT]:
            self.is_sprinting = True
        else:
            self.is_sprinting = False
        if not keys[pygame.K_s] and not keys[pygame.K_w] and self.current_speed > 0:
            self.move(dt, False)
        
        if self.current_speed > 300:
            self.current_speed = 300
        if self.current_speed < 0: 
            self.current_speed = 0
        if self.shoot_timer > 0:
            self.shoot_timer -= dt
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.y > SCREEN_HEIGHT:
            self.position.y = 0
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
            
    #move player
    def move(self, dt, key_pressed):
        if self.is_sprinting:
            dt *= 2
        if self.current_speed < PLAYER_MAX_SPEED and key_pressed:
            self.current_speed += 5
        else:
            self.current_speed -= 5
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        if self.is_moving_backwards:
            forward = -forward
        self.position += forward * self.current_speed * dt

    def shoot(self):
        FIRE.play()
        new_shot = Shot(self.position.x, self.position.y, PLAYER_SHOT_RADIUS)
        new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shoot_timer = PLAYER_SHOOT_TIMER

    def collide(self):
        main.lives -= 1
        print(f"{main.lives} lives remaining")
        self.kill()
        if main.lives <= 0:
            print("Game Over")
            return False
        else:
            return True

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, (66, 102, 245), self.position, self.radius, 1)
    def update(self, dt):
        self.position += self.velocity * dt
