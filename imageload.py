import pygame, os
from constants import *

def image_load_explosion():
    explosion_frames = [pygame.transform.scale(pygame.image.load(os.path.join(ROOT_PATH, r'images/explosionframes/frame_000.png')).convert_alpha(), (EXPLOSION_RADIUS, EXPLOSION_RADIUS)),
                        pygame.transform.scale(pygame.image.load(os.path.join(ROOT_PATH, r'images/explosionframes/frame_001.png')).convert_alpha(), (EXPLOSION_RADIUS, EXPLOSION_RADIUS)),
                        pygame.transform.scale(pygame.image.load(os.path.join(ROOT_PATH, r'images/explosionframes/frame_002.png')).convert_alpha(), (EXPLOSION_RADIUS, EXPLOSION_RADIUS)),
                        pygame.transform.scale(pygame.image.load(os.path.join(ROOT_PATH, r'images/explosionframes/frame_003.png')).convert_alpha(), (EXPLOSION_RADIUS, EXPLOSION_RADIUS)),
                        pygame.transform.scale(pygame.image.load(os.path.join(ROOT_PATH, r'images/explosionframes/frame_004.png')).convert_alpha(), (EXPLOSION_RADIUS, EXPLOSION_RADIUS)),
                        pygame.transform.scale(pygame.image.load(os.path.join(ROOT_PATH, r'images/explosionframes/frame_005.png')).convert_alpha(), (EXPLOSION_RADIUS, EXPLOSION_RADIUS)),
                        pygame.transform.scale(pygame.image.load(os.path.join(ROOT_PATH, r'images/explosionframes/frame_006.png')).convert_alpha(), (EXPLOSION_RADIUS, EXPLOSION_RADIUS)),
                        pygame.transform.scale(pygame.image.load(os.path.join(ROOT_PATH, r'images/explosionframes/frame_007.png')).convert_alpha(), (EXPLOSION_RADIUS, EXPLOSION_RADIUS)),
                        pygame.transform.scale(pygame.image.load(os.path.join(ROOT_PATH, r'images/explosionframes/frame_008.png')).convert_alpha(), (EXPLOSION_RADIUS, EXPLOSION_RADIUS)),
                        pygame.transform.scale(pygame.image.load(os.path.join(ROOT_PATH, r'images/explosionframes/frame_009.png')).convert_alpha(), (EXPLOSION_RADIUS, EXPLOSION_RADIUS)),
                        pygame.transform.scale(pygame.image.load(os.path.join(ROOT_PATH, r'images/explosionframes/frame_010.png')).convert_alpha(), (EXPLOSION_RADIUS, EXPLOSION_RADIUS)),
                        pygame.transform.scale(pygame.image.load(os.path.join(ROOT_PATH, r'images/explosionframes/frame_011.png')).convert_alpha(), (EXPLOSION_RADIUS, EXPLOSION_RADIUS)),
                        pygame.transform.scale(pygame.image.load(os.path.join(ROOT_PATH, r'images/explosionframes/frame_012.png')).convert_alpha(), (EXPLOSION_RADIUS, EXPLOSION_RADIUS)),
                        pygame.transform.scale(pygame.image.load(os.path.join(ROOT_PATH, r'images/explosionframes/frame_013.png')).convert_alpha(), (EXPLOSION_RADIUS, EXPLOSION_RADIUS)),
                        pygame.transform.scale(pygame.image.load(os.path.join(ROOT_PATH, r'images/explosionframes/frame_014.png')).convert_alpha(), (EXPLOSION_RADIUS, EXPLOSION_RADIUS)),
                        pygame.transform.scale(pygame.image.load(os.path.join(ROOT_PATH, r'images/explosionframes/frame_015.png')).convert_alpha(), (EXPLOSION_RADIUS, EXPLOSION_RADIUS)),
                        pygame.transform.scale(pygame.image.load(os.path.join(ROOT_PATH, r'images/explosionframes/frame_016.png')).convert_alpha(), (EXPLOSION_RADIUS, EXPLOSION_RADIUS))                   
    ]
    return explosion_frames
