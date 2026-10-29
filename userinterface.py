import pygame, sys
from constants import *
from logger import log_state, log_event

text_font = pygame.font.SysFont("Arial", 30)
health_amount = PLAYER_HEALTH

def draw_text(screen, text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))
    
class Score():
    def __init__(self, score_amount = 0):
        self.score_amount = score_amount
    
    def increase_score(self, score, increase, asteroid_radius):
        if asteroid_radius <= ASTEROID_MIN_RADIUS:
            self.score_amount += increase * 3
        elif ASTEROID_MIN_RADIUS < asteroid_radius < ASTEROID_MAX_RADIUS:
            self.score_amount += increase * 2
        else:
            self.score_amount += increase
            
class Health():
    def __init__(self, health_amount):
        self.health_amount = health_amount
        
    def health_decrease(self):
        self.health_amount -= 1

    def health_colour(self):
        if self.health_amount == 3:
            return (0,255,0)
        if self.health_amount == 2:
            return (255,255,0)
        if self.health_amount == 1:
            return (255,0,0)

class Lives():
    def __init__(self, life_amount):
        self.life_amount = life_amount
        
        
