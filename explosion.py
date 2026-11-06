import pygame
from imageload import image_load_explosion
from circleshape import CircleShape
from constants import *

class Explosion(CircleShape):
    
    def __init__(self, screen, x, y):
        super().__init__(x, y, EXPLOSION_RADIUS)
        self.x = x
        self.y = y
        self.EXPLOSION_RADIUS = EXPLOSION_RADIUS
        
        self.images = image_load_explosion()
        self.anim_index = 0 
        self.anim_timer = 0
        
    def update(self, dt):
        self.anim_timer += dt
        if self.anim_timer > 1 * dt:
            self.anim_index += 1
            self.anim_timer = 0
            if self.anim_index >= 17:
                self.kill()
    
    
    def draw(self, screen):
        screen.blit(self.images[self.anim_index], (self.x, self.y))

                

