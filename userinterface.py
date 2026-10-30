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
    
    def increase_score(self, score_class, increase, asteroid_radius):
        if asteroid_radius <= ASTEROID_MIN_RADIUS:
            score_class.score_amount += increase * 3
        elif ASTEROID_MIN_RADIUS < asteroid_radius < ASTEROID_MAX_RADIUS:
            score_class.score_amount += increase * 2
        else:
            score_class.score_amount += increase
            
class Userinterface():

    def ui_draw(self, screen, score_class, health_class, lives_class):
        draw_text(screen, f"Score: {score_class.score_amount}", text_font, (255,255,0), 10, 10)
        draw_text(screen, f"Health: {health_class.health_amount}", text_font, health_class.health_colour(), SCREEN_WIDTH/2 - 30, 10)
        draw_text(screen, f"Lives: {lives_class.life_amount}", text_font, (255,255,255), SCREEN_WIDTH - 125, 10)