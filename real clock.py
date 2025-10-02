import pygame
import math
from datetime import datetime

#basic parameters for python
pygame.init()
screen = pygame.display.set_mode((640, 480))

screen_size = (640,480)

#variable for the base circle
center_point = (screen_size[0]/2,screen_size[1]/2)
radius_clock = 200


#12 marks for the clock
start_8mark = 170
angles = (30,60,120,150,210,240,300,330)
start_4matk = 185


#function for the different hands
def hand (time_value,quarter_start_value,quarter_end_value,c,l,n,t):
        # time_value is the hand placement.
        # quarter_start_value is the number that the hand has on the first quartil.
        # quarter_end_value is the number that the hand has on the third quartil.
        # c is the color
        # l is the lengh takken of the hand(beginning at the circles radius)
        # n is the number that slices the hand's path on the circle.
        # t is the thickness
        
        if time_value > quarter_start_value:
            actual_time_value = time_value-quarter_start_value
        else:
            actual_time_value = time_value+quarter_end_value
        degree_math = 360/n
        end_x = center_point[0] + (radius_clock-l) * math.cos(math.radians((actual_time_value)*degree_math))
        end_y = center_point[1] + (radius_clock-l) * math.sin(math.radians((actual_time_value)*degree_math))
        end_point = (end_x, end_y)
        pygame.draw.line(screen, c, center_point, end_point, t)

#making a font for roman numbers
font = pygame.font.SysFont("arial",30)
roman_numbers = ("III","VI","IX","XII")
roman_angle = (90)
def startpos(angle):
    start_x_pos = center_point[0] + radius_clock * math.cos(math.radians(angle))  
    start_y_pos = center_point[1] + radius_clock * math.sin(math.radians(angle))
    start_pos = (start_x_pos,start_y_pos)
    return start_pos
def endpos(angle,mark):
    end_x_pos = center_point[0] + mark * math.cos(math.radians(angle))
    end_y_pos = center_point[1] + mark * math.sin(math.radians(angle))
    end_pos = (end_x_pos,end_y_pos)
    return end_pos

#main while
while True:
    #font for the pygame
    screen.fill((192,192,192))
    
    #center point
    pygame.draw.circle(screen,(0,0,0),center_point,3)
    
    
    #the base circle for the clock
    base_circle = pygame.draw.circle(screen,(122,122,122),center_point,radius_clock)
    base_circle = pygame.draw.circle(screen,(101,67,33),center_point,radius_clock+2,5)
    
    #8 marks
    for angle in angles:
        pygame.draw.line(screen,(101,67,33),startpos(angle),endpos(angle,start_8mark))
    #4 other marks
    for i in range(4):
        angle = 90*i
        pygame.draw.line(screen,(0,0,0),startpos(angle),endpos(angle,start_4matk),2)

    #4 roman marks used chat gpt for it
    for i in range(4):
        angle = 90*i
        x = center_point[0] + (radius_clock - 40) * math.cos(math.radians(angle))
        y = center_point[1] + (radius_clock - 40) * math.sin(math.radians(angle))
        
        # Render the Roman numeral
        text_surface = font.render(roman_numbers[i], True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(x, y))
        
        # Draw the Roman numeral
        screen.blit(text_surface, text_rect)
         
    
    #hand for seconds
    sec = datetime.now().second
    hand(sec,15,45,(193,154,107),10,60,1)
    
    #hand for minutes
    min = datetime.now().minute
    hand(min,15,45,(102,76,40),30,60,3)
    
    #hand for hours 
    hour = datetime.now().hour
    hand(hour,3,9,(50,20,20),80,12,7)

    
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()