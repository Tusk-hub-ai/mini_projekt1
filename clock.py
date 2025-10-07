import pygame
import math
from datetime import datetime

#basic parameters for python
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Back on the clock")

screen_size = (1280, 720)

#variable for the base circle
center_point = (screen_size[0]/2+300,screen_size[1]/2)
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

# functions that finds the 12 marks start and end position
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

#rectangle function
def rec(color,start,end,width,lenght):
    pygame.draw.rect(screen,color,(start,end,width,lenght))

#panel title
panel_labels = ["DESTINATION TIME", "PRESENT TIME", "LAST TIME DEPARTED"]
digifont = pygame.font.Font("digital-7.ttf",60)

# Default times and button message variable
destination_time = ""
message = ""

# Timer for message duration
message_timer = 0
MESSAGE_DURATION = 5000  # ms

# Button helper function help from chat gpt
def draw_button(text, pos, size, color, text_color=(255,255,255)):
    rect = pygame.Rect(pos, size)
    pygame.draw.rect(screen, color, rect, border_radius=5)
    label = font.render(text, True, text_color)
    label_rect = label.get_rect(center=rect.center)
    screen.blit(label, label_rect)
    return rect



#main while
while True:
    #font for the pygame
    screen.fill((192,192,192))
    
    #center point
    pygame.draw.circle(screen,(0,0,0),center_point,3)
    
    
    #the base circle for the clock
    base_circle = pygame.draw.circle(screen,(90,90,90),center_point,radius_clock+20)
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


    #render bttf time panel 
    center_point1 = (center_point[0]-600,center_point[1])
    start_point = (center_point1[0]-300,center_point1[1]-200)
    rec((50,50,50),start_point[0],start_point[1],600,400)


   #From now on, i had help from chatgpt to come up with clues, font metode, render, strftime. 
    #destination time
    rec((80,80,80),start_point[0]+5,start_point[1]+10,590,120)
    rec((0,0,0),start_point[0]+150,start_point[1]+100,300,30)
    # Render
    text_surface1 = font.render(panel_labels[0], True, (255, 255, 255))
    text_rect1 = text_surface1.get_rect(center=(start_point[0]+300,start_point[1]+115))
    # Draw text
    screen.blit(text_surface1, text_rect1)
    #clock present time
    text_surface1 = digifont.render(str(destination_time), True, (255, 0, 0))
    text_rect1 = text_surface1.get_rect(center=(start_point[0]+300,start_point[1]+70))
    screen.blit(text_surface1, text_rect1)
    
    #present time 
    rec((80,80,80),start_point[0]+5,start_point[1]+135,590,120)
    rec((0,0,0),start_point[0]+175,start_point[1]+225,250,30)
    # Render the Roman numeral
    text_surface2 = font.render(panel_labels[1], True, (255, 255, 255))
    text_rect2 = text_surface2.get_rect(center=(start_point[0]+300,start_point[1]+240))
    # Draw text
    screen.blit(text_surface2, text_rect2)
    #clock present timehelp from chat gpt
    present_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    text_surface2 = digifont.render(str(present_time), True, (0, 255, 0))
    text_rect2 = text_surface2.get_rect(center=(start_point[0]+300,start_point[1]+195))
    screen.blit(text_surface2, text_rect2)

    #last time departed
    rec((80,80,80),start_point[0]+5,start_point[1]+260,590,120)
    rec((0,0,0),start_point[0]+125,start_point[1]+350,350,30)
    # Render the Roman numeral
    text_surface3 = font.render(panel_labels[2], True, (255, 255, 255))
    text_rect3 = text_surface3.get_rect(center=(start_point[0]+300,start_point[1]+365))
    # Draw text
    screen.blit(text_surface3, text_rect3)
    #clock present time
    last_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    text_surface3= digifont.render(str(last_time), True, (255, 255, 0))
    text_rect3 = text_surface3.get_rect(center=(start_point[0]+300,start_point[1]+320))
    screen.blit(text_surface3, text_rect3)




      # Buttons
    button1 = draw_button("Change Destination Time", (200, 600), (400, 50), (70, 70, 70))
    button2 = draw_button("Activate time Machine", (700, 600), (400, 50), ( 70, 70, 70))

#Had help to make the if section underneeth and the pygame.event
    # Display message if exists
    if message and pygame.time.get_ticks() - message_timer < MESSAGE_DURATION:
        msg_surface = font.render(message, True, (0, 0, 0))
        screen.blit(msg_surface, (50, 100))
    elif pygame.time.get_ticks() - message_timer >= MESSAGE_DURATION:
        message = ""
   
    
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button1.collidepoint(event.pos):
                # Change destination time
                destination_time = "01-01-1955 06:00:00"
                message = "Destination time updated!"
                message_timer = pygame.time.get_ticks()

            elif button2.collidepoint(event.pos):
                # Time Trial message
                message = "You are not going 88 miles an hour and you are missing 1.21 gigawatts of eletrical power."
                message_timer = pygame.time.get_ticks()
