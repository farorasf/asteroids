import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    
    def __init__(self, x:float, y:float):
        super().__init__(x, y, PLAYER_RADIUS)
        self.x = x
        self.y = y
        self.PLAYER_RADIUS = PLAYER_RADIUS
        self.speed = PLAYER_SPEED_MIN
        self.velocity_x = 0
        self.velocity_y = 0
        self.accelerate_x = 0
        self.accelerate_y = 0
        self.shot_cooldown = 0
        self.rotation = 0 #rotation of player ship
        self.movement_rotation = 0 #rotation of movement vector
        self.immunity_frames = 0
        self.just_respawned = False
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED*dt
    
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen) -> None:
        if self.immunity_frames > 10:
            pygame.draw.polygon(screen, "red", self.triangle(), LINE_WIDTH)
        else:
            pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
        
    def update(self, dt: float) -> None:
        self.hit_immunity()
        keys = pygame.key.get_pressed()
        self.move(dt)
        if REALISTIC_SPACE_MODE == False:
            if not keys[pygame.K_w]:
                self.decelerate(dt)  

        if self.just_respawned != True:
            if keys[pygame.K_a]:
                self.rotate(-dt)
            if keys[pygame.K_d]:
                self.rotate(dt)
            if keys[pygame.K_w]:
                self.accelerate(dt)
            if keys[pygame.K_s]:
                self.decelerate(dt)
            if keys[pygame.K_SPACE]:
                if self.shot_cooldown > 0:
                    pass
                else:
                    self.shoot()
                    self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
                                 
        if self.just_respawned == True:
            if self.immunity_frames < PLAYER_IMMUNITY_FRAMES * 1.5:
                self.just_respawned = False
        
        self.shot_cooldown -= dt    
            
    def move(self, dt):
        if REALISTIC_SPACE_MODE == True:
            velocity_vector = pygame.Vector2(self.velocity_x, self.velocity_y)
            if pygame.math.Vector2.length(velocity_vector) > PLAYER_SPEED_MAX:
                pygame.math.Vector2.scale_to_length(velocity_vector, PLAYER_SPEED_MAX)    
            self.position += velocity_vector * dt
            
        if REALISTIC_SPACE_MODE == False:
            unit_vector = pygame.Vector2(0,1)
            rotated_vector = unit_vector.rotate(self.rotation)
            rotated_with_speed_vector = rotated_vector * self.speed * dt
            self.position += rotated_with_speed_vector   
           
    def accelerate(self, dt):
        if REALISTIC_SPACE_MODE == True:
            new_vector = pygame.Vector2(0,1)
            new_rotated_vector = new_vector.rotate(self.rotation)          
            new_rotated_vector_speed = new_rotated_vector * PLAYER_ACCELERATION * dt

            self.accelerate_x = new_rotated_vector_speed[0]
            self.accelerate_y = new_rotated_vector_speed[1]
            self.velocity_x += self.accelerate_x
            self.velocity_y += self.accelerate_y
            
            
        if REALISTIC_SPACE_MODE == False:
            self.speed += PLAYER_ACCELERATION * dt
            if self.speed > PLAYER_SPEED_MAX:
                self.speed = PLAYER_SPEED_MAX
            
    def decelerate(self, dt):
        if REALISTIC_SPACE_MODE == True:
            new_vector = pygame.Vector2(0,1)
            new_rotated_vector = new_vector.rotate(self.rotation)          
            new_rotated_vector_speed = new_rotated_vector * PLAYER_ACCELERATION * dt

            self.accelerate_x = new_rotated_vector_speed[0]
            self.accelerate_y = new_rotated_vector_speed[1]
            self.velocity_x -= self.accelerate_x
            self.velocity_y -= self.accelerate_y
            
        if REALISTIC_SPACE_MODE == False:
            keys = pygame.key.get_pressed()
            if not keys[pygame.K_s]:
                if self.speed >= PLAYER_SPEED_MIN:
                    self.speed -= 1
                if self.speed <= PLAYER_SPEED_MIN:
                    self.speed += 1
            if keys[pygame.K_s]:
                self.speed -= 2
                if self.speed < -100:
                    self.speed = -100
        
    def shoot(self):
        shot = Shot(self.position[0], self.position[1])
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        
    def hit_immunity(self):
        self.immunity_frames -= 1
        if self.immunity_frames < 0:
            self.immunity_frames = 0
        return self.immunity_frames
        
        
        