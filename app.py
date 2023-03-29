import pygame
import time
import random

pygame.init()

#Define colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

# Define display size
width, height = 800, 600

# Create display
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Define game clock
clock = pygame.time.clock()

# Define snake size
snake_block = 10
snake_speed = 15

# Define fonts
message_font = pygame.font.SysFont('comicsansms', 30)
score_font = pygame.font.SysFont('comicsansms', 35)