import pygame
import time

pygame.init()

#Define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
DARK_GREEN = (0,133,0)
LIGHT_GREEN = (0,183,0)

# Define display size
WIDTH, HEIGHT = 600, 400

# Create display
GAME_DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Define game clock
CLOCK = pygame.time.Clock()

# Define snake size
SNAKE_BLOCK = 10
SNAKE_SPEED = 15

# Define fonts
MESSAGE_FONT = pygame.font.SysFont('comicsansms', 30)
SCORE_FONT = pygame.font.SysFont('comicsansms', 35)

