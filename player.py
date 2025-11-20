import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_SPEED,  PLAYER_TURN_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, cd_timer=0.0):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cd_timer = cd_timer          
        
    def triangle(self):
        base = pygame.Vector2(0, 1)
        forward = base.rotate(self.rotation)
        right = base.rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
        
    def rotate(self, direction, dt):
        self.rotation += direction * PLAYER_TURN_SPEED * dt
        
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1, dt)
        if keys[pygame.K_d]:
            self.rotate(1, dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.cd_timer <= 0.0:
                self.shoot()
                self.cd_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        self.cd_timer -= dt
        if self.cd_timer < 0.0:
            self.cd_timer = 0.0
            
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
        
    def shoot(self):
        shot = Shot(self.position.x, self.position.y, self.rotation)
        velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        shot.velocity = velocity
        return shot