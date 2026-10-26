import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)
        self.x = x
        self.y = y
        self.SHOT_RADIUS = SHOT_RADIUS
    
           
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.SHOT_RADIUS, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt