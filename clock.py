import pygame
import math
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((820, 640))
screen.fill((255, 255, 255))
#frame
screen_size = (820,640)
center_point = (screen_size[0]/2, screen_size[1]/2)
angles = [0,30,60,90,120,150,180,210,240,270,300,330]
length = 300

    
    
pygame.draw.circle(screen,(0,0,0),(center_point),(length),10)

# current time
now = datetime.now()
hour = now.hour
minute = now.minute
second = now.second
print(hour,minute,second)

while True:
    for angle in angles:
        end_x = center_point[0] + length * math.cos(math.radians(angle))
        end_y = center_point[1] + length * math.sin(math.radians(angle))
        end_point = (end_x, end_y)
    pygame.draw.line(screen, (0,0,0), center_point, end_point, 2)
    end_x = center_point[0] + length * math.cos(math.radians((datetime.now().second)*6))
    end_y = center_point[1] + length * math.sin(math.radians((datetime.now().second)*6))
    end_point = (end_x, end_y)
    pygame.draw.line(screen, (255,0,0), center_point, end_point, 2)
    pygame.display.flip()
    end_x = center_point[0] + length * math.cos(math.radians((datetime.now().second-1)*6))
    end_y = center_point[1] + length * math.sin(math.radians((datetime.now().second-1)*6))
    end_point = (end_x, end_y)
    if pygame.draw.line(screen, (255,0,0), center_point, end_point, 2):
        pygame.draw.line(screen, (255,255,255), center_point, end_point, 2)
    pygame.display.flip()
    



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()