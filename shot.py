import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SPEED

class Shot(CircleShape):
    def __init__(self, x, y, direction):
        super().__init__(x, y, SHOT_RADIUS)
        unit_vector = pygame.Vector2(0, 1)
        self.velocity = unit_vector.rotate(direction) * PLAYER_SPEED * 2
        
    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius)
        
    def update(self, dt):
        self.position += self.velocity * dt