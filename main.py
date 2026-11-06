import pygame, sys, os
pygame.init()
from logger import log_state, log_event
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from userinterface import *
from healthandlives import *
from explosion import *
from imageload import *



def main():
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    image_load_explosion()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    
    clock = pygame.time.Clock()
    dt = 0.0

    
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Explosion.containers = (updatable, drawable)
     
    afield = AsteroidField()
    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
    score = Score(0)
    health = Health(PLAYER_HEALTH)
    lives = Lives(PLAYER_LIVES)
    userinterface = Userinterface()
    
    

    
    while True:
        log_state()     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        userinterface.ui_draw(screen, score, health, lives)
        dt = clock.tick(60)/1000 #0.016
        
        updatable.update(dt)
             
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                if player.immunity_frames <= 0:
                    health.health_decrease()
                    player.immunity_frames = PLAYER_IMMUNITY_FRAMES
                if health.health_amount <= 0:
                    lives.life_decrease(health, player)
                    if lives.life_amount <= 0:
                        game_over(score)
                
            for shot in shots:
                if asteroid.collides_with(shot):
                    explosion = Explosion(screen, asteroid.position[0] - EXPLOSION_RADIUS/2, asteroid.position[1] - EXPLOSION_RADIUS/2)
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

                    score.increase_score(score, 1, asteroid.radius)
                    
           
        
        for drawables in drawable:
            drawables.draw(screen)
            
        pygame.display.flip()  
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
      

if __name__ == "__main__":
    main()
