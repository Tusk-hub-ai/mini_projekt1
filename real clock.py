import pygame
import math
from datetime import datetime


pygame.init()
screen = pygame.display.set_mode((820, 640))
screen.fill((255, 255, 255))
screen_size = (640,480)
def seconds(sek):
    return sek
    


while True:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()