import pygame
import math
from datetime import datetime

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("BTTF Clock Interface")

screen_size = (1280, 720)
center_point = (screen_size[0]/2+300, screen_size[1]/2)
radius_clock = 200

# Clock mark positions
start_8mark = 170
angles = (30, 60, 120, 150, 210, 240, 300, 330)
start_4matk = 185

# Fonts
font = pygame.font.SysFont("arial", 30)
digifont = pygame.font.Font("digital-7.ttf", 60)

# Roman numerals for clock face
roman_numbers = ("III", "VI", "IX", "XII")

# Button helper function
def draw_button(text, pos, size, color, text_color=(255,255,255)):
    rect = pygame.Rect(pos, size)
    pygame.draw.rect(screen, color, rect, border_radius=5)
    label = font.render(text, True, text_color)
    label_rect = label.get_rect(center=rect.center)
    screen.blit(label, label_rect)
    return rect

# Clock hand function
def hand(time_value, quarter_start_value, quarter_end_value, c, l, n, t):
    if time_value > quarter_start_value:
        actual_time_value = time_value - quarter_start_value
    else:
        actual_time_value = time_value + quarter_end_value
    degree_math = 360 / n
    end_x = center_point[0] + (radius_clock - l) * math.cos(math.radians(actual_time_value * degree_math))
    end_y = center_point[1] + (radius_clock - l) * math.sin(math.radians(actual_time_value * degree_math))
    pygame.draw.line(screen, c, center_point, (end_x, end_y), t)

# Clock mark positions
def startpos(angle):
    return (
        center_point[0] + radius_clock * math.cos(math.radians(angle)),
        center_point[1] + radius_clock * math.sin(math.radians(angle))
    )

def endpos(angle, mark):
    return (
        center_point[0] + mark * math.cos(math.radians(angle)),
        center_point[1] + mark * math.sin(math.radians(angle))
    )

# Draw rectangle
def rec(color, start, end, width, length):
    pygame.draw.rect(screen, color, (start, end, width, length))

# Time Panel labels
panel_labels = ["DESTINATION TIME", "PRESENT TIME", "LAST TIME DEPARTED"]

# Default times
destination_time = "21-10-1985 07:28"
last_time = "26-10-1985 01:21"
message = ""

# Timer for message duration
message_timer = 0
MESSAGE_DURATION = 3000  # ms

# Main loop
while True:
    screen.fill((192, 192, 192))
    pygame.draw.circle(screen, (0, 0, 0), center_point, 3)

    # Clock face
    pygame.draw.circle(screen, (90, 90, 90), center_point, radius_clock + 20)
    pygame.draw.circle(screen, (122, 122, 122), center_point, radius_clock)
    pygame.draw.circle(screen, (101, 67, 33), center_point, radius_clock + 2, 5)

    # Marks
    for angle in angles:
        pygame.draw.line(screen, (101, 67, 33), startpos(angle), endpos(angle, start_8mark))
    for i in range(4):
        angle = 90 * i
        pygame.draw.line(screen, (0, 0, 0), startpos(angle), endpos(angle, start_4matk), 2)

    # Roman numerals
    for i in range(4):
        angle = 90 * i
        x = center_point[0] + (radius_clock - 40) * math.cos(math.radians(angle))
        y = center_point[1] + (radius_clock - 40) * math.sin(math.radians(angle))
        text_surface = font.render(roman_numbers[i], True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)

    # Clock hands
    now = datetime.now()
    hand(now.second, 15, 45, (193, 154, 107), 10, 60, 1)
    hand(now.minute, 15, 45, (102, 76, 40), 30, 60, 3)
    hand(now.hour % 12, 3, 9, (50, 20, 20), 80, 12, 7)

    # Time panel
    center_point1 = (center_point[0] - 600, center_point[1])
    start_point = (center_point1[0] - 300, center_point1[1] - 200)
    rec((50, 50, 50), start_point[0], start_point[1], 600, 400)

    # DESTINATION TIME
    rec((80, 80, 80), start_point[0] + 5, start_point[1] + 10, 590, 120)
    rec((0, 0, 0), start_point[0] + 150, start_point[1] + 100, 300, 30)
    text_surface1 = font.render(panel_labels[0], True, (255, 255, 255))
    text_rect1 = text_surface1.get_rect(center=(start_point[0] + 300, start_point[1] + 115))
    screen.blit(text_surface1, text_rect1)
    text_surface1 = digifont.render(destination_time, True, (255, 0, 0))
    text_rect1 = text_surface1.get_rect(center=(start_point[0] + 300, start_point[1] + 70))
    screen.blit(text_surface1, text_rect1)

    # PRESENT TIME
    rec((80, 80, 80), start_point[0] + 5, start_point[1] + 135, 590, 120)
    rec((0, 0, 0), start_point[0] + 175, start_point[1] + 225, 250, 30)
    text_surface2 = font.render(panel_labels[1], True, (255, 255, 255))
    text_rect2 = text_surface2.get_rect(center=(start_point[0] + 300, start_point[1] + 240))
    screen.blit(text_surface2, text_rect2)
    present_time = now.strftime("%d-%m-%Y %H:%M:%S")
    text_surface2 = digifont.render(present_time, True, (0, 255, 0))
    text_rect2 = text_surface2.get_rect(center=(start_point[0] + 300, start_point[1] + 195))
    screen.blit(text_surface2, text_rect2)

    # LAST TIME DEPARTED
    rec((80, 80, 80), start_point[0] + 5, start_point[1] + 260, 590, 120)
    rec((0, 0, 0), start_point[0] + 125, start_point[1] + 350, 350, 30)
    text_surface3 = font.render(panel_labels[2], True, (255, 255, 255))
    text_rect3 = text_surface3.get_rect(center=(start_point[0] + 300, start_point[1] + 365))
    screen.blit(text_surface3, text_rect3)
    text_surface3 = digifont.render(last_time, True, (255, 255, 0))
    text_rect3 = text_surface3.get_rect(center=(start_point[0] + 300, start_point[1] + 320))
    screen.blit(text_surface3, text_rect3)

    # Buttons
    button1 = draw_button("Change Destination Time", (200, 600), (400, 50), (70, 70, 70))
    button2 = draw_button("Activate time Machine", (700, 600), (400, 50), ( 70, 70, 70))

    # Display message if exists
    if message and pygame.time.get_ticks() - message_timer < MESSAGE_DURATION:
        msg_surface = font.render(message, True, (255, 0, 0))
        screen.blit(msg_surface, (500, 300))
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
                last_time = present_time  # move current to last
                destination_time = "01-01-1955 06:00:00"
                message = "Destination time updated!"
                message_timer = pygame.time.get_ticks()

            elif button2.collidepoint(event.pos):
                # Time Trial message
                message = "You are not going 88 miles an hour."
                message_timer = pygame.time.get_ticks()
