import pygame, sys
from constants import *
from logger import log_state, log_event

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
        if self.health_amount <= 1:
            return (255,0,0)

class Lives():
    def __init__(self, life_amount):
        self.life_amount = life_amount
        
    def life_decrease(self, health_class, player_class):
        self.life_amount -= 1
        self.respawn(health_class, player_class)
              
    def respawn(self, health_class, player_class):
        player_class.just_respawned = True
        health_class.health_amount = PLAYER_HEALTH
        player_class.position[0] = SCREEN_WIDTH/2
        player_class.position[1] = SCREEN_HEIGHT/2
        player_class.rotation = 0
        player_class.immunity_frames = 2 * PLAYER_IMMUNITY_FRAMES
        

def game_over(score_class):
    log_event("player_hit")
    print("Game over!")
    print (f"Your score: {score_class.score_amount}")
    sys.exit()
        
        
