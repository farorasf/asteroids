import pygame, sys
pygame.init()
from logger import log_state, log_event
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from userinterface import *



def main():
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
     
    afield = AsteroidField()
    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
    score = Score(0)
    health = Health(PLAYER_HEALTH)
    
    while True:
        log_state()     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        draw_text(screen, f"Score: {score.score_amount}", text_font, (255,255,0), 10, 10)
        draw_text(screen, f"Health: {health.health_amount}", text_font, health.health_colour(), SCREEN_WIDTH-125, 10)
        dt = clock.tick(60)/1000 
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                if player.immunity_frames <= 0:
                    health.health_decrease()
                    player.immunity_frames = PLAYER_IMMUNITY_FRAMES
                if health.health_amount <= 0:
                    log_event("player_hit")
                    print("Game over!")
                    print (f"Your score: {score.score_amount}")
                    sys.exit()
                
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    score.increase_score(score.score_amount, 1, asteroid.radius)

        for drawables in drawable:
            drawables.draw(screen)
            
        pygame.display.flip()  
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
