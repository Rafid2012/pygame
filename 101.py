import pygame
import sys
import random
import time

width,height = 800,600

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("pygame first window")

color = (255,0,0)

last_change = time.time()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    current_time = time.time()

    if current_time - last_change >= 5:
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        last_change = current_time

    screen.fill(color)
    pygame.display.flip()
