import pygame
import os

RUNNING = [
    pygame.image.load(os.path.join("assets/Dino", "DinoRun1.png")),
    pygame.image.load(os.path.join("assets/Dino", "DinoRun2.png")),
]
JUMPING = pygame.image.load(os.path.join("assets/Dino", "DinoJump.png"))
DUCKING = [
    pygame.image.load(os.path.join("assets/Dino", "DinoDuck1.png")),
    pygame.image.load(os.path.join("assets/Dino", "DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join("assets/Cactus", "SmallCactus1.png")),
    pygame.image.load(os.path.join("assets/Cactus", "SmallCactus2.png")),
    pygame.image.load(os.path.join("assets/Cactus", "SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join("assets/Cactus", "LargeCactus1.png")),
    pygame.image.load(os.path.join("assets/Cactus", "LargeCactus2.png")),
    pygame.image.load(os.path.join("assets/Cactus", "LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join("assets/Bird", "Bird1.png")),
    pygame.image.load(os.path.join("assets/Bird", "Bird2.png")),
]

METEOR = [
    pygame.image.load(os.path.join("assets/Other", "MeteorFlying.png"))
]

CLOUD = pygame.image.load(os.path.join("assets/Other", "Cloud.png"))

BG = pygame.image.load(os.path.join("assets/Other", "Track.png"))

POWERUPS = [
    pygame.image.load(os.path.join("assets/Powerups", "p_four.png")),
    pygame.image.load(os.path.join("assets/Powerups", "p_five.png")),
    pygame.image.load(os.path.join("assets/Powerups", "p_three.png")),
    pygame.image.load(os.path.join("assets/Powerups", "p_two.png")),
    pygame.image.load(os.path.join("assets/Powerups", "p_one.png"))
]

TROPHY = [
    pygame.image.load(os.path.join("assets/Trophy", "pokal.png"))
]