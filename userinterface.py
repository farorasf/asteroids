import pygame, sys
from constants import *

text_font = pygame.font.SysFont("Arial", 30)

def draw_text(screen, text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))
    
class Score():
    def __init__(self, score = 0):
        self.score = score
    
    def increase_score(self, score, increase, asteroid_radius):
        if asteroid_radius <= ASTEROID_MIN_RADIUS:
            self.score += increase * 3
        elif ASTEROID_MIN_RADIUS < asteroid_radius < ASTEROID_MAX_RADIUS:
            self.score += increase * 2
        else:
            self.score += increase
